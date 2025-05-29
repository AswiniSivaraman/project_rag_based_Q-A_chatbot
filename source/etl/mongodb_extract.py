# Get the raw data from MongoDB to Python. this is the first step in the ETL process.


# Import necessary libraries
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os


# load_dotenv(dotenv_path='../../.env')  # Load environment variables from .env file
load_dotenv()

# Get MongoDB URI and connect
db_uri = os.getenv("mongodb_uri")  # Fetch URI from environment variable
client = MongoClient(db_uri)       # Connect to MongoDB
db = client["sample_mflix"]


def fetch_multiple_collections(collection_names):
    """
    Fetch documents from multiple collections in sample_mflix in MongoDB.

    Args:
        collection_names (list): List of collection names.

    Returns:
        dict: Dictionary with collection names as keys and list of documents as values.
    """

    try:
        raw_data = {}
        for col in collection_names:
            documents = db[col].find()
            raw_data[col] = list(documents)
            print(f"{col} — {len(raw_data[col])} records fetched")
        return raw_data
    
    except Exception as e:
        print(f"Error Extracting data from MongoDB: {e}")
        return None




