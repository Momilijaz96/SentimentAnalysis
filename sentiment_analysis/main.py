# Main function calls for the sentiment analysis
import sys

sys.path.append("../SENTIMENTANALYSIS")
from sentiment_analysis.predict import predict_sentiment, load_model_ckpt
from config.config import logger, MODEL_SAVE_PATH, REDIS_URL
from celery import Celery
from typing import List

celery_app = Celery("worker", broker=REDIS_URL)


@celery_app.task
def predict_emotion(text: List[str]) -> List:
    """
    Predict sentiment of given single sentence
    Args:
        text: List of tweet text str e.g ['I am happy', 'I am sad']
    Returns:
        predictions: List of predicted emption str e.g ['happy', 'sad']
    """
    logger.info("Predicting sentiment of given text")
    model = load_model_ckpt(MODEL_SAVE_PATH)
    prediction = predict_sentiment(model, text)
    if not isinstance(prediction, list):
        prediction = [prediction]
    return prediction


# predict_emotion(["I am happy", "I am sad"]) # Add later in PyTest
