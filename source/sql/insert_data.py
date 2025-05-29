from source.sql.create_connection import connection
from source.sql.insert_query import (
    user_query, session_query, theater_query, movie_query,
    embedded_movie_query, comment_query
)
from source.sql.insert_data_in_table import insert_data_to_table


def insert_users(conn, data):
    insert_data_to_table(conn, user_query, data)

def insert_sessions(conn, data):
    insert_data_to_table(conn, session_query, data)

def insert_theaters(conn, data):
    insert_data_to_table(conn, theater_query, data)

def insert_movies(conn, data):
    insert_data_to_table(conn, movie_query, data)

def insert_embedded_movies(conn, data):
    insert_data_to_table(conn, embedded_movie_query, data)

def insert_comments(conn, data):
    insert_data_to_table(conn, comment_query, data)

def insert_all_data(cleaned_data):
    conn = connection()
    if conn is None:
        print("Connection failed. Cannot insert data.")
        return

    try:
        if "users" in cleaned_data and not cleaned_data["users"].empty:
            print("Inserting users...")
            insert_users(conn, cleaned_data["users"].values.tolist())

        if "sessions" in cleaned_data and not cleaned_data["sessions"].empty:
            print("Inserting sessions...")
            insert_sessions(conn, cleaned_data["sessions"].values.tolist())

        if "theaters" in cleaned_data and not cleaned_data["theaters"].empty:
            print("Inserting theaters...")
            insert_theaters(conn, cleaned_data["theaters"].values.tolist())

        if "movies" in cleaned_data and not cleaned_data["movies"].empty:
            print("Inserting movies...")
            insert_movies(conn, cleaned_data["movies"].values.tolist())

        if "embedded_movies" in cleaned_data and not cleaned_data["embedded_movies"].empty:
            print("Inserting embedded movies...")
            insert_embedded_movies(conn, cleaned_data["embedded_movies"].values.tolist())

        if "comments" in cleaned_data and not cleaned_data["comments"].empty:
            print("Inserting comments...")
            insert_comments(conn, cleaned_data["comments"].values.tolist())

        print("✅ All data inserted successfully.")
    
    except Exception as e:
        print("❌ Error during data insertion:", e)
        conn.rollback()
    
    finally:
        conn.close()

