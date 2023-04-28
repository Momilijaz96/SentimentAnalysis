# Main function calls for the sentiment analysis
import sys

sys.path.append("../SENTIMENTANALYSIS")
from sentiment_analysis.predict import predict_sentiment, load_model_ckpt
from config.config import logger, MODEL_SAVE_PATH


def predict_emotion(text: str) -> str:
    """
    Predict sentiment of given single sentence
    Args:
        text: str
    Returns:
        predictions: str
    """
    logger.info("Predicting sentiment of given text")
    model = load_model_ckpt(MODEL_SAVE_PATH)
    prediction = predict_sentiment(model, text)
    if not isinstance(prediction, list):
        prediction = [prediction]
    return prediction


# predict_emotion(["I am happy", "I am sad"])
