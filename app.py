from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SentimentRequest(BaseModel):
    sentences: list[str]

positive_words = [
    "love", "loved", "like", "liked", "good", "great",
    "excellent", "amazing", "awesome", "happy",
    "wonderful", "fantastic", "best", "perfect",
    "nice", "enjoy", "enjoyed", "excited", "glad"
]

negative_words = [
    "hate", "hated", "bad", "terrible", "awful",
    "horrible", "sad", "angry", "worst", "poor",
    "disappointed", "failure", "failed", "problem",
    "wrong", "boring", "annoying", "unhappy"
]

def get_sentiment(sentence):
    text = sentence.lower()

    positive = sum(1 for word in positive_words if word in text)
    negative = sum(1 for word in negative_words if word in text)

    if positive > negative:
        return "happy"
    elif negative > positive:
        return "sad"
    else:
        return "neutral"

@app.post("/sentiment")
def sentiment(request: SentimentRequest):
    results = []

    for sentence in request.sentences:
        results.append({
            "sentence": sentence,
            "sentiment": get_sentiment(sentence)
        })

    return {"results": results}
