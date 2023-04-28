# The script for adding a record in MongoDB.


import sys

sys.path.append("../SENTIMENTANALYSIS")

from config.config import DB_CONNECTION_STRING, DB_NAME
import time
from pymongo import MongoClient


def connect():
    # Connect to the MongoDB server
    client = MongoClient(DB_CONNECTION_STRING)

    # Get the database you want to create the collection in
    db = client[DB_NAME]

    # Create a new collection called 'tweets'
    collection = db.create_collection("tweets")

    return collection


def insert_doc(doc):
    """
    Function to insert record in MongoDB's collection.
    Args:
        doc(dict): {tweet:'',prediction:'',created_at:''}
    Returns:
        status(bool): Boolean to reflect if the record is inserted or not
    """

    collection = connect()

    result = collection.insert_one(doc)

    # Get the inserted document from the collection
    inserted_tweet = collection.find_one({"_id": result.inserted_id})

    # Print the inserted document
    print(inserted_tweet)

    return result.inserted_id
