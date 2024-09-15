// Import necessary libraries
import axios from 'axios';

// Set API endpoint URL
const API_URL = 'http://localhost:5000';

// Function to fetch detections from API
async function fetchDetections() {
    try {
        const response = await axios.get(API_URL + '/detections');
        const detections = response.data;
        return detections;
    } catch (error) {
        console.error(error);
    }
}

// Function to display detections
function displayDetections(detections) {
    const detectionsContainer = document.querySelector('.detections-container');
    detectionsContainer.innerHTML = '';
    detections.forEach(detection => {
        const detectionElement = document.createElement('div');
        detectionElement.classList.add('detection');
        detectionElement.innerHTML = `
            <h2>${detection.name}</h2>
            <p>Confidence: ${detection.confidence}</p>
            <p>Location: (${detection.x}, ${detection.y})</p>
        `;
        detectionsContainer.appendChild(detectionElement);
    });
}

// Fetch and display detections on page load
fetchDetections().then(detections => {
    displayDetections(detections);
});