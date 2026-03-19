from fastapi import FastAPI
from app.routes.predict import router as predict_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is Working!"}

app.include_router(predict_router)