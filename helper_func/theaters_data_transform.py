# Import necessary libraries
import pandas as pd
import re

def theaters_to_sentence(row):
    """
    Transforms a single row (representing a theater document) from a DataFrame
    into a human-readable sentence.

    This function extracts various theater-related attributes such as its ID,
    address components (street, city, state, zipcode), geolocation type,
    coordinates (latitude, longitude), and an associated document ID. It
    constructs a descriptive sentence by conditionally including details
    only if their corresponding values are present (not null) in the input row.
    This is useful for summarizing theater information in a textual format.

    Args:
        row (pandas.Series): A Series object representing a single theater record,
                             expected to contain theater-related attributes.

    Returns:
        str: A formatted sentence summarizing the theater's details.
    """
    sentence = (
        (f'Theater ID is "{row.get("theater_id")}"' if pd.notnull(row.get("theater_id")) else "") +
        (f" and it is located at " if pd.notnull(row.get("street1")) or pd.notnull(row.get("city")) or pd.notnull(row.get("state")) or pd.notnull(row.get("zipcode")) else "") +
        (f"{row.get('street1')}, " if pd.notnull(row.get("street1")) else "") +
        (f"{row.get('city')}, " if pd.notnull(row.get("city")) else "") +
        (f"{row.get('state')}, " if pd.notnull(row.get("state")) else "") +
        (f"{row.get('zipcode')}" if pd.notnull(row.get("zipcode")) else "") +
        (f". The geolocation type is \"{row.get('geo_type')}\"" if pd.notnull(row.get("geo_type")) else "") +
        (f" with coordinates ({row.get('latitude')}, {row.get('longitude')})" if pd.notnull(row.get("latitude")) and pd.notnull(row.get("longitude")) else "") +
        (f". The document ID associated with this theater is \"{row.get('theater_doc_id')}\"" if pd.notnull(row.get("theater_doc_id")) else "") +
        "."
    )

    return re.sub(r'\s+', ' ', sentence).strip()
