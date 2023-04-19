# Declare API endpoints for interacting with model/sentiment_analysis
from fastapi import FastAPI, Request
from http import HTTPStatus
from typing import Dict
from datetime import datetime
from functools import wraps
from sentiment_analysis.main import predict_emotion


# Define application
app = FastAPI(
    title="Sentiment Analysis API",
    description="API for sentiment analysis model",
    version="0.0.1",
)


def construct_response(f):
    """Construct a JSON response for an endpoint."""

    @wraps(f)
    def wrap(request: Request, *args, **kwargs) -> Dict:
        results = f(request, *args, **kwargs)
        response = {
            "message": results["message"],
            "method": request.method,
            "status-code": results["status-code"],
            "timestamp": datetime.now().isoformat(),
            "url": request.url._url,
        }
        if "data" in results:
            response["data"] = results["data"]
        return response

    return wrap


@app.get("/")
@construct_response
def index(request: Request) -> Dict:
    """
    Health check endpoint
    """
    response = {
        "message": "Sentiment Analysis API is up and running",
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return response


@app.get("/predict")
@construct_response
def predict_sentiment(request: Request) -> Dict:
    """
    Predict sentiment of the given tweet text.
    """
    # Get text from query parameters
    text = request.query_params.get("text", None)
    if text is None:
        response = {
            "message": "Please provide text to predict sentiment",
            "status-code": HTTPStatus.BAD_REQUEST,
            "data": {},
        }
        return response
    # Predict sentiment
    prediction = predict_emotion(text)
    response = {
        "message": "Sentiment prediction successful",
        "status-code": HTTPStatus.OK,
        "data": {"prediction": prediction},
    }
    return response
