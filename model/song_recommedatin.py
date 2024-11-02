import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='6dc4020dac1a4f6b9fd42333b41de3d9',client_secret='ba0287b7b1d2484084793af64ae0fe88'))


mood_features = {
    'happy': {'valence': 0.8, 'energy': 0.8, 'danceability': 0.9, 'genres': ['bollywood', 'indian pop'], 'artists': ['Arijit Singh', 'Shreya Ghoshal']},
    'sad': {'valence': 0.2, 'energy': 0.3, 'danceability': 0.3, 'genres': ['hindi', 'romantic'], 'artists': ['Arijit Singh', 'Lata Mangeshkar']},
    'relaxed': {'valence': 0.6, 'energy': 0.4, 'danceability': 0.5, 'genres': ['chill', 'indian classical'], 'artists': ['Hariharan', 'Shankar Mahadevan']},
    'angry': {'valence': 0.3, 'energy': 0.9, 'danceability': 0.8, 'genres': ['bollywood', 'indian rock'], 'artists': ['Neha Kakkar', 'Badshah']}
}

def get_advanced_recommendations(mood):
    if mood in mood_features:
        features = mood_features[mood]
        
        # Fetch recommendations using genres and artists associated with Hindi music
        recommendations = sp.recommendations(seed_genres=features['genres'],
        seed_artists=get_artist_ids(features['artists']),
        limit=3,
        target_valence=features['valence'],
        target_energy=features['energy'],
        target_danceability=features['danceability'])
        
        print(f"\nSongs recommended for the mood: {mood.capitalize()} (Hindi Songs)\n")
        for track in recommendations['tracks']:
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            song_link = track['external_urls']['spotify'] 
            print(f"{track_name} by {artist_name} - Listen here: {song_link}\n")
    else:
        print("Mood not recognized. Try 'happy', 'sad', 'relaxed', or 'angry'.")

# Helper function to get artist IDs from artist names
def get_artist_ids(artist_names):
    artist_ids = []
    for artist in artist_names:
        results = sp.search(q=f'artist:{artist}', type='artist')
        if results['artists']['items']:
            artist_ids.append(results['artists']['items'][0]['id'])
    return artist_ids

mood_input = input("Enter your mood (happy, sad, relaxed, angry): ").lower()

get_advanced_recommendations(mood_input)