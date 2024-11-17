import pickle
import cv2
from utils import get_face_landmarks
import numpy as np

# Emotion labels
emotions = ['ANGRY', 'SAD', 'HAPPY', 'CALM']

# Load the scaler and trained model
with open('./scaler2.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('./model_tuned2.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Start the video stream
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Mirror the frame (flip horizontally)
    frame = cv2.flip(frame, 1)

    # Get face landmarks from the frame
    face_landmarks = get_face_landmarks(frame, draw=True)
    
    if face_landmarks and len(face_landmarks) == 1404:
        # Scale the features before prediction
        scaled_landmarks = scaler.transform([face_landmarks])
        
        # Make a prediction using the trained model
        output = model.predict(scaled_landmarks)

        # Display the predicted emotion on the frame
        emotion_label = emotions[int(output[0])]
        cv2.putText(frame, emotion_label, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5)
    else:
        # If no face or incomplete landmarks detected, display a message
        cv2.putText(frame, 'No face detected or invalid landmarks', (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show the frame with the predicted emotion or error message
    cv2.imshow('Emotion Detection', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the webcam and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
