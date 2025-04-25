import React, { useState, ChangeEvent, FormEvent } from "react";
import axios from "axios";
import "./App.css";

type FormData = {
  Pregnancies: number;
  Glucose: number;
  BloodPressure: number;
  SkinThickness: number;
  Insulin: number;
  BMI: number;
  DiabetesPedigreeFunction: number;
  Age: number;
};

const defaultFormData: FormData = {
  Pregnancies: 0,
  Glucose: 0,
  BloodPressure: 0,
  SkinThickness: 0,
  Insulin: 0,
  BMI: 0,
  DiabetesPedigreeFunction: 0,
  Age: 0,
};

const App: React.FC = () => {
  const [formData, setFormData] = useState<FormData>(defaultFormData);
  const [prediction, setPrediction] = useState<string | null>(null);

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: parseFloat(value),
    });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://localhost:8000/predict", formData);
      setPrediction(res.data.prediction === "Positive" ? "Diabetic" : "Not Diabetic");
    } catch (err) {
      console.error("Prediction failed:", err);
      setPrediction("Something went wrong!");
    }
  };

  return (
    <div className="container">
      <h2>Health Risk Prediction</h2>
      <form onSubmit={handleSubmit}>
        {Object.entries(formData).map(([key, value]) => (
          <div className="form-group" key={key}>
            <label>{key}</label>
            <input
              type="number"
              name={key}
              value={value}
              onChange={handleChange}
              step="any"
              required
            />
          </div>
        ))}
        <button type="submit">Predict</button>
      </form>
      {prediction && <div className="result">Result: {prediction}</div>}
    </div>
  );
};

export default App;
