// Function to fetch server health data from the backend
async function fetchServerHealth() {
    try {
        const response = await fetch('/health/');
        if (!response.ok) throw new Error('Network response was not ok');
        const data = await response.json();
        updateUI(data);
    } catch (error) {
        console.error('Error fetching server health data:', error);
        showError();
    }
}

// Function to update the UI with the fetched data
function updateUI(data) {
    // CPU Usage
    document.getElementById('cpu-value').textContent = data.cpu_usage;

    // Memory Usage
    document.getElementById('memory-total').textContent = data.memory.total;
    document.getElementById('memory-used').textContent = data.memory.used;
    document.getElementById('memory-percent').textContent = data.memory.percent;

    // Disk Usage
    document.getElementById('disk-total').textContent = data.disk.total;
    document.getElementById('disk-used').textContent = data.disk.used;
    document.getElementById('disk-percent').textContent = data.disk.percent;
}

// Function to show an error message in the UI
function showError() {
    document.querySelectorAll('.metric p').forEach((element) => {
        element.textContent = 'Error fetching data';
    });
}

// Poll server health data every 5 seconds
setInterval(fetchServerHealth, 5000);

// Initial fetch when the page loads
fetchServerHealth();
