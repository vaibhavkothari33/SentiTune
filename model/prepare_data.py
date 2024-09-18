# import os
# import cv2
# import numpy as np
# from utils import get_face_landmarks

# # data directory
# data_dir = './data'

# print("Current Working Directory:", os.getcwd())
# print(os.path.abspath(data_dir))


# output = []

# output = []
# for emotion_indx, emotion in enumerate(sorted(os.listdir(data_dir))):
#     for image_path_ in os.listdir(os.path.join(data_dir, emotion)):
#         image_path = os.path.join(data_dir, emotion, image_path_)

#         image = cv2.imread(image_path)
#         face_landmarks = get_face_landmarks(image)

#         if len(face_landmarks) == 1404: 
#             face_landmarks.append(int(emotion_indx))
#             output.append(face_landmarks)

# np.savetxt('data.txt', np.asarray(output))

# import os
# import cv2
# import numpy as np
# from concurrent.futures import ThreadPoolExecutor, as_completed
# from utils import get_face_landmarks

# # Data directory
# data_dir = './data'

# print("Current Working Directory:", os.getcwd())
# print(os.path.abspath(data_dir))

# output = []

# # Function to process each image
# def process_image(image_path, emotion_indx):
#     image = cv2.imread(image_path)
#     face_landmarks = get_face_landmarks(image)

#     if len(face_landmarks) == 1404:
#         face_landmarks.append(int(emotion_indx))
#         return face_landmarks
#     return None

# # Limit the number of threads
# max_threads = 4  # Adjust this number based on system capacity

# # Using ThreadPoolExecutor to process images with limited threads
# with ThreadPoolExecutor(max_workers=max_threads) as executor:
#     future_to_image = {}
    
#     for emotion_indx, emotion in enumerate(sorted(os.listdir(data_dir))):
#         emotion_dir = os.path.join(data_dir, emotion)
        
#         # Submit image processing tasks to the executor
#         for image_path_ in os.listdir(emotion_dir):
#             image_path = os.path.join(emotion_dir, image_path_)
#             future = executor.submit(process_image, image_path, emotion_indx)
#             future_to_image[future] = image_path
    
#     # Collecting results as they complete
#     for future in as_completed(future_to_image):
#         result = future.result()
#         if result is not None:
#             output.append(result)

# # Saving the output
# np.savetxt('data.txt', np.asarray(output))
import os
import cv2
import numpy as np
from utils import get_face_landmarks
from math import ceil

# Data directory
data_dir = './data'

print("Current Working Directory:", os.getcwd())
print(os.path.abspath(data_dir))

output = []
emotions = sorted(os.listdir(data_dir))

# Split data into 3 parts
num_parts = 3
num_emotions = len(emotions)
part_size = ceil(num_emotions / num_parts)

# Function to process each emotion's images
def process_emotions(start_idx, end_idx, part_num):
    output = []
    for emotion_indx in range(start_idx, end_idx):
        emotion = emotions[emotion_indx]
        emotion_dir = os.path.join(data_dir, emotion)
        
        for image_path_ in os.listdir(emotion_dir):
            image_path = os.path.join(emotion_dir, image_path_)
            image = cv2.imread(image_path)
            face_landmarks = get_face_landmarks(image)

            if len(face_landmarks) == 1404:
                face_landmarks.append(int(emotion_indx))
                output.append(face_landmarks)

    # Save to a separate file
    filename = f'data_part{part_num}.txt'
    np.savetxt(filename, np.asarray(output))
    print(f"Data saved to {filename}")

# Process data in 3 parts
for part_num in range(num_parts):
    start_idx = part_num * part_size
    end_idx = min(start_idx + part_size, num_emotions)
    process_emotions(start_idx, end_idx, part_num + 1)
