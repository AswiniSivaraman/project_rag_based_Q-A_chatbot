# Import the required MySQL connector module and Error class for exception handling
import mysql.connector as sconn
from mysql.connector import Error

def close_connection(conn):
    """
    Closes the given MySQL database connection.

    Args:
        conn: The active MySQL connection object to be closed.

    Returns:
        None
    """
    try:
        # Attempt to close the connection
        conn.close()
        print("Connection closed successfully")
    except Error as e:
        # Handle any errors that occur while closing the connection
        print("Error occurred when closing the connection:", e)
