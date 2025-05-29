#import necessary libraries
import pandas as pd


def clean_embedded_movies(data):
    """
    Clean the embedded_movies data by flattening nested fields and transforming list data.

    Args:
        data (dict): Dictionary containing the raw embedded_movies data.

    Returns:
        pd.DataFrame: Cleaned DataFrame of embedded movies.
    """

    try:
        embedded_movies = pd.DataFrame(data['embedded_movies'])

        # Convert ObjectId to string
        embedded_movies['_id'] = embedded_movies['_id'].astype(str)
        embedded_movies = embedded_movies.rename(columns={'_id': 'embedded_movie_id'})

        # Convert date fields
        embedded_movies['released'] = pd.to_datetime(embedded_movies['released'], errors='coerce')
        embedded_movies['lastupdated'] = pd.to_datetime(embedded_movies['lastupdated'], errors='coerce')
        embedded_movies['tomatoes_lastupdated'] = pd.to_datetime(
            embedded_movies['tomatoes'].apply(lambda x: x.get('lastUpdated') if isinstance(x, dict) else None),
            errors='coerce'
        )

        # Flatten imdb fields
        embedded_movies['imdb_rating'] = embedded_movies['imdb'].apply(lambda x: x.get('rating') if isinstance(x, dict) else None)
        embedded_movies['imdb_votes'] = embedded_movies['imdb'].apply(lambda x: x.get('votes') if isinstance(x, dict) else None)
        embedded_movies['imdb_id'] = embedded_movies['imdb'].apply(lambda x: x.get('id') if isinstance(x, dict) else None)

        # Force imdb_rating to numeric (float), set errors to NaN
        embedded_movies['imdb_rating'] = pd.to_numeric(embedded_movies['imdb_rating'], errors='coerce')
        embedded_movies['imdb_votes'] = pd.to_numeric(embedded_movies['imdb_votes'], errors='coerce')
        embedded_movies['imdb_id'] = pd.to_numeric(embedded_movies['imdb_id'], errors='coerce')

        # Flatten awards
        embedded_movies['awards_text'] = embedded_movies['awards'].apply(lambda x: x.get('text') if isinstance(x, dict) else None)
        embedded_movies['awards_wins'] = embedded_movies['awards'].apply(lambda x: x.get('wins') if isinstance(x, dict) else None)
        embedded_movies['awards_nominations'] = embedded_movies['awards'].apply(lambda x: x.get('nominations') if isinstance(x, dict) else None)

        # Flatten tomatoes (only available fields)
        embedded_movies['viewer_rating'] = embedded_movies['tomatoes'].apply(lambda x: x.get('viewer', {}).get('rating') if isinstance(x, dict) else None)
        embedded_movies['viewer_reviews'] = embedded_movies['tomatoes'].apply(lambda x: x.get('viewer', {}).get('numReviews') if isinstance(x, dict) else None)
        embedded_movies['tomatoes_production'] = embedded_movies['tomatoes'].apply(lambda x: x.get('production') if isinstance(x, dict) else None)

        # Join list fields to comma-separated strings
        list_fields = ['cast', 'genres', 'languages', 'directors', 'writers', 'countries']
        for field in list_fields:
            embedded_movies[field] = embedded_movies[field].apply(lambda x: ", ".join(x) if isinstance(x, list) else None)

        embedded_movies['plot_embedding'] = embedded_movies['plot_embedding'].apply(
            lambda x: ', '.join(map(str, x)) if isinstance(x, list) else x
        )
        embedded_movies = embedded_movies.where(pd.notnull(embedded_movies), None)
        embedded_movies = embedded_movies.replace({pd.NA: None, float('nan'): None, 'nan': None})


        return embedded_movies[['embedded_movie_id', 'title', 'plot', 'fullplot', 'year', 'runtime',
                                'released', 'lastupdated', 'poster', 'cast', 'genres',
                                'languages', 'directors', 'writers', 'countries', 'type',
                                'num_mflix_comments', 
                                'imdb_rating', 'imdb_votes', 'imdb_id',
                                'awards_text', 'awards_wins', 'awards_nominations',
                                'viewer_rating', 'viewer_reviews',
                                'tomatoes_production', 'tomatoes_lastupdated']]
    
    except Exception as e:
        print(f"Error occured when cleaning embedded movies data: {e}")
        return None


