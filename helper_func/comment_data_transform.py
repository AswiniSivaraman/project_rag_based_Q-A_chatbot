# Import necessary libraries
import pandas as pd
import re  

def comments_to_sentence(row):
    """
    Transforms a single row (representing a comment document) from a DataFrame
    into a human-readable sentence.

    This function extracts relevant fields from the input row, such as name,
    email, movie ID, comment text, and date, and constructs a descriptive
    sentence about the comment. It gracefully handles missing or null values
    for optional fields by omitting them from the generated sentence.

    Args:
        row (pandas.Series): A Series object representing a single row from
                             a DataFrame, expected to contain comment-related
                             fields.

    Returns:
        str: A formatted sentence describing the comment.
    """

    name = row.get("name", "Someone")
    email = row.get("email")
    movie_id = row.get("movie_id")
    comment_text = row.get("text", "")
    date = row.get("date")

    sentence = (
        f"{name} shared a comment" +
        (f" saying \"{comment_text}\"" if pd.notnull(comment_text) else "") +
        (f" about the movie with ID {movie_id}" if pd.notnull(movie_id) else "") +
        (f" on {date}" if pd.notnull(date) else "") +
        (f" using the email ID {email}" if pd.notnull(email) else "") +
        "."
    )

    # Remove multiple spaces and strip leading/trailing ones
    sentence = re.sub(r'\s+', ' ', sentence).strip()

    return sentence

