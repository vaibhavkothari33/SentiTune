// Select DOM elements
const video = document.getElementById('video');
const cameraToggle = document.getElementById('camera-toggle');

// Initialize camera stream
let stream = null;
let cameraOn = false;

// Start or stop camera
async function toggleCamera() {
    if (cameraOn) {
        // Stop the camera
        stream.getTracks().forEach(track => track.stop());
        video.srcObject = null;
        cameraToggle.textContent = 'Start Camera';
    } else {
        try {
            // Request access to the camera
            stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
            cameraToggle.textContent = 'Stop Camera';
        } catch (error) {
            console.error('Error accessing camera: ', error);
        }
    }
    cameraOn = !cameraOn;
}

// Attach event listener to button
cameraToggle.addEventListener('click', toggleCamera);

// Start the camera on page load (optional)
// toggleCamera(); // Uncomment this if you want the camera to start automatically


// spotify.js
const clientId = 'ec966cbb22614e29995e738d2f71fcfd';
const clientSecret = '948c567f0bdc4a0d95c7c708322018ff';

// Function to get Spotify access token
async function getSpotifyAccessToken() {
    try {
        const response = await fetch('https://accounts.spotify.com/api/token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Basic ' + btoa(clientId + ':' + clientSecret)
            },
            body: 'grant_type=client_credentials'
        });

        const data = await response.json();
        return data.access_token;
    } catch (error) {
        console.error('Error fetching Spotify access token:', error);
    }
}

// Function to fetch songs based on mood
async function getSongsByMood(mood) {
    try {
        const token = await getSpotifyAccessToken();

        // Define genres based on mood input, fallback to 'pop' if mood not recognized
        const genreMap = {
            happy: 'pop',
            sad: 'blues',
            energetic: 'rock',
            calm: 'acoustic'
        };

        const genre = genreMap[mood] || 'pop'; // Default to 'pop' if mood is not mapped

        const response = await fetch(`https://api.spotify.com/v1/recommendations?seed_genres=${genre}&limit=5`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (!response.ok) {
            throw new Error('Failed to fetch song recommendations');
        }

        const data = await response.json();
        return data.tracks; // List of recommended tracks
    } catch (error) {
        console.error('Error fetching songs based on mood:', error);
        return []; // Return an empty array if an error occurs
    }
}

// Event listener for 'Get Songs' button
document.getElementById('get-songs-btn').addEventListener('click', async () => {
    const mood = document.getElementById('mood-input').value.toLowerCase().trim();

    if (!mood) {
        alert('Please enter a mood.');
        return;
    }

    // Get the recommended songs based on mood
    const songs = await getSongsByMood(mood);

    // Clear previous song list
    const predictionsList = document.getElementById('predictions-list');
    predictionsList.innerHTML = '';

    if (songs.length === 0) {
        const listItem = document.createElement('li');
        listItem.textContent = 'No songs found for this mood. Please try a different mood.';
        predictionsList.appendChild(listItem);
    } else {
        // Display recommended songs
        songs.forEach(song => {
            const listItem = document.createElement('li');
            listItem.textContent = `${song.name} by ${song.artists[0].name}`;
            predictionsList.appendChild(listItem);
        });
    }
});
