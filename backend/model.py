import torch
import torch.nn as nn
import os

class EnergyPredictor(nn.Module):
    def __init__(self):
        super(EnergyPredictor, self).__init__()
        self.layer1 = nn.Linear(3, 16)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(16, 1)

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        return x

if __name__ == '__main__':
    X = torch.tensor([
        [0.8, 0.4, 0.9],
        [0.2, 0.8, 0.1],
        [0.5, 0.5, 0.5],
        [0.9, 0.2, 0.8]
    ], dtype=torch.float32)
    
    y = torch.tensor([[85.0], [12.0], [45.0], [90.0]], dtype=torch.float32)

    model = EnergyPredictor()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    for epoch in range(500):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

    if not os.path.exists('../models'):
        os.makedirs('../models')
    
    torch.save(model.state_dict(), '../models/energy_model.pth')
    print("Brain saved successfully to: models/energy_model.pth")
