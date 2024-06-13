import os
import yaml
import torch
import torch.nn as nn
from codes.utils.device import device
from codes.models.FNO import TensorizedFNO
from codes.models.CNO import CompressedCNO
from codes.data.dataset import LidDrivenDataset
from codes.utils.visualization import plot_ldc_like

#from sklearn.metrics import mean_squared_error

def all_error_metrics(y_true, y_pred):
    
    mse = nn.MSELoss()

    u_field = y_true[:,0,:,:]
    v_field = y_true[:,1,:,:]
    c_field = y_true[:,2,:,:]
    
    u_pred = y_pred[:,0,:,:]
    v_pred = y_pred[:,1,:,:]
    c_pred = y_pred[:,2,:,:]
    
    u_mse = mse(u_field, u_pred)
    v_mse = mse(v_field, v_pred)
    c_mse = mse(c_field, c_pred)
    
    return u_mse, v_mse, c_mse

def read_yaml_file(folder_path, file_name):
    """Reads a YAML file and returns the data."""
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as exc:
            print(f"Error reading YAML file: {exc}")
            return None

dataset = LidDrivenDataset(file_path_x= '/work/mech-ai/rtali/MPSBench/mehdiMLData/samp_bubbleX8.npz', 
                           file_path_y = '/work/mech-ai/rtali/MPSBench/mehdiMLData/samp_bubbleY8.npz')

train_loader, val_loader = dataset.create_dataloader(batch_size= 3, split_fraction= 0, shuffle=False)


torch.cuda.empty_cache()

config_data = read_yaml_file('experiments/cno_1', "config.yaml")

CNO_trained_1 = CompressedCNO(in_dim = config_data['in_dim'], out_dim = config_data['out_dim'], 
                          N_layers = config_data['N_layers'], in_size = config_data['in_size'], 
                          out_size = config_data['out_size']).to(device)

CNO_trained_1.load_checkpoint(save_name="200", save_folder='experiments/cno_1/checkpoints')

mse_0 = 0
mse_1 = 0
mse_2 = 0

CNO_trained_1.eval()
with torch.no_grad():
    
    for batch in val_loader:
        inputs, targets = batch[0].to(device), batch[1].to(device)
        outputs = CNO_trained_1.forward(inputs)
    
        mses = all_error_metrics(targets, outputs)
        mse_0 += mses[0]
        mse_1 += mses[1]
        mse_2 += mses[2]
    
mse_0 = mse_0/len(val_loader.dataset)
mse_1 = mse_1/len(val_loader.dataset)
mse_2 = mse_2/len(val_loader.dataset)

print(config_data)
print('MSE(u) = {}, MSE(v) = {}, MSE(c) = {}'.format(mse_0, mse_1, mse_2))

