from fastapi import APIRouter
from app.schemas.request import TextRequest
from app.model.predictor import predictor
from app.database.database import SessionLocal
from app.database.models import EmotionRecord
import json

router = APIRouter()


@router.post("/predict")
def predict_emotion(request: TextRequest):
    result = predictor.predict(request.text)

    # save to database
    db = SessionLocal()
    record = EmotionRecord(
        text=request.text,
        emotions=json.dumps(result)
    )
    db.add(record)
    db.commit()
    db.close()

    return result