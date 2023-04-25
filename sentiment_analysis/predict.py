# Model inference utilty
from transformers import (
    AutoModelForSequenceClassification,
    DistilBertModel,
    AutoTokenizer,
)
import torch


from .data import preprocess_data
from config.config import logger, label2id, id2label

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_model_ckpt(modle_ckpt_path: str) -> DistilBertModel:
    """
    Load model from checkpoint
    Args:
        modle_ckpt_path: str
    Returns:
        model: DistilBertModel
    """
    logger.info("Loading model from checkpoint")
    return AutoModelForSequenceClassification.from_pretrained(
        modle_ckpt_path, label2id=label2id, id2label=id2label
    )


def predict_sentiment(model: DistilBertModel, text: str) -> int:
    """
    Predict sentiment of given single sentence
    Args:
        model: DistilBertModel
        text: str
        tokenizer: AutoTokenizer
    Returns:
        predictions: int
    """
    encodings = preprocess_data(text)
    outputs = model(**encodings)
    predictions = outputs.logits.argmax(-1).squeeze().tolist()
    prediction_labels = [model.config.id2label[p] for p in predictions]
    return prediction_labels
