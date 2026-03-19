from transformers import pipeline

classifier = None

def get_model():
    global classifier
    if classifier is None:
        classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base",top_k=None)
    print("Model loaded successfully.")
    return classifier

def predict_emotion(text: str):
    model = get_model()
    results = model(text)[0]
    
    emotions={item["label"]:round(item["score"], 3) for item in results}
    return emotions