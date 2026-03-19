from fastapi import APIRouter
from pydantic import BaseModel
from app.model.predictor import predict_emotion

router = APIRouter()

class TextInput(BaseModel):
    text: str

@router.post("/predict")
def predict(data:TextInput):
    result = predict_emotion(data.text)
    return result