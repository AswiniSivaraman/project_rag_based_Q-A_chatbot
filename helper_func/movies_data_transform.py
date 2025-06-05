import pandas as pd
import re

def movies_to_sentence(row):
    sentence = (
        (f"The movie is titled \"{row.get('title')}\"" if pd.notnull(row.get('title')) else "") +
        (f" and is a {row.get('genres')} {row.get('type')}" if pd.notnull(row.get('genres')) and pd.notnull(row.get('type')) else "") +
        (f" that was released in {row.get('year')}" if pd.notnull(row.get('year')) else "") +
        (f" with an official release date of {row.get('released')}" if pd.notnull(row.get('released')) else "") +
        (f". It has a runtime of {row.get('runtime')} minutes" if pd.notnull(row.get('runtime')) else "") +
        (f" and is rated \"{row.get('rated')}\"" if pd.notnull(row.get('rated')) else "") +
        (f". The plot reads \"{row.get('plot')}\"" if pd.notnull(row.get('plot')) else "") +
        (f" and the full story is \"{row.get('fullplot')}\"" if pd.notnull(row.get('fullplot')) else "") +
        (f". It was directed by {row.get('directors')}" if pd.notnull(row.get('directors')) else "") +
        (f" and features the cast {row.get('cast')}" if pd.notnull(row.get('cast')) else "") +
        (f". The movie is available in {row.get('languages')}" if pd.notnull(row.get('languages')) else "") +
        (f" and was produced in {row.get('countries')}" if pd.notnull(row.get('countries')) else "") +
        (f". It holds an IMDb rating of {row.get('imdb_rating')}" if pd.notnull(row.get('imdb_rating')) else "") +
        (f" based on {row.get('imdb_votes')} votes" if pd.notnull(row.get('imdb_votes')) else "") +
        (f", with the IMDb ID being {row.get('imdb_id')}" if pd.notnull(row.get('imdb_id')) else "") +
        (f". Awards received include {row.get('awards_text')}" if pd.notnull(row.get('awards_text')) else "") +
        (f". The movie has {row.get('num_mflix_comments')} comments on MFlix" if pd.notnull(row.get('num_mflix_comments')) else "") +
        (f". Rotten Tomatoes viewer rating is {row.get('tomatoes_viewer_rating')}" if pd.notnull(row.get('tomatoes_viewer_rating')) else "") +
        (f" based on {row.get('tomatoes_viewer_numReviews')} reviews" if pd.notnull(row.get('tomatoes_viewer_numReviews')) else "") +
        (f", with a viewer score of {row.get('tomatoes_viewer_meter')}%" if pd.notnull(row.get('tomatoes_viewer_meter')) else "") +
        (f". Critic rating on Rotten Tomatoes is {row.get('tomatoes_critic_rating')}" if pd.notnull(row.get('tomatoes_critic_rating')) else "") +
        (f" from {row.get('tomatoes_critic_numReviews')} critic reviews" if pd.notnull(row.get('tomatoes_critic_numReviews')) else "") +
        (f", with a critic score of {row.get('tomatoes_critic_meter')}%" if pd.notnull(row.get('tomatoes_critic_meter')) else "") +
        (f". It received {row.get('tomatoes_fresh')} fresh reviews" if pd.notnull(row.get('tomatoes_fresh')) else "") +
        (f" and {row.get('tomatoes_rotten')} rotten reviews" if pd.notnull(row.get('tomatoes_rotten')) else "") +
        (f". The poster can be found at {row.get('poster')}" if pd.notnull(row.get('poster')) else "") +
        (f". Rotten Tomatoes data was last updated on {row.get('tomatoes_lastupdated')}" if pd.notnull(row.get('tomatoes_lastupdated')) else "") +
        (f", and the overall database entry was last updated on {row.get('lastupdated')}" if pd.notnull(row.get('lastupdated')) else "") +
        (f". The internal movie ID used is {row.get('movie_id')}" if pd.notnull(row.get('movie_id')) else "") +
        "."
    )

    # Clean extra spaces
    return re.sub(r'\s+', ' ', sentence).strip()
