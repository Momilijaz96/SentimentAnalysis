# The script for adding a record in MongoDB.

import sys

sys.path.append("..")

from config.config import DB_CONNECTION_STRING, DB_NAME, COLLECTION_NAME, logger
from pymongo import MongoClient
from typing import Dict

def connect():
    print("DB Connection string: " + DB_CONNECTION_STRING)
    try:
        # Connect to the MongoDB server
        client = MongoClient(DB_CONNECTION_STRING)

        # Get the database you want to create the collection in
        db = client[DB_NAME]
        print("Connected successfully!!!")

        if COLLECTION_NAME not in client[DB_NAME].list_collection_names():
            print(
                "Collection does not exist..Creating new collection: " + COLLECTION_NAME
            )
            collection = db.create_collection(COLLECTION_NAME)
        else:
            print("Found collection named: " + COLLECTION_NAME)
            collection = client[DB_NAME][COLLECTION_NAME]

        return collection

    except Exception as e:
        print("Error while connecting to MongoDB", e)
        return None


def insert_doc(doc:Dict):
    """
    Function to insert record in MongoDB's collection.
    Args:
        doc(dict): {tweet:'',prediction:'',created_at:''}
    Returns:
        status(bool): Boolean to reflect if the record is inserted or not
    """
    if doc is None:
        print("Please provide a document to insert")
        return None
    elif not isinstance(doc, dict):
        print("Please provide a valid document to insert")
        return None
    elif not all(key in doc for key in ["tweet", "prediction", "created_at"]):
        print("Document to be inserted missing a key, Received: ", doc)
        return None
    
    collection = connect()
    if collection is not None:
        try:
            result = collection.insert_one(doc)

            # Get the inserted document from the collection
            inserted_tweet = collection.find_one({"_id": result.inserted_id})
            print("Inserted document: " + str(inserted_tweet))

            return result.inserted_id
        
        except Exception as e:
            print("Error while inserting document in MongoDB", e)
            return None
    else:
        print("Could'nt insert document becasue of connection error ")
        return None
