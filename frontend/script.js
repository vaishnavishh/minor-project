document.getElementById('predictForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const temp = document.getElementById('temp').value;
    const humidity = document.getElementById('humidity').value;
    const wind = document.getElementById('wind').value;
    const resultDiv = document.getElementById('result');

    // 1. Reveal the result box and show "Processing" state
    resultDiv.style.display = 'block';
    resultDiv.innerHTML = `<div style="color: #4facfe;">🧠 AI is analyzing patterns...</div>`;

    try {
        // 2. Fetch data from your Render Backend
        const response = await fetch('https://minor-project-ya5t.onrender.com/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ temp, humidity, wind })
        });

        if (!response.ok) throw new Error('Server issues');

        const data = await response.json();

        // 3. Clean up the prediction (ensuring no negative numbers)
        let finalUsage = Math.max(0, data.predicted_usage);

        // 4. Inject the beautiful result with the neon styling
        resultDiv.innerHTML = `
            <div style="font-size: 0.9rem; opacity: 0.8;">Predicted Solar Generation:</div>
            <span class="prediction-value">${finalUsage.toFixed(2)} kWh</span>
        `;

    } catch (error) {
        // 5. Handle errors (like if Render is sleeping)
        resultDiv.innerHTML = `<div style="color: #ff4b2b;">❌ Error: Server is waking up. Please try again in 30 seconds.</div>`;
        console.error('Error:', error);
    }
});