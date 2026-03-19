from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.predict import router as predict_router
from app.routes.analytics import router as analytics_router
from app.database.database import engine, Base
from app.database import models

app = FastAPI(
    title="AI Emotion Recognition API",
    version="1.0"
)

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(predict_router)
app.include_router(analytics_router)