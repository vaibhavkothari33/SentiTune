# import pickle
# import cv2
# from utils import get_face_landmarks

# emotions = ['ANGRY', 'DISGUSTED', 'FEARFUL',"hAPPY","NEUTRAL"]

# with open('./model1', 'rb') as f:
#     model = pickle.load(f)

# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()

# while ret:
#     ret, frame = cap.read()

#     face_landmarks = get_face_landmarks(frame, draw=True, static_image_mode=False)

#     output = model.predict([face_landmarks])

#     cv2.putText(frame,emotions[int(output[0])],(10, frame.shape[0] - 1),cv2.FONT_HERSHEY_SIMPLEX,3,(0, 255, 0),5)

#     cv2.imshow('frame', frame)

#     cv2.waitKey(25)


# cap.release()
# cv2.destroyAllWindows()


import pickle
import cv2
from utils import get_face_landmarks

# Emotion labels
emotions = ['ANGRY', 'DISGUSTED', 'FEARFUL', 'HAPPY', 'NEUTRAL']

# Load the trained model from the file
with open('./modelOne2.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Read the first frame
ret, frame = cap.read()

# Start the video stream
while ret:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Get face landmarks from the frame (removed 'static_image_mode' argument)
    face_landmarks = get_face_landmarks(frame, draw=True)

    # Check if face_landmarks has valid length (as per your training data)
    if face_landmarks and len(face_landmarks) == 1404:
        # Make a prediction using the trained model
        output = model.predict([face_landmarks])

        # Display the predicted emotion on the frame
        emotion_label = emotions[int(output[0])]
        cv2.putText(frame, emotion_label, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 5)

    else:
        # If no face or incomplete landmarks detected, display message
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
