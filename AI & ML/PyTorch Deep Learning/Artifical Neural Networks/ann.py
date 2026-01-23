"""
    Problem Definition: Number Classification Project with Mnist Data Set
    MNIST
    ANN: Artificial Neural Networks
"""

# %% Library
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

# Optional: Detect Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Data Set Loading
def get_data_loaders(batch_size = 64):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    # Data Sets
    train_set = torchvision.datasets.MNIST(root = "./data", train = True, download = True, transform = transform)
    test_set = torchvision.datasets.MNIST(root = "./data", train =  False, download = True, transform = transform)

    # Loaders
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_set, batch_size=batch_size, shuffle=False)

    return train_loader, test_loader

# Data Visualization
def visualize_samples(loader, n):
    images, labels = next(iter(loader))
    fig, axes = plt.subplots(1, n, figsize=(10, 5))
    for i in range(n):
        axes[i].imshow(images[i].squeeze(), cmap = "gray")
        axes[i].set_title(f"Label: {labels[i].item()}")
        axes[i].axis("off")
    plt.show()

# %% Define ANN Model

# ANN Class
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        
        # Converting Image to Vector (1D)
        self.flatten = nn.Flatten()

        # First Full Connected Layer
        self.fc1 = nn.Linear(28*28, 128)

        # Activation Func.
        self.relu = nn.ReLU()

        # Second Full Connected Layer
        self.fc2 = nn.Linear(128, 64)

        # Output Layer
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):

        # Converting Image to Vector (1D)
        x = self.flatten(x)

        # First Full Connected Layer
        x = self.fc1(x)

        # Activation Func.
        x = self.relu(x)

        # Second Full Connected Layer
        x = self.fc2(x)

        # Activation Func.
        x = self.relu(x)

        # Output Layer
        x = self.fc3(x)

        return x

# Create Model and Compile
# Define the loss Func and Optim Algorithm
define_loss_and_optimizer = lambda model: (
    nn.CrossEntropyLoss(),
    optim.Adam(model.parameters(), lr = 0.001)
)

# %% Train 
def train_model(model, train_loader, criterion, optimizer, epochs = 10):
    model.train()
    train_losses = []
    
    # Inputted Epoch Number as Training
    for epoch in range(epochs):
        total_loss = 0
        
        # All Training Data is under Iterasion 
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            predictions = model(images)
            loss = criterion(predictions, labels)
            loss.backward()
            optimizer.step()

            total_loss = total_loss + loss.item()

        avg_loss = total_loss / len(train_loader)
        train_losses.append(avg_loss)

        print(f"Epoch: {epoch+1}/{epochs}, Loss: {avg_loss:.3f}")
    
    # Loss Graph
    plt.figure()
    plt.plot(range(1, epochs + 1), train_losses, marker = "o", linestyle = "-", label = "Train Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.title("Training Loss")
    plt.legend()
    plt.show()

# %% Test
def test_model(model, test_loader):
    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            predictions = model(images)
            _, predicted = torch.max(predictions, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print(f"Test Accuracy: {100*correct/total:.3f}%")

# %% Main
if __name__ == "__main__":
    # Load Datasets
    train_loader, test_loader = get_data_loaders()

    # Visualize some sample digits
    visualize_samples(train_loader, 5)

    # Create Model and Move to Device
    model = NeuralNetwork().to(device)

    # Define Loss Function and Optimizer
    criterion, optimizer = define_loss_and_optimizer(model)

    # Train the Model
    train_model(model, train_loader, criterion, optimizer, epochs=5)

    # Test the Model
    test_model(model, test_loader)
