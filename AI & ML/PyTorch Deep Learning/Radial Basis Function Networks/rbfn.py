# %% Libraries
import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# %% Prepairing Dataset & Preprocess
# Classification problem: Iris dataset, 3 classes
df = pd.read_csv("./data/iris.data", header=None)

X = df.iloc[:, :-1].values # Giving X the value of First 4 Columns (0, 1, 2, 3)
y, _ = pd.factorize(df.iloc[:, -1])

# Standarize the Data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train Test | Split to 2
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)

def to_tensor(data, target):
    return torch.tensor(data, dtype= torch.float32), torch.tensor(target, dtype= torch.long)

X_train, y_train = to_tensor(X_train, y_train)
X_test, y_test = to_tensor(X_test, y_test)
# %% Defining RBFN model & rbf_kernel
def rbf_kernel(X, centers, beta):
    return torch.exp(-beta * torch.cdist(X, centers)**2)

class RBFN(nn.Module):
    def __init__(self, input_dim, num_centers, output_dim):
        super(RBFN, self).__init__()
        self.centers = nn.Parameter(torch.randn(num_centers, input_dim)) # Start RBF's centers randomly
        self.beta = nn.Parameter(torch.ones(1) * 2.0) # Control wide of RBF's beta parameters
        self.Linear = nn.Linear(num_centers, output_dim) # Redirect Output -> Fully connected Layer
        
        
    def forward(self, x): # Forward propagation
        # Compute the RBF kernel 
        phi = rbf_kernel(x, self.centers, self.beta)
        return self.Linear(phi)
    
# %% Model Training

num_centers = 10
model = RBFN(input_dim=4, num_centers=num_centers, output_dim=3)

# Define Loss Function & Optimization
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr= 0.01)

# Train Model
num_epochs = 100
for epoch in range(num_epochs):
    optimizer.zero_grad() # Reset Grads
    outputs = model(X_train) # Prediction
    loss = criterion(outputs, y_train) # Calculate Loss
    loss.backward() # Backpropagation
    optimizer.step() # Update Weights
    
    if (epoch+1) % 10 == 0:
        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item():.4f}")

# %% Model Test & Performance Evaluation 
with torch.no_grad():
    y_pred = model(X_test)
    preds_test = torch.argmax(y_pred, dim=1)
    accuracy = (preds_test == y_test).float().mean().item()
    print("Accuracy:", accuracy)


















