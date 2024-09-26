# Hindi Song Recommender based on Mood 🎵

This Python project recommends **Hindi songs** from Spotify based on the user's mood. It utilizes the **Spotify Web API** and allows users to input their mood manually, then suggests songs accordingly. Each song recommendation includes a **Spotify link** for direct listening.

## Features

- Advanced **mood detection**: The script suggests songs based on four predefined moods: `happy`, `sad`, `relaxed`, and `angry`.
- Focus on **Hindi music**: The recommendations prioritize Hindi genres such as Bollywood, Indian pop, and classical, and feature well-known Indian artists.
- Songs come with **direct Spotify links** so users can listen with just one click.
- Uses Spotify's **valence**, **energy**, and **danceability** parameters to match songs to moods accurately.

## Mood to Feature Mapping

The system maps each mood to a set of **musical features**:

- **Happy**: Songs with high valence, high energy, and danceability (Genres: Bollywood, Indian Pop).
- **Sad**: Songs with low valence, low energy, and slower pace (Genres: Hindi, Romantic).
- **Relaxed**: Calm and soothing songs with mid valence and lower energy (Genres: Chill, Indian Classical).
- **Angry**: Songs with high energy and intensity (Genres: Bollywood, Indian Rock).

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/vaibhavkothari33/speech_to_handsign.git
    cd hindi-song-recommender
    ```

2. **Install the required Python libraries**:

    You need to install `spotipy`, a lightweight Python library for the Spotify Web API.

    ```bash
    pip install spotipy
    ```

3. **Set up your Spotify Developer Account**:

   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Create an app to get your **Client ID** and **Client Secret**.
   - Update the script with your credentials in the following lines:

    ```python
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='your_client_id',
                                                               client_secret='your_client_secret'))
    ```

## Usage

1. **Run the script**:

    ```bash
    python song_recommender.py
    ```

2. **Enter your mood** when prompted:

    ```bash
    Enter your mood (happy, sad, relaxed, angry): happy
    ```

3. The script will recommend songs and provide clickable Spotify links for each recommendation:

    ```
    Songs recommended for the mood: Happy (Hindi Songs)
    
    Tum Hi Ho by Arijit Singh - Listen here: https://open.spotify.com/track/1cHZdj1HjIPovrXKHY9LwA

    Pal by Shreya Ghoshal - Listen here: https://open.spotify.com/track/2JdLR91NnBxMSUosfUB1rC
    ```

## Advanced Configuration

### Mood Mapping

You can customize the `mood_features` dictionary to include more moods or change the mood-to-feature mapping.

For example, to add a new mood like `excited`, you can add this to the dictionary:

```python
'excited': {'valence': 0.9, 'energy': 0.9, 'danceability': 0.95, 'genres': ['bollywood', 'party'], 'artists': ['Neha Kakkar', 'Badshah']}
