import pandas as pd
import re

def sessions_to_sentence(row):
    sentence = (
        (f'A session with ID "{row.get("session_id")}"' if pd.notnull(row.get("session_id")) else "") +
        (f" was initiated by user ID \"{row.get('user_id')}\"" if pd.notnull(row.get("user_id")) else "") +
        (f" and was secured using the JWT token \"{row.get('jwt')}\"" if pd.notnull(row.get("jwt")) else "") +
        "."
    )

    # Clean up extra spaces
    return re.sub(r'\s+', ' ', sentence).strip()
