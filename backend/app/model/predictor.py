from transformers import pipeline
classifier = None

def get_model(text: str):
    global classifier
    if classifier is None:
        print("Loading model...")
        classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)
        print("Model loaded.")
    return classifier

def predict_emotions(text: str):
    try:
        model=get_model()
        result = model(text)[0]
        emotions={item["label"]:round(item["score"], 3) for item in result}
        return emotions
    except Exception as e:
        print(f"Error in prediction: {e}")
        return {"error": str(e)}