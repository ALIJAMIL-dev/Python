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

# %% Hyperparameter Tuning


# %% LSTM Training



# %% Test and Evaluation

model = LSTM(len(vocab), embedding_dim=8, hidden_dim=32)

