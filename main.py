from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np 


# load model
model = joblib.load('model.pkl')

app = FastAPI()

# Define the expected input format
class InputData(BaseModel):
    Pregnancies: int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int

@app.get("/")
def read_root():
    return 'welcome to my model'

@app.post("/predict")
def predict(data: InputData):
    input_array = np.array([[data.Pregnancies, data.Glucose, data.BloodPressure,data.SkinThickness,data.Insulin,data.BMI,data.DiabetesPedigreeFunction,data.Age]])

    prediction = model.predict(input_array)
    return int(prediction[0])
