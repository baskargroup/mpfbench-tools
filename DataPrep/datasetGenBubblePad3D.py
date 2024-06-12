import os
import re
import numpy as np
import random
import logging
import argparse
import glob
import sys

def pad_array_to_center(original_array, pad_height, pad_width):
    # Calculate padding values for height and width
    pad_top = (pad_height - original_array.shape[2]) // 2
    pad_bottom = pad_height - original_array.shape[2] - pad_top
    pad_left = (pad_width - original_array.shape[3]) // 2
    pad_right = pad_width - original_array.shape[3] - pad_left
    
    # Pad the array
    padded_array = np.pad(original_array, ((0, 0), (0, 0), (pad_top, pad_bottom), (pad_left, pad_right)), mode='constant')
    return padded_array


# Configure logging
#log_filename = f'/work/mech-ai-scratch/mehdish/projects/Flowbench/GPUruns/Processed/dataset/bubble_processed_filenames.log'
log_filename = ''
logging.basicConfig(filename=log_filename, 
                    level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Base directory containing the bubbleGroup directories
#base_directory = '/work/mech-ai-scratch/mehdish/projects/Flowbench/GPUruns/Processed/2Dbubble'
base_directory = ''


# Output directory
#output_directory = '/work/mech-ai-scratch/mehdish/projects/Flowbench/GPUruns/Processed/dataset'
output_directory = ''

#Start time step
time_start = int(sys.argv[1])
time_end = int(sys.argv[2])
seed = 785

# Set the random seed
random.seed(seed)

# Initialize lists to store X and Y data
X = []
Y = []

# Regular expression pattern to extract the numbers from filenames
pattern = re.compile(r'bubble_(\d+)_([\d.]+)_([\d.]+)_([\d.]+).npz')

group_folders = glob.glob(os.path.join(base_directory, "bubbleGroup*_npz"))


# Process each bubble group directory
for group_folder in group_folders:

    # Get all NPZ files in the directory
    all_files = [filename for filename in os.listdir(group_folder) if filename.endswith('.npz')]

    # Randomly select 200 NPZ files
    selected_files = random.sample(all_files, 200)

    # Iterate over the selected NPZ files
    for filename in selected_files:
        # Log the filename
        logging.info(filename)
        
        # Extract the numbers from the filename
        match = pattern.match(filename)
        if match:
            rho_number = int(match.group(1))
            viscosity_number = int(match.group(2))
            Bo_number = int(match.group(3))
            Re_number = int(match.group(4))
            
            # Append the extracted numbers to X
            X.append([rho_number, viscosity_number, Bo_number, Re_number])
            
            # Load the data from the NPZ file
            data = np.load(os.path.join(group_folder, filename))['data']
            
            tmp = data[time_start:time_end, :, :, :]
            
            # Desired dimensions
            pad_height = 512
            pad_width = 512
    
            # # Pad the array
            tmp = pad_array_to_center(tmp, pad_height, pad_width)
            
            
            # Append the data to Y
            Y.append(tmp)

# Convert X and Y to numpy arrays
X = np.array(X)
Y = np.array(Y)


# Print shapes to verify
print("Shape :", Y.shape)

# Print shapes to verify
print("Shape :", X.shape)

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

np.savez_compressed(os.path.join(output_directory, 'Y_bubble.npz.npz'), Y=Y)
np.savez_compressed(os.path.join(output_directory, 'X_bubble.npz.npz'), X=X)
