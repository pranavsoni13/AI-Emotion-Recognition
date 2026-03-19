import os
import torch
import pickle
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class EmotionPredictor:
    def __init__(self):
        print("Loading trained emotion model...")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, "..", "..", ".."))

        model_path = os.path.join(project_root, "models", "emotion_model")

        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)

        encoder_path = os.path.join(model_path, "label_encoder.pkl")

        with open(encoder_path, "rb") as f:
            self.label_encoder = pickle.load(f)

        print("Model loaded successfully!")

    def predict(self, text: str):

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True
        )

        with torch.no_grad():
            outputs = self.model(**inputs)

        probs = torch.nn.functional.softmax(outputs.logits, dim=1)[0]

        emotions = {}

        for i, score in enumerate(probs):
            emotion_name = self.label_encoder.inverse_transform([i])[0]
            emotions[emotion_name] = round(score.item(), 3)

        return emotions


predictor = EmotionPredictor()