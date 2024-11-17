from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import cv2
import pickle
import numpy as np
from utils import get_face_landmarks
import asyncio

# Initialize FastAPI app
app = FastAPI()

# Allow CORS for all origins (you can restrict this in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Emotion labels
emotions = ['ANGRY', 'SAD',  'HAPPY', 'CALM']

# Load the trained model
with open('./modelOne31.pkl', 'rb') as f:
    model = pickle.load(f)

# Video capture using OpenCV
camera = cv2.VideoCapture(0)

async def video_stream(websocket: WebSocket):
    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Resize and encode frame to JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # Send frame to the frontend
        await websocket.send_bytes(frame_bytes)

        # Process frame for emotion prediction
        face_landmarks = get_face_landmarks(frame, draw=False)
        if face_landmarks and len(face_landmarks) == 1404:
            prediction = model.predict([face_landmarks])
            emotion = emotions[int(prediction[0])]
            await websocket.send_text(emotion)
        else:
            await websocket.send_text("No face detected")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        await video_stream(websocket)
    except WebSocketDisconnect:
        print("Client disconnected")
    finally:
        camera.release()
