# Add data preprocessing functions

from transformers import AutoTokenizer
from config.config import logger, MODEL_SAVE_PATH


def load_tokenizer(ckpt_path: str) -> AutoTokenizer:
    """
    Function to load tokenizer.
    Args:
        ckpt_path: str
    Returns:
        tokenizer: AutoTokenizer
    """
    logger.info("Loading tokenizer from checkpoint")
    return AutoTokenizer.from_pretrained(ckpt_path)


def preprocess_data(text: str) -> dict:
    """
    Function to preprocess data.
    Args:
        text: str
    Returns:
        encodings: dict
    """
    logger.info("Preprocessing data")
    tokenizer = load_tokenizer(MODEL_SAVE_PATH)
    encodings = tokenizer(text, truncation=True, padding=True, return_tensors="pt")

    return encodings
