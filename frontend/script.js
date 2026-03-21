document.getElementById('predictForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const temp = document.getElementById('temp').value;
    const humidity = document.getElementById('humidity').value;
    const wind = document.getElementById('wind').value;
    const resultDiv = document.getElementById('result');

    resultDiv.innerText = "Processing...";

    const response = await fetch('https://minor-project-ya5t.onrender.com/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ temp, humidity, wind })
    });

    const data = await response.json();
    let finalUsage = Math.max(0, data.predicted_usage); 
    resultDiv.innerText = "Predicted Usage: " + finalUsage.toFixed(2) + " kWh";
    });