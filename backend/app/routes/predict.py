from fastapi import APIRouter
from pydantic import BaseModel
from app.model.predictor import predict_emotion

router = APIRouter()

class TextInput(BaseModel):
    text: str

@router.post("/predict")
def predict(data:TextInput):
    try:
        emotions = predict_emotion(data.text)
        return {"emotions": emotions}
    except Exception as e:
        print(f"Error in /predict: {e}")
        return {"error": str(e)}