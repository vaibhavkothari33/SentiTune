import pickle
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# Load data from the text file
data_file = "./data6_part.txt"
data = np.loadtxt(data_file)

# Split data into features (X) and labels (y)
X = data[:, :-1]  # Features are all columns except the last one
y = data[:, -1]   # Labels are the last column

# Normalize the feature set for better performance
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)

# Initialize the Random Forest Classifier with optimized parameters
rf_classifier = RandomForestClassifier(
    n_estimators=200,  # Increase number of trees
    max_depth=20,      # Limit tree depth to reduce overfitting
    min_samples_split=5,  # Minimum samples required to split a node
    min_samples_leaf=2,   # Minimum samples required in a leaf node
    random_state=42,
    class_weight="balanced"  # Handle class imbalance if any
)

# Fit the model
rf_classifier.fit(X_train, y_train)

# Predict on the test data
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Perform hyperparameter tuning using GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=3,
    n_jobs=-1,
    scoring='accuracy'
)
grid_search.fit(X_train, y_train)
best_params = grid_search.best_params_

print("Best Hyperparameters:", best_params)

# Train the final model with best parameters
best_rf_classifier = RandomForestClassifier(
    **best_params, random_state=42, class_weight="balanced"
)
best_rf_classifier.fit(X_train, y_train)

# Evaluate the tuned model
y_pred_tuned = best_rf_classifier.predict(X_test)
accuracy_tuned = accuracy_score(y_test, y_pred_tuned)
print(f"Tuned Accuracy: {accuracy_tuned * 100:.2f}%")
print("Tuned Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_tuned))
print("Tuned Classification Report:")
print(classification_report(y_test, y_pred_tuned))

# Save the tuned model and scaler to a file
with open('./model_tuned2.pkl', 'wb') as f:
    pickle.dump(best_rf_classifier, f)

with open('./scaler2.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("Tuned model saved as model_tuned.pkl and scaler.pkl")

