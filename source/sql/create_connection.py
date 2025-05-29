# Import necessary libraries
import mysql.connector as sconn  
from mysql.connector import Error  
from dotenv import load_dotenv 
import os  

def configuration():
    """
    Loads MySQL database configuration from a .env file and prepares a configuration dictionary.

    Returns:
        dict: A dictionary containing MySQL configuration parameters such as user, password, host, and database.
              Returns None if an error occurs.
    """
    try:
        # Load environment variables from the .env file
        load_dotenv()

        # Create the configuration dictionary using environment variables
        config = {
            "user": os.getenv("db_user"),         # Username for the MySQL connection
            "password": os.getenv("db_password"), # Password for the MySQL connection
            "host": os.getenv("db_host"),         # Host where the database is running (e.g., localhost)
            "database": os.getenv("db_name")      # Name of the database to connect to
        }

        print("Configuration completed")
        return config

    except Error as e:
        # Handle any error that might occur during configuration loading
        print("Error occurred during configuration:", e)
        return None

def connection():
    """
    Establishes a connection to the MySQL database using the configuration.

    Returns:
        MySQLConnection: A MySQL connection object if successful, otherwise None.
    """
    try:
        # Get configuration from the configuration() function
        config = configuration()

        # Return None if configuration loading failed
        if config is None:
            return None

        # Attempt to connect to the MySQL database using the configuration
        conn = sconn.connect(**config)

        # Check if the connection was successful
        if conn.is_connected():
            print("Connection completed")
        
        return conn

    except Error as e:
        # Handle any errors that occur during the connection attempt
        print("Error occurred when opening connection:", e)
        return None
