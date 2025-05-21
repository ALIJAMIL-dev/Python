# %% Create the Data and Visualize
import torch
import torchvision
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

def gen_data(seq_length = 50, num_samples = 1000):
    x = np.linspace(0, 100, num_samples)
    y = np.sin(x)
    sequence = []
    targets = []

    for i in range(len(x)-seq_length):
       sequence.append(y[i:i+seq_length])
       targets.append(y[i+seq_length])

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label="sin(t)", color="b", linewidth = 2)
    plt.title("Sinus Dalga Graphic")
    plt.xlabel("Time(Radition)")
    plt.ylabel("Genlik")
    plt.legend()
    plt.grid(True)
    plt.show()

    return np.array(sequence), np.array(targets)

sequence, targets = gen_data() 

# %% Create RNN Model
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1):

        super(RNN, self).__init__()
        self.rnn =nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.rnn(x)
        out = self.fc(out[:,-1,:])

        return out

model = RNN(1, 16, 1, 1)

# %% Training
seq_length = 50
input_size = 1
hidden_size = 16 
output_size = 1
num_layers = 1
epochs = 20
batch_size = 32
learning_rate = 0.001

X, y = gen_data(seq_length)
X = torch.tensor(X, dtype= torch.float32).unsqueeze(-1)
y = torch.tensor(y, dtype= torch.float32).unsqueeze(-1)

dataset = torch.utils.data.TensorDataset(X,y)
dataLoader = torch.utils.data.DataLoader(dataset, batch_size, shuffle=True)

model = RNN(input_size, hidden_size, output_size, num_layers)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

for epoch in range(epochs):
    for batch_x, batch_y in dataLoader:
        optimizer.zero_grad()
        pred_y = model(batch_x)
        loss = criterion(pred_y, batch_y)
        loss.backward()
        optimizer.step()
    print(f"Epoch: {epoch+1}/{epochs}, Loss: {loss.item():.4f}")
# %% RNN Test and Evaluation


