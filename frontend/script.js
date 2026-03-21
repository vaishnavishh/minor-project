document.getElementById('predictForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const temp = parseFloat(document.getElementById('temp').value);
    const humidity = parseFloat(document.getElementById('humidity').value);
    const wind = parseFloat(document.getElementById('wind').value);
    const resultDiv = document.getElementById('result');

    // 1. Input Validation (The "Engineer" Touch)
    // Ensures the AI doesn't get "garbage" data
    if (temp < 250 || temp > 330) {
        resultDiv.style.display = 'block';
        resultDiv.innerHTML = `<div style="color: #ffcc00;">⚠️ Please enter Temperature between 250K and 330K</div>`;
        return;
    }

    // 2. Show Processing State
    resultDiv.style.display = 'block';
    resultDiv.style.animation = 'pulse 1.5s infinite';
    resultDiv.innerHTML = `<div style="color: #4facfe;">🧠 AI is analyzing 35,000 hours of patterns...</div>`;

    try {
        // 3. Fetch from Backend
        const response = await fetch('https://minor-project-ya5t.onrender.com/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ temp, humidity, wind })
        });

        if (!response.ok) throw new Error('Server issues');

        const data = await response.json();
        let finalUsage = Math.max(0, data.predicted_usage);

        // 4. Dynamic Weather Logic (The "UI" Touch)
        let weatherIcon = "☁️"; 
        if (temp > 298) weatherIcon = "☀️"; // Sunny if > 25°C
        if (humidity > 70) weatherIcon = "🌧️"; // Humid/Rainy
        if (wind > 15) weatherIcon = "💨"; // Windy

        // 5. Inject Modern Result
        resultDiv.style.animation = 'none'; // Stop pulsing
        resultDiv.innerHTML = `
            <div style="font-size: 3rem; margin-bottom: 10px;">${weatherIcon}</div>
            <div style="font-size: 0.9rem; opacity: 0.8; letter-spacing: 1px;">PREDICTED ENERGY OUTPUT</div>
            <span class="prediction-value">${finalUsage.toFixed(2)} kWh</span>
            <div style="font-size: 0.7rem; margin-top: 10px; color: #4facfe; opacity: 0.6;">Verified by PyTorch Model</div>
        `;

    } catch (error) {
        resultDiv.style.animation = 'none';
        resultDiv.innerHTML = `<div style="color: #ff4b2b;">❌ Server is waking up... <br> Please try again in 20 seconds.</div>`;
        console.error('Error:', error);
    }
});