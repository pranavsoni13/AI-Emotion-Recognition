import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["HF_TOKEN"],
)

def predict_emotion(text: str):
    result = client.text_classification(
        text,
        model="j-hartmann/emotion-english-distilroberta-base",
    )

    return {
        item.label: round(item.score, 3)
        for item in result
    }