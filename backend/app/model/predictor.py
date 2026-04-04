import requests

API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"

headers = {
    "Authorization": "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"
}

def predict_emotion(text: str):
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": text}
        )
        result = response.json()[0]

        emotions = {
            item["label"]: round(item["score"], 3)
            for item in result
        }

        return emotions

    except Exception as e:
        return {"error": str(e)}