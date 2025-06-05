import pandas as pd
import re

def users_to_sentence(row):
    sentence = (
        (f'User ID is "{row.get("user_id")}"' if pd.notnull(row.get("user_id")) else "") +
        (f" and is registered under the name \"{row.get('name')}\"" if pd.notnull(row.get("name")) else "") +
        (f" with the email address \"{row.get('email')}\"" if pd.notnull(row.get("email")) else "") +
        (f" and the account password is \"{row.get('password')}\"" if pd.notnull(row.get("password")) else "") +
        "."
    )

    return re.sub(r'\s+', ' ', sentence).strip()
