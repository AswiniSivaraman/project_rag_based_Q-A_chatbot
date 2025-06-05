import pandas as pd
import re  

def comments_to_sentence(row):

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

