from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

class InputData(BaseModel):
    complaint_text: str

# Load trained model and vectorizer
model = joblib.load("model/artifacts/recall_model.joblib")
vectorizer = joblib.load("model/artifacts/vectorizer.joblib")

@app.get("/")
def read_root():
    return {"msg": "Welcome to the Litigation Intelligence API"}

@app.post("/predict")
def predict(data: InputData):
    text_vec = vectorizer.transform([data.complaint_text])
    prediction = model.predict(text_vec)[0]
    return {"prediction": prediction}
