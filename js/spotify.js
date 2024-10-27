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

// Function to fetch Hindi songs based on mood with multiple artist seeds
async function getHindiSongsByMood(mood) {
    try {
        const token = await getSpotifyAccessToken();

        // Define multiple artist IDs to use as seeds for each mood
        const genreArtistMap = {
            happy: { genre: 'pop, bollywood', artistIds: ['3fDFFhD8jtvqH3V3EZN5Y7', '3QJzdZJYIAcoET1GcfpNGi'] }, // Arijit Singh, Neha Kakkar
            sad: { genre: 'indian pop, bollywood', artistIds: ['5f4QpKfy7ptCHwTqspnSJI', '1mYsTxnqsietFxj1OgoGbG'] }, // Shreya Ghoshal, A.R. Rahman
            energetic: { genre: 'punjabi, world-music', artistIds: ['6Xzy8ls1xEEnwt7ezCOZ2Y', '1tqhsYv8yBBdwANFNzHtcr'] }, // Diljit Dosanjh, Badshah
            calm: { genre: 'indian classical, bollywood', artistIds: ['5hAhrnb0Ch4ODwWu4tsbpi', '3rkZY3T2SkXZHF7f5qGLZT'] } // Anoushka Shankar, Hariharan
        };

        // Get the genre and artist IDs for the selected mood, default to "bollywood" genre and popular artists
        const { genre, artistIds } = genreArtistMap[mood] || { genre: 'bollywood', artistIds: ['3fDFFhD8jtvqH3V3EZN5Y7', '1mYsTxnqsietFxj1OgoGbG'] };

        // Generate artist seed parameter by joining artist IDs
        const seedArtists = artistIds.join(',');

        // Fetch recommendations using both genre and multiple artist seeds
        const response = await fetch(`https://api.spotify.com/v1/recommendations?seed_genres=${genre}&seed_artists=${seedArtists}&limit=5`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (!response.ok) {
            throw new Error('Failed to fetch Hindi song recommendations');
        }

        const data = await response.json();
        console.log("API Response:", data); // Debugging

        return data.tracks || []; // Return an empty array if no tracks are found
    } catch (error) {
        console.error('Error fetching Hindi songs based on mood:', error);
        return []; // Return an empty array if an error occurs
    }
}

// Event listener to use getHindiSongsByMood
document.getElementById('get-songs-btn').addEventListener('click', async () => {
    const mood = document.getElementById('mood-input').value.toLowerCase().trim();

    if (!mood) {
        alert('Please enter a mood.');
        return;
    }

    // Get the recommended Hindi songs based on mood
    const songs = await getHindiSongsByMood(mood);

    // Clear previous song list
    const predictionsList = document.getElementById('predictions-list');
    predictionsList.innerHTML = '';

    if (songs.length === 0) {
        const listItem = document.createElement('li');
        listItem.textContent = 'No Hindi songs found for this mood. Please try a different mood.';
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
