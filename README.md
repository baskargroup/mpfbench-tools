# MPF-Bench 


This is the repository for the [MPF-Bench](https://baskargroup.github.io/mpf-bench). It contains the link to the full dataset and the code used for training the SciML operators. 

MPF-Bench is an extensive dataset which contains over 11,000 two-phase bubble rise and droplet fall simulations. The dataset captures intricate physics by varying surface tension, density, and viscosity by several orders of mangintude. MPF-Bench will facilitate the development of SciML neural PDE solvers for complex multiphase fluid systems.

## Table of Contents

1. [Model](#model)
2. [Data](#data)
3. [Website](#website)

## Model

We provide workflows for training three known and widely used neural operators: Fourier Neural Operators (FNO), Convolutional Neural Operators (CNO), and Deep Operator Networks (DeepONets). The full implementations of these three networks are included and explained here.

## Data

MPF-Bench offers over 11,000 solutions for two-phase bubble rise and droplet flow dynamics in both 2D and 3D. Simulation include a wide range of flow scenarios including two orders of magnitude of surface tension and density/viscosity ratio. Our solutions are available as a time sequences for both 2D and 3D. This dataset is specifically designed to support the development of next-generation scientific machine learning (SciML) neural PDE solvers, particularly those tackling complex multiphase flows.


<h2 id="paper">Website</h2>

We have a [project website](https://baskargroup.github.io/mpf-bench) which highlights MPF-Bench main results. Our website gives an overview of our dataset, solver, SciML training, and our research team that worked on this project.

