from typing import List
from fastapi import Query
from pydantic import BaseModel


class TweetText(BaseModel):
    text: str = Query(None, min_length=1, max_length=280)


class PredictPayLoad(BaseModel):
    texts: List[TweetText]
