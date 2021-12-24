import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data.dataset import Dataset 
from torch.autograd import Variable
import numpy as np
import matplotlib.pyplot as plt
import psutil
from pathlib import Path
import datetime

device = 'cuda'

class Lin(nn.Module):
    def __init__(self):
        """ Define and instantiate your layers"""
        super(Lin, self).__init__()

        self.lstm1 = nn.LSTM(1, 10, batch_first=True)
        self.fc1 = nn.Linear(10, 160000)
        self.fc2 = nn.Linear(160000, 4)

    def forward(self, x):
        x, _ = self.lstm1(x)
        print(x.shape)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

net = Lin().to(device)
data = torch.tensor([[[1.0], [2.0]]], device=device)
print(net(data))
