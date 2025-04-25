from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("health_model.pkl")
scaler = joblib.load("scaler.pkl")

class HealthInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.post("/predict")
def predict_health(data: HealthInput):
    input_data = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure,
                            data.SkinThickness, data.Insulin, data.BMI,
                            data.DiabetesPedigreeFunction, data.Age]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    return {"prediction": "Positive" if prediction == 1 else "Negative"}
