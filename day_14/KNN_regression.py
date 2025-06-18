from sklearn.datasets import load_diabetes
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Load diabetes dataset
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Test different K values for regression
k_values = [3, 5, 7, 9, 11, 15, 20]
results = {}

for k in k_values:
    # Create and train KNN regressor
    knn_regressor = KNeighborsRegressor(
        n_neighbors=k, weights="distance"  # Distance-weighted predictions
    )
    knn_regressor.fit(X_train_scaled, y_train)

    # Make predictions
    y_pred = knn_regressor.predict(X_test_scaled)

    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results[k] = {"mse": mse, "r2": r2}
    print(f"K={k}: MSE={mse:.2f}, R²={r2:.4f}")

# Find best K base
