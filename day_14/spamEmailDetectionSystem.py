# Example with text features (simplified)
# Features: word count, exclamation marks, capital letters ratio

import numpy as np
from sklearn.linear_model import LogisticRegression


# Sample data
email_features = np.array(
    [
        [50, 2, 0.1],  # Normal email
        [200, 8, 0.4],  # Likely spam
        [30, 0, 0.05],  # Normal email
        [150, 12, 0.6],  # Likely spam
    ]
)

spam_labels = np.array([0, 1, 0, 1])  # 0: Not spam, 1: Spam

# Train model
spam_detector = LogisticRegression()
spam_detector.fit(email_features, spam_labels)

# Predict new email
new_email = [[100, 5, 0.3]]
spam_probability = spam_detector.predict_proba(new_email)[0][1]
print(f"Spam probability: {spam_probability:.2f}")



