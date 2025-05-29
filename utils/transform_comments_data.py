#import necessary libraries
import pandas as pd



def clean_comments(data):
    """
    Clean the comments data by converting ObjectIds, fixing dates,
    filtering by valid movie_ids, and removing duplicates.

    Args:
        data (dict): Dictionary containing the raw MongoDB data.

    Returns:
        pd.DataFrame: Cleaned DataFrame of comments.
    """

    try:
        comments = pd.DataFrame(data['comments'])
        comments["_id"] = comments["_id"].astype(str)
        comments["movie_id"] = comments["movie_id"].astype(str)
        comments["date"] = pd.to_datetime(comments["date"], errors='coerce').dt.date
        comments = comments.rename(columns={"_id": "comment_id"})
        comments = comments.drop_duplicates(subset=['text', 'email'])

        # Filter by valid movie_ids to avoid foreign key issues
        valid_movie_ids = pd.DataFrame(data['movies'])['_id'].astype(str).tolist()
        comments = comments[comments['movie_id'].isin(valid_movie_ids)]

        return comments[['comment_id', 'name', 'email', 'movie_id', 'text', 'date']]
    
    except Exception as e:
        print(f"Error occurred when cleaning comments data: {e}")
        return None
