import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# Load preprocessed data
df = pd.read_csv("data/cleaned_preprocessed.csv")

# Features and target
X = df.drop("resale_price", axis=1)
y = df["resale_price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------- RANDOM FOREST --------------------
rf_model = RandomForestRegressor(n_estimators=80, random_state=42)
rf_model.fit(X_train, y_train)
joblib.dump(rf_model, 'models/rf_model.pkl')

# ----------------- GRADIENT BOOSTING -------------------
gb_model = GradientBoostingRegressor(random_state=42)

param_grid = {
    'n_estimators': [100, 200],
    'learning_rate': [0.01, 0.1],
    'max_depth': [3, 5],
    'min_samples_split': [2, 5],
    'subsample': [0.8, 1.0]
}

grid_search = GridSearchCV(gb_model, param_grid, cv=3, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
print(f"\n Best Gradient Boosting Params: {best_params}")

# Train with best params
gb_model = GradientBoostingRegressor(**best_params, random_state=42)
gb_model.fit(X_train, y_train)
joblib.dump(gb_model, 'models/gb_model.pkl')