from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.utils import predict_message

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Allow all domains (frontend)
    allow_credentials=True,
    allow_methods=["*"],       # Allow all HTTP methods
    allow_headers=["*"],       # Allow all headers
)

class SMSRequest(BaseModel):
    message: str

@app.post("/predict")
def predict_sms(request: SMSRequest):
    pred = predict_message(request.message)
    return {"message": request.message, "prediction": pred}

@app.get("/")
def home():
    return {"status": "SMS Spam Classifier API Running!"}
