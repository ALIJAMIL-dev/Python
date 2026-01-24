'''
Image Generation: MNIST dataset
'''

# %% Libraries
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as Datasets
import torchvision.utils as utils
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np


# %% Dataset Preparation
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

batch_size = 128 # Mini Batch Size
image_size = 28*28 # Image Size

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, ), (0.5, )) # Normalization -> between -1 and 1
    ])

# Loading MNIST Dataset
dataset = Datasets.MNIST(root="./data", train=True, transform=transform, download=True)
# Loading the Dataset in batches
dataLoader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# %% Create Discriminator 

# %% Create Generator

# %% GAN Training

# %% Model Test & Performance Evaluation