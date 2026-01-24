"""
Define Problem: Derivation Text with LSTM
"""

# %% Libraries
import torch
import torch.nn as nn
import torch.optim as optim
from collections import Counter 
from itertools import product

# %% Data Loading and Preprocessing
text = """This product exceeded my expectations.,
    I'm very satisfied with the quality and performance.,
    Absolutely worth the price, highly recommended!,
    It works perfectly and arrived earlier than expected.,
    High quality, great design, and easy to use."""
       

# Data Preprocessing
# Get rid of punctuation marks
# Transforming to small letters
# Plenty Of Words

words = text.replace(".","").replace("'","").replace(",","").replace("!","").lower().split()

# Create Index and Calculate Frekans of Words
wordCounts = Counter(words)
vocab = sorted(wordCounts, key=wordCounts.get, reverse=True)
w2i = {word: i for i, word in enumerate(vocab)}
i2w = {i: word for i, word in enumerate(vocab)}
data = [(words[i], words[i+1]) for i in range(len(words)-1)]

# %% Define LSTM Module
class LSTM(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        # Calling Above class's constructor
        super(LSTM, self).__init__()
        # Embedding Layer
        self.embedding = nn.Embedding(vocab_size, embedding_dim) 
        # LSTM Layer
        self.lstm = nn.LSTM(embedding_dim, hidden_dim)
        # Fully connected Layer
        self.fc = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x):
        """
            input -> embedding -> lstm -> fc -> output
        """

        x = self.embedding(x) 
        lstm_out, _ = self.lstm(x.view(1,1,-1))
        output = self.fc(lstm_out.view(1,-1))
        return output

model = LSTM(len(vocab), embedding_dim=8, hidden_dim=32)

# %% Hyperparameter Tuning

# Word list -> Tensor
def prepare_sequence(seq, to_ix):
    return torch.tensor([to_ix[w] for w in seq], dtype= torch.long)

# Hyperparameter Tuning Combinations Determination
embedding_sizes = [8, 16] # Embedding sizes to try
hidden_sizes = [32, 64] # Hidden layer sizes to try
learning_rates = [0.01, 0.005] # Learning Rate

best_loss = float("inf") # Variable to store the lowest loss value
best_params = {} # Empty dictionary to store best parameters

print("Hyperparameter tuning starting...")

# Grid Search
for emb_size, hidden_size, lr in product(embedding_sizes, hidden_sizes, learning_rates):
    print(f"Test: Embedding: {emb_size}, Hidden: {hidden_size}, Learning Rate: {lr}")

    # Define Model
    model = LSTM(len(vocab), emb_size, hidden_size) # Create model with selected Parameters
    loss_function = nn.CrossEntropyLoss() # Entropy loss function
    optimizer = optim.Adam(model.parameters(), lr = lr) # Adam optimizer with selected lr

    epochs = 50
    total_loss = 0
    for epoch in range(epochs):
        epoch_loss = 0.0 # Resets Epoch Loss in the beginning
        for word, next_word in data:
            model.zero_grad() # Resets Grads
            input_tensor = prepare_sequence([word], w2i) # Transform Input to Tensor
            target_tensor = prepare_sequence([next_word], w2i) # Transform Target Word to Tensor
            output = model(input_tensor) # Prediction
            loss = loss_function(output, target_tensor) 
            loss.backward() # Apply Backpropagation
            optimizer.step() # Update Parameters
            epoch_loss += loss.item()

        if epoch % 10 == 0:
            print(f"Epoch: {epoch}, Loss: {epoch_loss:.5f}")  
        total_loss = epoch_loss
        # Save Best Model
    if total_loss < best_loss:
        best_loss = total_loss
        best_params = {"embedding_dim": emb_size, "hidden_dim": hidden_size, "learning_rate": lr}

    print()


print(f"Best params: {best_params}")

# %% LSTM Training



# %% Test and Evaluation



