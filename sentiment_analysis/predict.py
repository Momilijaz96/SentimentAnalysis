# Model inference utilty
from transformers import AutoModel, DistilBertModel, AutoTokenizer
import torch


from data import preprocess_data
from config.config import logger, label2id, id2label

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def load_model_ckpt(modle_ckpt_path: str) -> DistilBertModel:
    """
    Load model from checkpoint
    Args:
    Returns:
    """
    logger.info("Loading model from checkpoint")
    return AutoModel.from_pretrained(
        modle_ckpt_path, label2id=label2id, id2label=id2label
    )


def predict(model: DistilBertModel, text: str) -> int:
    """
    Predict sentiment of given single sentence
    Args:
        model: DistilBertModel
        text: str
        tokenizer: AutoTokenizer
    Returns:
        predictions: int
    """
    logger.info("Predicting sentiment of given text")
    encodings = preprocess_data(text)
    outputs = model(**encodings)
    prediction = outputs.logits.argmax(-1).squeeze().tolist()
    prediction_label = model.config.id2label[prediction]
    return prediction_label
