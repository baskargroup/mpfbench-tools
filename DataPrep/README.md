# Dataset Preparation Script

## Overview
We offer the following 2 possibilities for data preparation for both the bubble and droplet datasets
- Without Padding - In this case the output tensor will take the form : Y[1000][t1..t2][u,v,c][256][512]
- With Padding - In this case the output tensor will take the form : Y[1000][t1..t2][u,v,c][512][512]
- Here, t1 => starting time step desired, t2 => ending time step desired, u,v => velocity fields, c => concentration


## Features

- Tensorizes all the raw data available from our download portal.
- User is able to specify the specific sets of time steps they are interested in training.
- User gets both the input tensor (X) and output tensor (Y)

## Requirements

- Python 3.9+
- Required library : numpy

## Usage
- Download all the data using the script provided in the Downloader directory. Untar all the files
- Point the appropriate python script (on of the four below) to this untarred location.
- For Preparing the Bubble Dataset with time steps t1...tN (N <= 200) time steps. ```python3 datasetGenBubble.py t1 t2```
- For Preparing the Bubble Dataset with time steps t1...tN (N <= 200) time steps. ```python3 datasetGenBubblePad.py t1 t2```
- For Preparing the Droplet Dataset with time steps t1...tN (N <= 200) time steps. ```python3 datasetGenDrop.py t1 t2```
- For Preparing the Bubble Dataset with time steps t1...tN (N <= 200) time steps. ```python3 datasetGenDropPad.py t1 t2```

