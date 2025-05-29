user_query = """
    INSERT INTO users (
        user_id, name, email, password
    ) VALUES (%s, %s, %s, %s)
"""

session_query = """
    INSERT INTO sessions (
        session_id, user_id, jwt
    ) VALUES (%s, %s, %s)
"""

theater_query = """
    INSERT INTO theaters (
        theater_doc_id, theater_id, street1, city, state, zipcode, geo_type, latitude, longitude
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

movie_query = """
    INSERT INTO movies (
        movie_id, title, plot, fullplot, year, runtime,
        released, lastupdated, rated, languages, countries,
        poster, cast, directors, genres, type, num_mflix_comments,
        imdb_rating, imdb_votes, imdb_id,
        awards_text, awards_wins, awards_nominations,
        tomatoes_viewer_rating, tomatoes_viewer_numReviews, tomatoes_viewer_meter,
        tomatoes_critic_rating, tomatoes_critic_numReviews, tomatoes_critic_meter,
        tomatoes_lastupdated, tomatoes_fresh, tomatoes_rotten
    ) VALUES (%s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s,
              %s, %s, %s,
              %s, %s, %s,
              %s, %s, %s,
              %s, %s, %s,
              %s, %s, %s)
"""

embedded_movie_query = """
    INSERT INTO embedded_movies (
        embedded_movie_id, title, plot, fullplot, year, runtime,
        released, lastupdated, poster, cast, genres,
        languages, directors, writers, countries, type,
        num_mflix_comments, imdb_rating, imdb_votes, imdb_id,
        awards_text, awards_wins, awards_nominations, viewer_rating, viewer_reviews,
        tomatoes_production, tomatoes_lastupdated
    ) VALUES (%s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s,
              %s)
"""

comment_query = """
    INSERT INTO comments (
        comment_id, name, email, movie_id, text, date
    ) VALUES (%s, %s, %s, %s, %s, %s)
"""
