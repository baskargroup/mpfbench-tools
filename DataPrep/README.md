# Dataset Preparation Script

## Overview
We offer the following 2 possibilities for data preparation for both the bubble and droplet datasets
- Without Padding - In this case the output tensor will take the form : ```Y[1000][t1..t2][u,v,c][256][512]```
- With Padding - In this case the output tensor will take the form : ```Y[1000][t1..t2][u,v,c][512][512]```
- Here, t1 => starting time step desired, t2 => ending time step desired, u,v => velocity fields, c => concentration
- We provide a tensor containing all the relevant dimensionless numbers i.e., density ratio, viscosity ratio, Bond number and  Reynolds number for the simulation. This tensor looks as follows ```X[1000][rho,mu,Bo,Re][256][512]``` or ```X[1000][rho,mu,Bo,Re][512][512]``` depending on whether a dataset is requested with padding or without padding.


## Features

- Tensorizes all the raw data available from our download portal.
- User is able to specify the specific sets of time steps they are interested in training.
- User gets both the input tensor (X) and output tensor (Y)

## Requirements

- Python 3.9+
- Required library : numpy

## Usage
- Download all the data using the script provided in the Downloader directory. Untar all the files
- In the script indicate the base\_directory (where the untarred files are located) and the output\_directory where you desire the ML tensors to be dumped.
- Specify log\_filename in the script
- For Preparing the 2D Bubble Dataset with time steps t1...t2 (N <= 200) time steps. ```python3 datasetGenBubble2D.py t1 t2```
- For Preparing the 2D Bubble Dataset with time steps t1...t2 (N <= 200) time steps. ```python3 datasetGenBubblePad2D.py t1 t2```
- For Preparing the 2D Droplet Dataset with time steps t1...t2 (N <= 200) time steps. ```python3 datasetGenDrop2D.py t1 t2```
- For Preparing the 2D Bubble Dataset with time steps t1...t2 (N <= 200) time steps. ```python3 datasetGenDropPad2D.py t1 t2```

