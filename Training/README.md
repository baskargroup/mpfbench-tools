# ML Training

## Overview

This directory provides a comprehensive list of ML training scripts that can be used to train FNO and CNO models on our data. The idea is to train a Seq. to Seq models. e.g., we take inputs for N number of time steps of the simulation and output the next time step of the simulation. We have trained a total of 8 models. This repository contains the full code for all these experiments. 

## Features

- End to end code. Outputs various MSE statistics on a validation dataset.
- Four models each for CNO and FNO
	- 8 to 1 for Bubble - Take first 8 time steps of the simulation and predict the 9th time step
	- 8 to 1 for Drop - Take first 8 time steps of the simulation and predict the 9th time step
	- 4 to 1 for Bubble - Take first 4 time steps of the simulation and predict the 5th time step
	- 4 to 1 for Drop - Take first 4 time steps of the simulation and predict the 5th time step

## Requirements

- ```pip install requirements.txt```

## Usage
- Run ```data_prep.py```
- Under ```experiments``` directory, create a model specific directory e.g., ```cno_1``` or ```fno_1```. Within this second directory create a config file called ```config.yaml```. Follow the example we have provided in this repo.
- Adjust the following settings as required in the config file, if using CNO:

	- model: "cno"
	- file_path_x: ''
	- file_path_y: ''
	- batch_size: 5
	- split_fraction: 0.8
	- in_dim: 20
	- out_dim: 5
	- N_layers: 4
	- in_size: 512
	- out_size: 512
	- learning_rate: 0.001
	- num_epochs: 200
	- checkpoint_frequency: 50

- Adjust the the following settings as required in the config file, if using FNO:

	- model: "fno"
	- file_path_x: ''
	- file_path_y: ''
	- batch_size: 5
	- split_fraction: 0.8
	- n_modes:
  		- 32
  		- 32
	- n_layers: 5
	- in_channels: 20
	- out_channels: 5
	- hidden_channels: 32
	- projection_channels: 128
	- learning_rate: 0.001
	- num_epochs: 200
	- checkpoint_frequency: 50

- Run the script ```script.sh``` on a HPC server
- Training Results will be stored in a ```.out``` file.
- To output validation metrics per field, run ```out_of_sample.py``` 
