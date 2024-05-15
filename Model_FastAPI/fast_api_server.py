from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ETL import ETL_final

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost",
    'http://127.0.0.1:5501',
    'http://127.0.0.1:5502',
    'http://127.0.0.1:5500',
    

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


#uvicorn fast_api_server:app --reload

class Measuers(BaseModel):
    Pregnancies : int
    Insulin : float
    Glucose : float
    BloodPressure : float
    bmi :float
    age : int




@app.post("/predict_diabetes/")
async def predict_diabetes(data: Measuers):
    try:
        print(type(data))
        Pregnancies = data.Pregnancies
        Insulin = data.Insulin
        Glucose = data.Glucose
        BloodPressure = data.BloodPressure
        bmi = data.bmi
        age = data.age

        print("Data before ETL:", Pregnancies, Insulin,Glucose,BloodPressure,bmi,age)
        print("_________")
        predict_result = ETL_final([Pregnancies, Insulin,Glucose,BloodPressure,bmi,age])
        print("_________")
 
        print(predict_result)

        result = "Negative" if predict_result == "Not DIABETES" else "Positive"

  

        return {"predict_result": result}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
