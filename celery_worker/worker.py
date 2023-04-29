import sys

sys.path.append("../SENTIMENTANALYSIS")

from config.config import REDIS_URL
from sentiment_analysis.main import predict_emotion
from celery import Celery

app = Celery("worker", broker=REDIS_URL, backend=REDIS_URL)


@app.task
def predict(text: str):
    print("Celery worker received: ", text)
    return predict_emotion(text)
