# Load Transformed Data into MySQL Database. This is the last step in the ETL process.

# Import necessary libraries
from source.sql.table_creation import create_all_tables
from source.sql.insert_data import insert_all_data

def load_transformed_data(cleaned_data):
    """
    Load the cleaned data into MySQL tables.
    This function creates the necessary tables in the MySQL database
    and inserts the cleaned data into these tables.
    Args:
        cleaned_data (dict): A dictionary containing cleaned data for each collection.
                             Keys are collection names and values are DataFrames.
    """

    print("Creating MySQL tables...")
    create_all_tables()

    print("Inserting cleaned data into tables...")
    insert_all_data(cleaned_data)

    print("ETL load process completed.")
