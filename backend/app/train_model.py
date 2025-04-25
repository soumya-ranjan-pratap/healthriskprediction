import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Load data
df = pd.read_csv("diabetes.csv")

# Step 2: Features & Target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Step 3: Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 5: Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 6: Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Step 7: Save model & scaler
joblib.dump(model, "health_model.pkl")
joblib.dump(scaler, "scaler.pkl")
