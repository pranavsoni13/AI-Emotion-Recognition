import os
from datasets import load_dataset
import pandas as pd

# -------- Paths --------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_PATH = os.path.join(DATA_DIR, "emotions_grouped.csv")

os.makedirs(DATA_DIR, exist_ok=True)

# -------- Load dataset --------
dataset = load_dataset("go_emotions")

train_data = dataset["train"]

df = pd.DataFrame(train_data)

# convert label IDs → emotion names
emotion_names = dataset["train"].features["labels"].feature.names

# keep first emotion label only
df["emotion"] = df["labels"].apply(
    lambda x: emotion_names[x[0]] if len(x) > 0 else None
)

df = df.dropna(subset=["emotion"])

# -------- Emotion grouping (27 → 7) --------
emotion_map = {
    "admiration": "love",
    "amusement": "joy",
    "anger": "anger",
    "annoyance": "anger",
    "approval": "love",
    "caring": "love",
    "confusion": "neutral",
    "curiosity": "neutral",
    "desire": "love",
    "disappointment": "sadness",
    "disapproval": "anger",
    "disgust": "anger",
    "embarrassment": "sadness",
    "excitement": "joy",
    "fear": "fear",
    "gratitude": "love",
    "grief": "sadness",
    "joy": "joy",
    "love": "love",
    "nervousness": "fear",
    "optimism": "joy",
    "pride": "joy",
    "realization": "neutral",
    "relief": "joy",
    "remorse": "sadness",
    "sadness": "sadness",
    "surprise": "surprise"
}

df["emotion"] = df["emotion"].map(emotion_map)

# remove rows not mapped
df = df.dropna(subset=["emotion"])

# keep final columns
df = df[["text", "emotion"]]

# -------- Save processed dataset --------
df.to_csv(OUTPUT_PATH, index=False)

print("Processed dataset saved to:", OUTPUT_PATH)
print("Total samples:", len(df))
print("\nEmotion distribution:")
print(df["emotion"].value_counts())