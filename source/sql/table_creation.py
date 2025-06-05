from source.sql.create_connection import connection
from source.sql.table_query import (
    create_table_users,
    create_table_sessions,
    create_table_theaters,
    create_table_movies,
    create_table_embedded_movies,
    create_table_comments
)
from source.sql.drop_query import (
    drop_table_users,
    drop_table_comments,
    drop_table_embedded_movies,
    drop_table_movies,
    drop_table_sessions,
    drop_table_theaters
)

def create_all_tables():
    """
    Drops existing tables if they exist, then creates all necessary tables
    in the MySQL database using the definitions from table_query.py.
    """
    conn = connection()
    if conn is None:
        print("Connection failed. Cannot create tables.")
        return

    cursor = conn.cursor()

    try:

        print("\n--- Dropping existing tables ---")
        drop_table_comments(cursor)
        drop_table_embedded_movies(cursor)
        drop_table_movies(cursor)
        drop_table_sessions(cursor)
        drop_table_theaters(cursor)
        drop_table_users(cursor)
        print("All existing tables dropped.\n")

        print("--- Creating new tables ---")
        print("Creating users table...")
        create_table_users(cursor)
        print("Creating sessions table...")
        create_table_sessions(cursor)
        print("Creating theaters table...")
        create_table_theaters(cursor)
        print("Creating movies table...")
        create_table_movies(cursor)
        print("Creating embedded_movies table...")
        create_table_embedded_movies(cursor)
        print("Creating comments table...")
        create_table_comments(cursor)

        conn.commit()
        print("All tables created successfully.")

    except Exception as e:
        print("Error during table creation:", e)
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()
