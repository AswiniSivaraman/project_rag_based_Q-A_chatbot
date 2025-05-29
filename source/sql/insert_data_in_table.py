# Import necessary libraries
import mysql.connector as sconn  
from mysql.connector import Error  

def insert_data_to_table(conn, query_insert, value):
    """
    Inserts multiple rows of data into a MySQL table using the provided SQL query and values.

    Args:
        conn: Active MySQL connection object.
        query_insert: SQL INSERT query with placeholders (e.g., "INSERT INTO table_name (col1, col2) VALUES (%s, %s)").
        value: A list of tuples, where each tuple contains the values to be inserted into a row.

    Returns:
        None
    """
    # Create a cursor object to execute SQL commands
    c = conn.cursor()

    try:
        # Execute the INSERT query for all records in the value list
        c.executemany(query_insert, value)

        # Commit the transaction to permanently save the changes
        conn.commit()
        print("Data inserted into the table successfully")

    except Error as e:
        # Print any error that occurs during data insertion
        print("Error occurred when inserting the data into the table:", e)
