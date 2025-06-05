import pandas as pd
import re

def theaters_to_sentence(row):
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
