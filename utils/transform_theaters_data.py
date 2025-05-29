#import necessary libraries
import pandas as pd


def clean_theaters(data):
    """
    Clean the theaters data by flattening nested address and geo fields.

    Args:
        data (dict): Dictionary containing the raw theaters data.

    Returns:
        pd.DataFrame: Cleaned DataFrame of theaters.
    """

    try:

        theaters = pd.DataFrame(data['theaters'])
        theaters["_id"] = theaters["_id"].astype(str)  # Convert ObjectId to string
        theaters = theaters.rename(columns={"_id": "theater_doc_id"})  

        # Rename and flatten fields
        theaters["theater_id"] = theaters["theaterId"]  
        theaters["street1"] = theaters["location"].apply(lambda x: x['address'].get('street1') if x else None)
        theaters["city"] = theaters["location"].apply(lambda x: x['address'].get('city') if x else None)
        theaters["state"] = theaters["location"].apply(lambda x: x['address'].get('state') if x else None)
        theaters["zipcode"] = theaters["location"].apply(lambda x: x['address'].get('zipcode') if x else None)
        theaters["geo_type"] = theaters["location"].apply(lambda x: x['geo'].get('type') if x else None)
        theaters["latitude"] = theaters["location"].apply(lambda x: x['geo']['coordinates'][1] if x else None)
        theaters["longitude"] = theaters["location"].apply(lambda x: x['geo']['coordinates'][0] if x else None)

        return theaters[['theater_doc_id','theater_id', 'street1', 'city', 'state', 'zipcode', 'geo_type', 'latitude', 'longitude']]

    except Exception as e:
        print(f"Error occurred when cleaning theaters data: {e}")
        return None
