def create_table_users(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id VARCHAR(255) PRIMARY KEY,
        name TEXT,
        email VARCHAR(255),
        password TEXT
    );
    """)

def create_table_sessions(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        session_id VARCHAR(255) PRIMARY KEY,
        user_id VARCHAR(255),
        jwt TEXT
    );
    """)

def create_table_theaters(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS theaters (
        theater_doc_id VARCHAR(255) PRIMARY KEY,
        theater_id INT,
        street1 TEXT,
        city TEXT,
        state TEXT,
        zipcode TEXT,
        geo_type TEXT,
        latitude DOUBLE,
        longitude DOUBLE
    );
    """)

def create_table_movies(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        movie_id VARCHAR(255) PRIMARY KEY,
        title TEXT,
        plot TEXT,
        fullplot TEXT,
        year VARCHAR(10),
        runtime INT,
        released DATE,
        lastupdated TIMESTAMP,
        rated TEXT,
        languages TEXT,
        countries TEXT,
        poster TEXT,
        cast TEXT,
        directors TEXT,
        genres TEXT,
        type TEXT,
        num_mflix_comments INT,
        imdb_rating DOUBLE,
        imdb_votes INT,
        imdb_id INT,
        awards_text TEXT,
        awards_wins INT,
        awards_nominations INT,
        tomatoes_viewer_rating DOUBLE,
        tomatoes_viewer_numReviews INT,
        tomatoes_viewer_meter INT,
        tomatoes_critic_rating DOUBLE,
        tomatoes_critic_numReviews INT,
        tomatoes_critic_meter INT,
        tomatoes_lastupdated TIMESTAMP,
        tomatoes_fresh INT,
        tomatoes_rotten INT
    );
    """)

def create_table_embedded_movies(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS embedded_movies (
        embedded_movie_id VARCHAR(255) PRIMARY KEY,
        title TEXT,
        plot TEXT,
        fullplot TEXT,
        year VARCHAR(10),
        runtime INT,
        released DATE,
        lastupdated TIMESTAMP,
        poster TEXT,
        cast TEXT,
        genres TEXT,
        languages TEXT,
        directors TEXT,
        writers TEXT,
        countries TEXT,
        type TEXT,
        num_mflix_comments INT,
        imdb_rating VARCHAR(255),
        imdb_votes INT,
        imdb_id INT,
        awards_text TEXT,
        awards_wins INT,
        awards_nominations INT,
        viewer_rating DOUBLE,
        viewer_reviews INT,
        tomatoes_production TEXT,
        tomatoes_lastupdated TIMESTAMP
    );
    """)

def create_table_comments(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comments (
        comment_id VARCHAR(255) PRIMARY KEY,
        name TEXT,
        email VARCHAR(255),
        movie_id VARCHAR(255),
        text TEXT,
        date DATE
    );
    """)
