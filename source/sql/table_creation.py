from source.sql.create_connection import connection
from source.sql.table_query import (
    create_table_users,
    create_table_sessions,
    create_table_theaters,
    create_table_movies,
    create_table_embedded_movies,
    create_table_comments
)

def create_all_tables():
    """
    Creates all necessary tables in the MySQL database using the table definitions
    from table_query.py
    """
    conn = connection()
    if conn is None:
        print("Connection failed. Cannot create tables.")
        return

    cursor = conn.cursor()

    try:
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
        print("✅ All tables created successfully.")

    except Exception as e:
        print("❌ Error during table creation:", e)
        conn.rollback()
    
    finally:
        cursor.close()
        conn.close()
