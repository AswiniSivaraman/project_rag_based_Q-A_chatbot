# Import necessary libraries
import mysql.connector as sconn  
from mysql.connector import Error  

def create_table(conn, query_create):
    """
    Creates a table in the connected MySQL database using the provided SQL query.

    Args:
        conn: Active MySQL connection object.
        query_create: SQL query string for creating the table.

    Returns:
        None
    """
    # Create a cursor object to execute SQL statements
    c = conn.cursor()
    
    try:
        # Execute the table creation query
        c.execute(query_create)
        print("Table Created Successfully")
    
    except Error as e:
        # Handle and print any errors during table creation
        print("Error occurred when creating table:", e)
