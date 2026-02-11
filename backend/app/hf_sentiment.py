import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")

HF_URL = (
    "https://router.huggingface.co/"
    "hf-inference/models/cardiffnlp/"
    "twitter-roberta-base-sentiment-latest"
)

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def analyze_sentiment(text: str):
    if not HF_API_KEY:
        return "NEUTRAL", 0.0

    try:
        response = requests.post(
            HF_URL,
            headers=HEADERS,
            json={"inputs": text},
            timeout=10
        )

        if response.status_code != 200:
            return "NEUTRAL", 0.0

        if not response.headers.get("content-type", "").startswith("application/json"):
            return "NEUTRAL", 0.0

        data = response.json()

        if isinstance(data, dict) and data.get("error"):
            return "NEUTRAL", 0.0

        if isinstance(data, list) and data:
            top = data[0][0]
            label = top.get("label", "NEUTRAL").upper()
            score = round(float(top.get("score", 0.0)), 4)

            sentiment = "POSITIVE" if label == "POSITIVE" else "NEGATIVE"
            return sentiment, score

        return "NEUTRAL", 0.0

    except Exception:
        return "NEUTRAL", 0.0
