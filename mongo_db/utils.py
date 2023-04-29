# The script for adding a record in MongoDB.


import sys

sys.path.append("../SENTIMENTANALYSIS")

from config.config import DB_CONNECTION_STRING, DB_NAME, COLLECTION_NAME, logger
import time
from pymongo import MongoClient


def connect():
    try:
        # Connect to the MongoDB server
        logger.info("DB Connection string: " + DB_CONNECTION_STRING)
        client = MongoClient(DB_CONNECTION_STRING)
        logger.info("Connected successfully!!!")
        # Get the database you want to create the collection in
        db = client[DB_NAME]
        if COLLECTION_NAME not in client[DB_NAME].list_collection_names():
            logger.info("Collection does not exist")
            collection = db.create_collection(COLLECTION_NAME)
        else:
            logger.error("Collection exists")
            collection = client[DB_NAME][COLLECTION_NAME]

        return collection

    except Exception as e:
        print("Error while connecting to MongoDB", e)
        return None


def insert_doc(doc):
    """
    Function to insert record in MongoDB's collection.
    Args:
        doc(dict): {tweet:'',prediction:'',created_at:''}
    Returns:
        status(bool): Boolean to reflect if the record is inserted or not
    """

    collection = connect()
    if collection is not None:
        result = collection.insert_one(doc)

        # Get the inserted document from the collection
        inserted_tweet = collection.find_one({"_id": result.inserted_id})
        logger.info("Inserted document: " + str(inserted_tweet))

        return result.inserted_id
    else:
        return None
