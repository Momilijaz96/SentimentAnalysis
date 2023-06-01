# Main function calls for the sentiment analysis
import sys

sys.path.append("..")  # for parent folder visibility

from .predict import predict_sentiment, load_model_ckpt
from config.config import logger, MODEL_SAVE_PATH
from typing import List


def predict_emotion(text: List[str]) -> List:
    """
    Predict sentiment of given single sentence
    Args:
        text: List of tweet text str e.g ['I am happy', 'I am sad']
    Returns:
        predictions: List of predicted emption str e.g ['happy', 'sad']
    """
    try:
        model = load_model_ckpt(MODEL_SAVE_PATH)
        logger.debug("Model loaded successfully")
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise e

    try:
        prediction = predict_sentiment(model, text)
        if not isinstance(prediction, list):
            prediction = [prediction]
        logger.debug("Prediction completed successfully")
        return prediction
    except Exception as e:
        logger.error(f"Error predicting sentiment: {e}")
        raise e

# predict_emotion(["I am happy", "I am sad"]) # Add later in PyTest
