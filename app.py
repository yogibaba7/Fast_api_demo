from fastapi import FastAPI , Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

model_api_url = 'https://fast-api-demo-iygd.onrender.com/predict'

@app.get("/",response_class=HTMLResponse)
def get_form(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/",response_class=HTMLResponse)
def predict_from_form(request:Request,
                      Pregnancies:int = Form(...),
                      Glucose:int = Form(...),
                      BloodPressure:int = Form(),
                      SkinThickness : int = Form(),
                      Insulin:int = Form(...),
                      BMI: float = Form(...),
                      DiabetesPedigreeFunction:float = Form(...),
                      Age:int = Form(...)):
        input_data = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age}
        response = requests.post(model_api_url,json=input_data)

        if response.status_code==200:
              prediction = response.json()
        else:
              prediction = "Could not get prediction"
        
        return templates.TemplateResponse('index.html',{'request':request,'prediction':prediction})

    
    
