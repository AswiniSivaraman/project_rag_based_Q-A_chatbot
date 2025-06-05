import pandas as pd
import re

def embedded_movies_to_sentence(row):
    sentence = (
        (f"The movie is titled \"{row.get('title')}\"" if pd.notnull(row.get('title')) else "") +
        (f" and is a {row.get('genres')} {row.get('type')}" if pd.notnull(row.get('genres')) and pd.notnull(row.get('type')) else "") +
        (f" that was released in {row.get('year')}" if pd.notnull(row.get('year')) else "") +
        (f" with an official release date of {row.get('released')}" if pd.notnull(row.get('released')) else "") +
        (f". It was directed by {row.get('directors')}" if pd.notnull(row.get('directors')) else "") +
        (f", written by {row.get('writers')}" if pd.notnull(row.get('writers')) else "") +
        (f", and stars {row.get('cast')}" if pd.notnull(row.get('cast')) else "") +
        (f". The runtime is {row.get('runtime')} minutes" if pd.notnull(row.get('runtime')) else "") +
        (f". The plot goes like this - \"{row.get('plot')}\"" if pd.notnull(row.get('plot')) else "") +
        (f" and the full story is \"{row.get('fullplot')}\"" if pd.notnull(row.get('fullplot')) else "") +
        (f". It is available in {row.get('languages')}" if pd.notnull(row.get('languages')) else "") +
        (f" and was produced in {row.get('countries')}" if pd.notnull(row.get('countries')) else "") +
        (f". It is rated '{row.get('rated')}'" if pd.notnull(row.get('rated')) else "") +
        (f" with an IMDb rating of {row.get('imdb_rating')}" if pd.notnull(row.get('imdb_rating')) else "") +
        (f" based on {row.get('imdb_votes')} votes" if pd.notnull(row.get('imdb_votes')) else "") +
        (f" and has the IMDb ID {row.get('imdb_id')}" if pd.notnull(row.get('imdb_id')) else "") +
        (f". The average viewer rating is {row.get('viewer_rating')}" if pd.notnull(row.get('viewer_rating')) else "") +
        (f" based on {row.get('viewer_reviews')} viewer reviews" if pd.notnull(row.get('viewer_reviews')) else "") +
        (f". Awards received include {row.get('awards_text')}" if pd.notnull(row.get('awards_text')) else "") +
        (f". The Rotten Tomatoes production information reads {row.get('tomatoes_production')}" if pd.notnull(row.get('tomatoes_production')) else "") +
        (f" and was last updated on {row.get('tomatoes_lastupdated')}" if pd.notnull(row.get('tomatoes_lastupdated')) else "") +
        (f". The official poster is available at {row.get('poster')}" if pd.notnull(row.get('poster')) else "") +
        (f". The internal movie ID is {row.get('embedded_movie_id')}" if pd.notnull(row.get('embedded_movie_id')) else "") +
        (f". This record was last updated on {row.get('lastupdated')}" if pd.notnull(row.get('lastupdated')) else "") +
        "."
    )

    # Remove multiple spaces and strip leading/trailing ones
    sentence = re.sub(r'\s+', ' ', sentence).strip()

    return sentence
