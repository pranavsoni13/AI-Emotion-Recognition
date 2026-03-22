
classifier = None

def get_model():
    global classifier
    if classifier is None:
        from transformers import pipeline
        print("Loading model...")
        classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", top_k=None)
        print("Model loaded.")
    return classifier

def predict_emotion(text: str):
    try:
        model=get_model()
        result = model(text)[0]
        emotions={item["label"]:round(item["score"], 3) for item in result}
        return emotions
    except Exception as e:
        print(f"Error in prediction: {e}")
        return {"error": str(e)}