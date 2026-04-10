import requests

API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"

headers = {
    "Authorization": "Bearer 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"
}

def predict_emotion(text: str):
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": text}
        )

        data = response.json()

        # 🔴 agar error aaya HF se
        if isinstance(data, dict) and "error" in data:
            return {"error": data["error"]}

        # ✅ safe access
        result = data[0]

        emotions = {
            item["label"]: round(item["score"], 3)
            for item in result
        }

        return emotions

    except Exception as e:
        print("🔥 ERROR:", e)
        return {"error": str(e)}