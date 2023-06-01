# Add data preprocessing functions

from transformers import AutoTokenizer
from config.config import  MODEL_SAVE_PATH
from typing import Dict


def load_tokenizer(ckpt_path: str) -> AutoTokenizer:
    """
    Function to load tokenizer.
    Args:
        ckpt_path: str
    Returns:
        tokenizer: AutoTokenizer
    """
    return AutoTokenizer.from_pretrained(ckpt_path)


def preprocess_data(text: str) -> Dict:
    """
    Function to preprocess data.
    Args:
        text: str
    Returns:
        encodings: dict
    """
    tokenizer = load_tokenizer(MODEL_SAVE_PATH)
    encodings = tokenizer(text, truncation=True, padding=True, return_tensors="pt")

    return encodings
