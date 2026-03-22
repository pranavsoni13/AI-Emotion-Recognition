from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.predict import router as predict_router
from app.routes.analytics import router as analytics_router
from app.database.database import engine, Base
from app.database import models
import os

app = FastAPI(
    title="AI Emotion Recognition API",
    description="A FastAPI backend for emotion recognition using a pre-trained model.",
    version="1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Status": "API is running"}

@app.get("/health")
def health():
    return {"Status": "Healthy"}

@app.get("/")
def home():
    return {"message": "Welcome to the AI Emotion Recognition API!"}

Base.metadata.create_all(bind=engine)

app.include_router(predict_router, tags=["Predict"])
app.include_router(analytics_router, prefix="/analytics", tags=["Analytics"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0",port=int(os.environ.get("PORT", 10000))) 