# Declare API endpoints for interacting with model/sentiment_analysis
from fastapi import FastAPI, Request
from http import HTTPStatus
from typing import Dict
from datetime import datetime
from functools import wraps
from sentiment_analysis.main import predict_emotion
from app.schemas import PredictPayLoad
from fastapi.middleware.cors import CORSMiddleware
from mongo_db import utils as mongo_utils
from config.config import logger
import sys

sys.path.append("../SENTIMENTANALYSIS")

# Define application
app = FastAPI(
    title="Sentiment Analysis API",
    description="API for sentiment analysis model",
    version="0.0.1",
)

# Add CORS headers
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def construct_response(f):
    """Construct a JSON response for an endpoint."""

    @wraps(f)
    def wrap(request: Request, *args, **kwargs) -> Dict:
        """
        Function to wrap response of other endpoints in a JSON response.
        Args:
            request: Request
            *args: Arguments
            **kwargs: Keyword arguments
        Returns:
            response: Dict
        """
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
    Health check endpoint.
    Args:
        request: Request
    Returns:
        response: Dict
    """
    response = {
        "message": "Sentiment Analysis API is up and running",
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return response


@app.post("/predict")
@construct_response
async def predict_sentiment(request: Request, payload: PredictPayLoad) -> Dict:
    """
    Predict sentiment of the given tweet text.
    Args:
        request: Request
        payload: PredictPayLoad
    Returns:
        response: Dict
    """
    # Get text from query parameters
    texts = [item.text for item in payload.texts]
    if texts is None:
        response = {
            "message": "Please provide text to predict sentiment",
            "status-code": HTTPStatus.BAD_REQUEST,
            "data": {},
        }
        return response

    # Predict sentiment
    prediction = predict_emotion.delay(texts)

    # Store result in MongoDB
    # for text, p in zip(texts, prediction):
    #     doc = {
    #         "tweet": text,
    #         "prediction": p,
    #         "created_at": datetime.now().isoformat(),
    #     }

    #     status = mongo_utils.insert_doc(doc)
    #     if status:
    #         logger.info(f"Inserted document with id: {status}")
    #     else:
    #         logger.warning("Error while inserting document in MongoDB")

    response = {
        "message": "Sentiment prediction successful",
        "status-code": HTTPStatus.OK,
        "data": {"prediction": prediction.id},
    }
    return response
