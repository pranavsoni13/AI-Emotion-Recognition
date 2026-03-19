from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base


class EmotionRecord(Base):
    __tablename__ = "emotion_records"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    emotions = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)