import requests
import os

API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"

headers = {
    "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
}

def predict_emotion(text: str):
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": text}
        )

        data = response.json()

        if isinstance(data, dict) and "error" in data:
            return {"error": data["error"]}

        result = data[0]

        emotions = {
            item["label"]: round(item["score"], 3)
            for item in result
        }

        return emotions

    except Exception as e:
        return {"error": str(e)}