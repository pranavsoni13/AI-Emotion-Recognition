from transformers import pipeline

class EmotionPredictor:
    def __init__(self):
        print("Loading HuggingFace model...")
        self.classifier=pipeline("text-classification",model="j-hartmann/emotion-english-distilroberta-base",top_k=None,device=-1)
        print("Model Loaded!")
    def predict(self,text:str):
        result=self.classifier(text)[0]
        return {
            item["label"].lower():round(item["score"],3)
            for item in result
        }
predictor = EmotionPredictor()