"""
    Problem Definition: Data Composing -> Autoencoders
    Data: FashionMNIST
"""

# %% Libraries
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms, datasets
import matplotlib.pyplot as plt
import numpy as np

# %% Dataset Preparation & Preprocessing
transform = transforms.Compose([transforms.ToTensor()]) # Convert Images to Tensor

# Download the dataset & Load it
train_dataset = datasets.FashionMNIST(root="./data", train=True, transform=transform, download=True)
test_dataset = datasets.FashionMNIST(root="./data", train=False, transform=transform, download=True)

# Batch size
batch_size = 128

# Train & Test Data Loaders
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)


# %% Developing Autoencoders 
class AutoEncoder(nn.Module):
    
    def __init__(self):
        super(AutoEncoder, self).__init__()
        
        # Encoder
        self.encoder = nn.Sequential(
            nn.Flatten(), # 28*28 -> 784 Vector
            nn.Linear(28*28, 256), # Fully Connected Layer -> 256
            nn.ReLU(), # Activation method
            nn.Linear(256, 64), # FIlly Connected Layer 256 -> 64
            nn.ReLU()
            )
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(64, 256), # Fully Connected Layer -> 256
            nn.ReLU(), # Activation method
            nn.Linear(256, 28*28), # Fully Connected Layer 256 -> 28*28
            nn.Sigmoid(), # 0-1 
            nn.Unflatten(1, [1,28,28]) # 1D -> 28*28
            )
    
    def forward(self, x):
        encoded = self.encoder(x) # Encode Input
        decoded = self.decoder(encoded) # Convert Encoded data to Image 
        return decoded

# model = AutoEncoder()

# %% Callback: Early stopping
class EarlyStopping: # Early stopping (Callback)
    def __init__(self, patience=5, min_delta=0.001):
        self.patience = patience
        self.min_delta = min_delta
        self.best_loss = None
        self.counter = 0
    
    def __call__(self, loss):
        if self.best_loss is None or loss < self.best_loss - self.min_delta:
            self.best_loss = loss
            self.counter = 0
        else:
            self.counter += 1
            
        if self.counter >= self.patience:
            return True
        
        return False
            


# %% Model Training

# %% Model Testing