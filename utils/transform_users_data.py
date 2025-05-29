#import necessary libraries
import pandas as pd


def clean_users(data):
    """
    Clean the users data by extracting relevant fields.

    Args:
        data (dict): Dictionary containing the raw users data.

    Returns:
        pd.DataFrame: Cleaned DataFrame of users.
    """
    try:

        users = pd.DataFrame(data['users'])
        users["_id"] = users["_id"].astype(str)  # Convert ObjectId to string
        users = users.rename(columns={"_id": "user_id"})  # Rename for SQL
        return users[['user_id', 'name', 'email', 'password']]
    
    except Exception as e:
        print(f"Error occurred when cleaning users data: {e}")
        return None

