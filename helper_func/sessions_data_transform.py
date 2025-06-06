# Import necessary libraries
import pandas as pd
import re

def sessions_to_sentence(row):
    """
    Transforms a single row (representing a user session document) from a DataFrame
    into a human-readable sentence.

    This function extracts session-related attributes such as the session ID,
    associated user ID, and JWT token. It constructs a descriptive sentence
    by conditionally including details only if their corresponding values are
    present (not null) in the input row. This is useful for summarizing
    session information in a textual format.

    Args:
        row (pandas.Series): A Series object representing a single session record,
                             expected to contain session-related attributes.

    Returns:
        str: A formatted sentence summarizing the session's details.
    """
    sentence = (
        (f'A session with ID "{row.get("session_id")}"' if pd.notnull(row.get("session_id")) else "") +
        (f" was initiated by user ID \"{row.get('user_id')}\"" if pd.notnull(row.get("user_id")) else "") +
        (f" and was secured using the JWT token \"{row.get('jwt')}\"" if pd.notnull(row.get("jwt")) else "") +
        "."
    )

    # Clean up extra spaces
    return re.sub(r'\s+', ' ', sentence).strip()
