# Model inference utilty

from transformers import AutoModel, DistilBertModel


def load_ckpt(modle_ckpt_path: str) -> DistilBertModel:
    """
    Load model from checkpoint
    Args:
    Returns:
    """
    return AutoModel.from_pretrained(modle_ckpt_path)


def predict(model: DistilBertModel, text: str) -> int:
    """
    Predict sentiment of text
    Args:
    Returns:
    """
    return 1
