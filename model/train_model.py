import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
# Load data from the text file

    
data_file = "./data_part.txt"
data = np.loadtxt(data_file)
# Split data into features (X) and labels (y)
X = data[:, :-1]  # Features are all columns except the last one
y = data[:, -1]   # Labels are the last column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,shuffle=True)

# Initialize the Random Forest Classifier
rf_classifier = RandomForestClassifier()

# Train the classifier on the training data
rf_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = rf_classifier.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print(confusion_matrix(y_test, y_pred))

    # with open('./modelOne', 'wb') as f:
    #     pickle.dump(rf_classifier, f)


# import pickle
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, confusion_matrix

# # Initialize empty lists to store features (X) and labels (y)
# all_X = []
# all_y = []

# # Load data from the three batch files and accumulate
# # for i in range(1, 4):  # Assuming files are named data_part1.txt, data_part2.txt, data_part3.txt
# data_file = f"./data_part_one.txt"
# data = np.loadtxt(data_file)
    
#     # Separate features (X) and labels (y)
#     X = data[:, :-1]  # Features are all columns except the last one
#     y = data[:, -1]   # Labels are the last column
    
#     # Accumulate the data from all batches
#     all_X.append(X)
#     all_y.append(y)

# # # Concatenate all batches into a single dataset
# # all_X = np.vstack(all_X)
# # all_y = np.hstack(all_y)

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42, shuffle=True)

# # Initialize the Random Forest Classifier
# rf_classifier = RandomForestClassifier()

# # Train the classifier on the training data
# rf_classifier.fit(X_train, y_train)

# # Make predictions on the test data
# y_pred = rf_classifier.predict(X_test)

# # Evaluate the accuracy of the model
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy * 100:.2f}%")
# print(confusion_matrix(y_test, y_pred))

# Save the trained model to a file
with open('./modelOne2.pkl', 'wb') as f:
    pickle.dump(rf_classifier, f)

print("Model saved as modelOne.pkl")
