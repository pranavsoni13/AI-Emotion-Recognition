classifier = None

def predict_emotion(text: str):
    global classifier
    try:
        if classifier is None:
            print("Loading model...")
            from transformers import pipeline
            classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base",top_k=None)
            print("Model loaded successfully.")
        result = classifier(text)[0]
    
        emotions={item["label"]:round(item["score"], 3) for item in result}
        return emotions
    except Exception as e:
        print(f"Error in prediction: {e}")
        return {"error": str(e)}