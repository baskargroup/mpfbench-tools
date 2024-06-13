import numpy as np

if __name__ == '__main__':
    
    PATH = ''
    
    drop = np.load(PATH)['Y']
    
    #Prepare the data
    drop_data_4 = drop[:,:5,:,:,:] 
    
    #Prepare the data - 2
    drop_data_8 = drop[:,:9,:,:,:]
    
    #Prepare X and Y
    drop_data_X4 = drop_data_4[:,:4,:,:,:]
    drop_data_Y4 = drop_data_4[:,4,:,:,:]
    
    drop_data_X8 = drop_data_8[:,:8,:,:,:]
    drop_data_Y8 = drop_data_8[:,8,:,:,:]
    
    #Save the data
    np.savez_compressed('dropX4.npz', data = drop_data_X4)
    np.savez_compressed('dropY4.npz', data = drop_data_Y4)
    np.savez_compressed('dropX8.npz', data = drop_data_X8)
    np.savez_compressed('dropY8.npz', data = drop_data_Y8)
