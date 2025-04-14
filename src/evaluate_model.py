import numpy as np
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Load preprocessed data
df = pd.read_csv("data/cleaned_preprocessed.csv")

# Features and target
X = df.drop("resale_price", axis=1)
y = df["resale_price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------- EVALUATE RANDOM FOREST --------------------
rf_model = joblib.load('models/rf_model.pkl')
y_pred_rf = rf_model.predict(X_test)

mse_rf = mean_squared_error(y_test, y_pred_rf)
rmse_rf = np.sqrt(mse_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print(f" Random Forest - R²: {r2_rf:.2f}, RMSE: Rs{rmse_rf:.0f}, MSE: Rs{mse_rf:.0f}")


# -------------------- EVALUATE GRADIENT BOOSTING --------------------
gb_model = joblib.load('models/gb_model.pkl')
y_pred_gb = gb_model.predict(X_test)

mse_gb = mean_squared_error(y_test, y_pred_gb)
rmse_gb = np.sqrt(mse_gb)
r2_gb = r2_score(y_test, y_pred_gb)

print(f" Gradient Boosting - R²: {r2_gb:.2f}, RMSE: Rs{rmse_gb:.0f}, MSE: Rs{mse_gb:.0f}")
