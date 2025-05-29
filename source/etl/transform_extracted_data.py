from utils.transform_comments_data import clean_comments
from utils.transform_embedded_movies_data import clean_embedded_movies
from utils.transform_movies_data import clean_movies
from utils.transform_sessions_data import clean_sessions
from utils.transform_theaters_data import clean_theaters
from utils.transform_users_data import clean_users


def clean_extracted_data(raw_data):
    """
    Apply all cleaning functions to the extracted MongoDB data and return them as a dictionary.

    Args:
        raw_data (dict): Dictionary where keys are collection names and values are lists of documents.

    Returns:
        dict: Dictionary of cleaned DataFrames with keys matching collection names.
    """
    
    try:
        return {
            "comments": clean_comments(raw_data),
            "embedded_movies": clean_embedded_movies(raw_data),
            "movies": clean_movies(raw_data),
            "sessions": clean_sessions(raw_data),
            "theaters": clean_theaters(raw_data),
            "users": clean_users(raw_data)
        }
    
    except Exception as e:
        print(f"Error cleaning extracted data: {e}")
        return None