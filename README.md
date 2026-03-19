# AI Based Renewable Energy Usage Forecasting

## Project Overview
This project is a web-based application designed to forecast renewable energy usage based on environmental inputs (Temperature, Humidity, Wind Speed) using an Artificial Intelligence model. It features a fully functional frontend, a backend API connected to a NoSQL database, and an integrated PyTorch neural network.

## Project Details
**Course:** MINOR PROJECT(H)
**Group Number:** 206
**Team Members:**
* Vaishnavi Shukla (1230432688)
* Tanishk (1230432665)
* Vaidehi Gupta (1230432687)
* Vishwajeet (1230432707)

## Tech Stack
* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **AI Model:** PyTorch
* **Database:** MongoDB
* **Deployment:** Netlify (Frontend), Render (Backend)

## How to Run Locally

### Backend Setup
1. Open terminal and navigate to the `backend` folder.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`
4. Ensure MongoDB is running locally on port 27017.
5. Start the server: `python app.py`

### Frontend Setup
1. Open the `frontend` folder.
2. Open `index.html` in any modern web browser.
3. Enter the environmental parameters to see the AI prediction.

## Deployment Strategy
* **Render (Backend):** The Flask application will be hosted as a Web Service on Render. Environment variables (like `MONGO_URI` for MongoDB Atlas) will be configured in the Render dashboard.
* **Netlify (Frontend):** The `frontend` folder will be deployed to Netlify by simply dragging and dropping the folder into the Netlify dashboard. Before deploying, ensure the `fetch` URL in `script.js` is updated from `http://127.0.0.1:5000/predict` to the live Render backend URL.