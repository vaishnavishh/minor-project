import torch
import torch.nn as nn
import os
import pandas as pd

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
    print("Loading massive datasets with Pandas... This might take a minute!")
    
    
    weather_df = pd.read_csv('weather_features.csv')
    energy_df = pd.read_csv('energy_dataset.csv')
    
    
    weather_df['dt_iso'] = pd.to_datetime(weather_df['dt_iso'], utc=True)
    energy_df['time'] = pd.to_datetime(energy_df['time'], utc=True)
    
    
    weather_avg = weather_df.groupby('dt_iso')[['temp', 'humidity', 'wind_speed']].mean().reset_index()
    
    
    merged_df = pd.merge(weather_avg, energy_df, left_on='dt_iso', right_on='time')
    
    
    merged_df = merged_df.dropna(subset=['temp', 'humidity', 'wind_speed', 'generation solar'])
    
    print(f"Successfully aligned {len(merged_df)} hours of historical data!")

   
    X_data = merged_df[['temp', 'humidity', 'wind_speed']].values[:5000]
    y_data = merged_df[['generation solar']].values[:5000]
    
    X = torch.tensor(X_data, dtype=torch.float32)
    y = torch.tensor(y_data, dtype=torch.float32)

    
    model = EnergyPredictor()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    print("Training the AI Brain... Please wait.")
    for epoch in range(1000):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        
        
        if epoch % 100 == 0:
            print(f"Training Cycle {epoch}/1000 completed...")

    
    if not os.path.exists('../models'):
        os.makedirs('../models')
    
    torch.save(model.state_dict(), '../models/energy_model.pth')
    print("Brain saved successfully to: models/energy_model.pth ")
