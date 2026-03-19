from fastapi import APIRouter
from app.database.database import SessionLocal
from app.database.models import EmotionRecord
import json
from collections import Counter
from datetime import datetime

router = APIRouter()

@router.get("/analytics")
def get_analytics():

    db = SessionLocal()
    records = db.query(EmotionRecord).all()
    db.close()

    total_predictions = len(records)

    emotion_counter = Counter()

    for record in records:
        emotions = json.loads(record.emotions)

        # find highest emotion
        top_emotion = max(emotions, key=emotions.get)
        emotion_counter[top_emotion] += 1

    most_common = None
    if emotion_counter:
        most_common = emotion_counter.most_common(1)[0][0]

    return {
        "total_predictions": total_predictions,
        "most_common_emotion": most_common,
        "emotion_counts": dict(emotion_counter)
    }


@router.get("/emotion-timeline")
def emotion_timeline():

    db = SessionLocal()
    records = db.query(EmotionRecord).all()
    db.close()

    timeline = []

    for record in records:
        emotions = json.loads(record.emotions)
        top_emotion = max(emotions, key=emotions.get)

        timeline.append({
            "date": record.created_at.strftime("%Y-%m-%d"),
            "emotion": top_emotion
        })

    return {"timeline": timeline}