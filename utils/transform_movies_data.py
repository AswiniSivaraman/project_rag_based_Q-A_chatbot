#import necessary libraries
import pandas as pd


def clean_movies(data):

    """
    Clean the movies data by flattening nested structures and keeping necessary fields.

    Args:
        data (dict): Dictionary containing raw MongoDB data.

    Returns:
        pd.DataFrame: Cleaned DataFrame of movies.
    """

    try:

        movies = pd.DataFrame(data['movies'])
        movies['_id'] = movies['_id'].astype(str) # Convert ObjectId to string
        movies['released'] = pd.to_datetime(movies['released'], errors='coerce')  # Fix malformed dates
        movies['lastupdated'] = pd.to_datetime(movies['lastupdated'], errors='coerce')  # Fix malformed dates 

        # Convert list fields to comma-separated strings
        list_fields = ['cast', 'genres', 'languages', 'directors', 'countries']
        for field in list_fields:
            movies[field] = movies[field].apply(lambda x: ", ".join(x) if isinstance(x, list) else None)


        # Flatten nested dictionaries and lists ( imbd, awards, tomatoes )
        movies['imdb_rating'] = movies['imdb'].apply(lambda x: x.get('rating') if isinstance(x, dict) else None)
        movies['imdb_votes'] = movies['imdb'].apply(lambda x: x.get('votes') if isinstance(x, dict) else None)
        movies['imdb_id'] = movies['imdb'].apply(lambda x: x.get('id') if isinstance(x, dict) else None)
        
        # Force imdb_rating to numeric (float), set errors to NaN
        movies['imdb_rating'] = pd.to_numeric(movies['imdb_rating'], errors='coerce')
        movies['imdb_votes'] = pd.to_numeric(movies['imdb_votes'], errors='coerce')
        movies['imdb_id'] = pd.to_numeric(movies['imdb_id'], errors='coerce')

        
        movies['awards_text'] = movies['awards'].apply(lambda x: x.get('text') if isinstance(x, dict) else None)   
        movies['awards_wins'] = movies['awards'].apply(lambda x: x.get('wins') if isinstance(x, dict) else None)
        movies['awards_nominations'] = movies['awards'].apply(lambda x: x.get('nominations') if isinstance(x, dict) else None)

        movies['tomatoes_viewer_rating'] = movies['tomatoes'].apply(lambda x: x.get('viewer', {}).get('rating') if isinstance(x, dict) else None)
        movies['tomatoes_viewer_numReviews'] = movies['tomatoes'].apply(lambda x: x.get('viewer', {}).get('numReviews') if isinstance(x, dict) else None)
        movies['tomatoes_viewer_meter'] = movies['tomatoes'].apply(lambda x: x.get('viewer', {}).get('meter') if isinstance(x, dict) else None)
        movies['tomatoes_critic_rating'] = movies['tomatoes'].apply(lambda x: x.get('critic', {}).get('rating') if isinstance(x, dict) else None)
        movies['tomatoes_critic_numReviews'] = movies['tomatoes'].apply(lambda x: x.get('critic', {}).get('numReviews') if isinstance(x, dict) else None)
        movies['tomatoes_critic_meter'] = movies['tomatoes'].apply(lambda x: x.get('critic', {}).get('meter') if isinstance(x, dict) else None)
        # movies['tomatoes_production'] = movies['tomatoes'].apply(lambda x: x.get('production') if isinstance(x, dict) else None)
        movies['tomatoes_lastupdated'] = pd.to_datetime(
            movies['tomatoes'].apply(lambda x: x.get('lastUpdated') if isinstance(x, dict) else None),
            errors='coerce'
        )
        movies['tomatoes_fresh'] = movies['tomatoes'].apply(lambda x: x.get('fresh') if isinstance(x, dict) else None)
        movies['tomatoes_rotten'] = movies['tomatoes'].apply(lambda x: x.get('rotten') if isinstance(x, dict) else None)

        movies = movies.rename(columns={'_id': 'movie_id'})  # Rename ID for SQL

        movies = movies.where(pd.notnull(movies), None)
        movies = movies.replace({pd.NA: None, float('nan'): None, 'nan': None})

        return movies[['movie_id', 'title', 'plot', 'fullplot', 'year', 'runtime',
                    'released', 'lastupdated', 'rated', 'languages', 'countries',
                    'poster', 'cast', 'directors', 'genres', 'type', 'num_mflix_comments',
                    'imdb_rating', 'imdb_votes', 'imdb_id',
                    'awards_text', 'awards_wins', 'awards_nominations',
                    'tomatoes_viewer_rating', 'tomatoes_viewer_numReviews', 'tomatoes_viewer_meter',
                    'tomatoes_critic_rating', 'tomatoes_critic_numReviews', 'tomatoes_critic_meter',
                    'tomatoes_lastupdated', 'tomatoes_fresh', 'tomatoes_rotten']]
    
    except Exception as e:
        print(f"Error occurred when cleaning movies data: {e}")
        return None

