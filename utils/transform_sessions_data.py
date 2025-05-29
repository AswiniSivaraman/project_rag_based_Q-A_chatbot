#import necessary libraries
import pandas as pd


def clean_sessions(data):
    """
    Clean the sessions data by converting ObjectId to string and extracting necessary fields.

    Args:
        data (dict): Dictionary containing raw MongoDB data.

    Returns:
        pd.DataFrame: Cleaned DataFrame of sessions.
    """

    try:

        sessions = pd.DataFrame(data['sessions'])
        sessions['_id'] = sessions['_id'].astype(str)  # Convert ObjectId to string
        sessions['user_id'] = sessions['user_id'].astype(str)  # Ensure user_id is string
        sessions = sessions.rename(columns={'_id': 'session_id'})  # Rename ID for SQL
        return sessions[['session_id', 'user_id', 'jwt']]

    except Exception as e:
        print(f"Error occurred when cleaning sessions data: {e}")
        return None