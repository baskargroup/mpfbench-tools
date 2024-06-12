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
- 
