document.getElementById('summarize-button').addEventListener('click', function() {
    const inputType = document.getElementById('input-type').value;
    const inputData = document.getElementById('input-data').value;
    const summaryText = document.getElementById('summary-text');

    // Basic input validation
    if (!inputData) {
        summaryText.textContent = "Please enter input data.";
        return;
    }

    // Call the Python backend (replace with your actual endpoint)
    fetch('/summarize', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            input_type: inputType,
            input_data: inputData
        })
    })
    .then(response => response.json())
    .then(data => {
        summaryText.textContent = data.summary;
    })
    .catch(error => {
        summaryText.textContent = "Error: " + error;
    });
});