from sklearn.datasets import load_wine
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score, train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import numpy as np

# Load wine dataset
wine = load_wine()
X, y = wine.data, wine.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Feature scaling (important for KNN!)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Find optimal K value
k_values = range(1, 21)
cv_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train_scaled, y_train, cv=5)
    cv_scores.append(scores.mean())

# Plot K vs accuracy
plt.figure(figsize=(10, 6))
plt.plot(k_values, cv_scores, marker="o")
plt.title("KNN: K Value vs Cross-Validation Accuracy")
plt.xlabel("K Value")
plt.ylabel("Cross-Validation Accuracy")
plt.grid(True)
plt.show()

# Train with optimal K
optimal_k = k_values[np.argmax(cv_scores)]
print(f"Optimal K: {optimal_k}")

knn_classifier = KNeighborsClassifier(n_neighbors=optimal_k)
knn_classifier.fit(X_train_scaled, y_train)

# Make predictions
y_pred = knn_classifier.predict(X_test_scaled)

# Evaluate
print(classification_report(y_test, y_pred, target_names=wine.target_names))
