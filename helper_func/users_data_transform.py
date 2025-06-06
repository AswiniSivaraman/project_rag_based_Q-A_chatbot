# Import necessary libraries
import pandas as pd
import re

def users_to_sentence(row):
    """
    Transforms a single row (representing a user document) from a DataFrame
    into a human-readable sentence.

    This function extracts user-related attributes such as the user ID, name,
    email address, and password. It constructs a descriptive sentence by
    conditionally including details only if their corresponding values are
    present (not null) in the input row. This is useful for summarizing
    user information in a textual format.

    Args:
        row (pandas.Series): A Series object representing a single user record,
                             expected to contain user-related attributes.

    Returns:
        str: A formatted sentence summarizing the user's details.
    """
    sentence = (
        (f'User ID is "{row.get("user_id")}"' if pd.notnull(row.get("user_id")) else "") +
        (f" and is registered under the name \"{row.get('name')}\"" if pd.notnull(row.get("name")) else "") +
        (f" with the email address \"{row.get('email')}\"" if pd.notnull(row.get("email")) else "") +
        (f" and the account password is \"{row.get('password')}\"" if pd.notnull(row.get("password")) else "") +
        "."
    )

    return re.sub(r'\s+', ' ', sentence).strip()
