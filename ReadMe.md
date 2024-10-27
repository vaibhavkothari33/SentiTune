# SentiTune 🎶

SentiTune is an intelligent music recommendation web app designed to suggest songs based on the user's mood. Using a combination of AI and Spotify's vast music catalog, SentiTune detects emotions and serves up playlists that match each user's current vibe.

## Objective

The main goal of SentiTune is to recommend songs based on the detected mood of the user, making music discovery more personalized and dynamic.

## Tech Stack

- **Languages**:
  - **Python** for the AI model
  - **HTML**, **CSS**, and **JavaScript** for the frontend
- **Backend**:
  - **FastAPI** with **Uvicorn** as the ASGI server
- **APIs**:
  - **Spotify API** for recommending songs based on mood
- **Additional Libraries**:
  - `scikit-learn`, `numpy`, `pandas` for AI model processing
  - `dotenv` for secure API key management

## Getting Started

### Clone the Repository

To run SentiTune on your local machine, start by cloning the repository:

```bash
git clone https://github.com/vaibhavkothari33/SentiTune.git
```

## Install Requirements

Navigate to the project directory and install the dependencies for the backend:

```bash
pip install -r requirements.txt
```

Frontend: Open index.html in your browser to load the interface.

## AI Model

Our AI model currently achieves **89% accuracy** in mood prediction. It supports the following mood categories:

- **Happy**
- **Sad**
- **Energetic**
- **Angry**
- **Calm**

## Future Goals

- **Improve Accuracy**: Enhance the accuracy of mood prediction through additional training data and refined model parameters.
- **Expanded Mood Categories**: Add support for a wider variety of moods.
- **Additional Features**:
  - **Customizable Playlists**: Allow users to create and save playlists based on specific moods.
  - **User Feedback**: Integrate a feedback loop so users can rate song recommendations, improving the accuracy of future suggestions.
  - **Mood History**: Track past moods and recommendations for personalized insights.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## Team Name : LeetRankers

### Vaibhav Kothari E23CSEU1451

E23CSEU1451@bennett.edu.in

### Srishti Singh E23CSEU1449

E23CSEU1449@bennett.edu.in

### Pranjal Srivastava E23CSEU1443

E23CSEU1443@bennett.edu.in

Happy tuning! 🎧
