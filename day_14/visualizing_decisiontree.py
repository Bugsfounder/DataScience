# Import necessary libraries
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_iris, make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import numpy as np

# Load the famous Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the Decision Tree
dt_classifier = DecisionTreeClassifier(
    max_depth=3,  # Limit depth to prevent overfitting
    min_samples_split=2,  # Minimum samples required to split a node
    min_samples_leaf=1,  # Minimum samples required at leaf node
    random_state=42,
)

dt_classifier.fit(X_train, y_train)

# Make predictions
y_pred = dt_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Feature importance
feature_importance = dt_classifier.feature_importances_
print("\nFeature Importance:")
for i, importance in enumerate(feature_importance):
    print(f"{iris.feature_names[i]}: {importance:.4f}")


# Visualize the decision tree
plt.figure(figsize=(20, 10))
plot_tree(
    dt_classifier,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True,
    fontsize=10,
)
plt.title("Decision Tree for Iris Classification")
plt.show()

# Real-world example: Customer Churn Prediction
# Sample customer data
customer_data = np.array(
    [
        [25, 50000, 2, 1],  # Age, Income, Years, Churned
        [45, 80000, 5, 0],  # Age, Income, Years, Stayed
        [30, 45000, 1, 1],  # Age, Income, Years, Churned
        [35, 75000, 8, 0],  # Age, Income, Years, Stayed
    ]
)

X_customer = customer_data[:, :-1]  # Features
y_customer = customer_data[:, -1]  # Target

# Train churn prediction model
churn_model = DecisionTreeClassifier(max_depth=2)
churn_model.fit(X_customer, y_customer)

# Predict for new customer
new_customer = [[28, 55000, 3]]
churn_prediction = churn_model.predict(new_customer)
print(f"Churn prediction: {'Will churn' if churn_prediction[0] else 'Will stay'}")
