from fastapi import APIRouter

router = APIRouter()


@router.post("/predict")
def predict():
    return {"msg": "This is the predict endpoint!"}