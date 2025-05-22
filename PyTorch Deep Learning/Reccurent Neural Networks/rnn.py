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

# Creating Datas for Testing
X_test = np.linspace(100, 110, seq_length).reshape(1,-1)
y_test = np.sin(X_test)

X_test2 = np.linspace(120, 130, seq_length).reshape(1,-1)
y_test2 = np.sin(X_test2)

X_test = torch.tensor(y_test, dtype= torch.float32).unsqueeze(-1)
X_test2 = torch.tensor(y_test2, dtype= torch.float32).unsqueeze(-1)

model.eval()
prediction1 = model(X_test).detach().numpy()
prediction2 = model(X_test2).detach().numpy()

plt.figure()
plt.plot(np.linspace(0, 100, len(y)), y, marker = "o", label = "Training Dataset")
plt.plot(X_test.numpy().flatten(), marker = "o", label = "Test 1")
plt.plot(X_test2.numpy().flatten(), marker = "o", label = "Test 2")

plt.plot(np.arange(seq_length, seq_length+1), prediction1.flatten(), "ro", label = "Prediction 1")
plt.plot(np.arange(seq_length, seq_length+1), prediction2.flatten(), "ro", label = "Prediction 2")

plt.legend()
plt.show()