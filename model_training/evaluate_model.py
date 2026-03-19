from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="models/emotion_model"
)

print(classifier("I am extremely happy today"))
print(classifier("I feel terrible about this"))
print(classifier("I am nervous about tomorrow"))