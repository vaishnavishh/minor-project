from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import torch
from model import EnergyPredictor
import os

app = Flask(__name__)
CORS(app)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["energy_db"]
collection = db["predictions"]

model = EnergyPredictor()
model.load_state_dict(torch.load('models/energy_model.pth', map_location='cpu'))
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [float(data['temp']), float(data['humidity']), float(data['wind'])]
    input_tensor = torch.tensor([features], dtype=torch.float32)

    with torch.no_grad():
        prediction = model(input_tensor).item()

    record = {
        "input": data,
        "prediction": prediction
    }
    collection.insert_one(record)

    return jsonify({"predicted_usage": prediction})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email == "admin@nexenergy.com" and password == "admin123":
        return jsonify({"success": True, "message": "Authentication successful"}), 200
    else:
        return jsonify({"success": False, "message": "Invalid email or password"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)