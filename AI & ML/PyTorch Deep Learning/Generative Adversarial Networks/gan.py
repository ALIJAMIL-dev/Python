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
class Discriminator(nn.Module):
    # Discriminator: Image Classification (Real, Fake)
    def __init__(self):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(image_size, 1024), # Input: image size, 1024: Output of 1024 Neural network 
            nn.LeakyReLU(0.2), # Activation function & 0.2 negative slope
            nn.Linear(1024, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 1), # Output Layer
            nn.Sigmoid() # Make output between 0-1
            )
        
        
    def forward(self, img):
        return self.model(img.view(-1, image_size)) # Making the image 1D and then give it to model

# %% Create Generator
class Generator(nn.Module):
    # Generate Image(28*28) 
    def __init__(self, z_dim):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(z_dim, 256), # Input, 256 Fully Connected Layer
            nn.ReLU(), # Activator function
            nn.Linear(256, 512), # 256, 512 FC layer
            nn.ReLU(),
            nn.Linear(512, 1024),
            nn.ReLU(),
            nn.Linear(1024, image_size), # From 1024 to 28*28 (784)
            nn.Tanh() # Out Activation Function
            )
        
    def forward(self, x):
        return self.model(x).view(-1, 1, 28, 28) # Converts output to 28*28 Image

# %% GAN Training

# Hyperparameters
lr = 0.0002 # Learning Rate
z_dim = 100 # Random noise vector dimension
epochs = 20 # Epochs

# Start Model: Define Generator & Discriminator
generator = Generator(z_dim).to(device)
discriminator = Discriminator().to(device)

# Define: Loss Function & Optimization Algorithms
criterion = nn.BCELoss() # Binary Cross Entropy
g_optimizer = optim.Adam(generator.parameters(), lr = lr, betas = (0.5, 0.999)) # Generator Optimizer
d_optimizer = optim.Adam(discriminator.parameters(), lr = lr, betas = (0.5, 0.999)) # Discriminator Optimizer

# Launching training cycle
for epoch in range(epochs):    
    for i, (real_imgs, _) in enumerate(dataLoader): # Loading Images
        real_imgs = real_imgs.to(device) 
        batch_size = real_imgs.size(0) # Obtain the current batch size
        real_labels = torch.ones(batch_size, 1).to(device) # Label Real Images as 1
        fake_labels = torch.zeros(batch_size, 1).to(device) # Label Fake Images as 0
        
        # Training Discriminator
        z = torch.randn(batch_size, z_dim).to(device) # Make Random noises
        fake_imgs = generator(z) # Make Fake Images with Generator
        real_loss = criterion(discriminator(real_imgs), real_labels) # Real Image Loss
        fake_loss = criterion(discriminator(fake_imgs.detach()), fake_labels) # Fake Image Loss
        d_loss = real_loss + fake_loss # Total Discriminator Loss
        
        d_optimizer.zero_grad() # Reset Grads
        d_loss.backward() # Backpropagation
        d_optimizer.step() # Update Parameters
        
        # Training Generator
        g_loss = criterion(discriminator(fake_imgs), real_labels) # Generator Loss
        g_optimizer.zero_grad() # Reset Grads
        g_loss.backward() # Backpropagation
        g_optimizer.step() # Update Parameters
     
    print(f"Epoch {epoch+1}/{epochs} d_loss: {d_loss.item():.3f}, g_loss: {g_loss.item():.3f}")

# %% Model Test & Performance Evaluation

# Making Noises with Random Noise
with torch.no_grad():
    z = torch.randn(16, z_dim).to(device) # Make 16 Random Noises
    sample_images = generator(z).cpu() # Making Fake Images with Generator
    grid = np.transpose(utils.make_grid(sample_images, nrow=4, normalize=True), (1, 2, 0)) # Display images in Grid
    plt.imshow(grid)
    plt.show( )