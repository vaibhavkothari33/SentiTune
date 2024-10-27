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

toggleCamera();


// spotify.js
