# Evaluation of the model
from sklearn.metrics import accuracy_score, f1_score
from typing import Dict


def compute_metrics(pred: Dict) -> Dict:
    """
    Function to compute the accuracy and f1 score of the model
    Args:
        pred: Dictionary containing the predictions and labels
    Returns:
        Dictionary containing the accuracy and f1 score
    """
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    f1 = f1_score(labels, preds, average="weighted")
    acc = accuracy_score(labels, preds)
    return {"accuracy": acc, "f1": f1}
