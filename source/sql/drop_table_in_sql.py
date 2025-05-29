# Import necessary libraries
import mysql.connector as sconn  
from mysql.connector import Error  

def drop_table(conn, query_drop):
    """
    Drops a table in the connected MySQL database using the provided SQL query.

    Args:
        conn: Active MySQL connection object.
        query_drop: SQL query string to drop the table (e.g., "DROP TABLE IF EXISTS table_name").

    Returns:
        None
    """
    # Create a cursor object to execute SQL statements
    c = conn.cursor()

    try:
        # Execute the DROP TABLE query
        c.execute(query_drop)
        print("Table dropped successfully")
    
    except Error as e:
        # Handle and print any errors that occur during table dropping
        print("Error occurred when dropping the table:", e)
