# Import necessary libraries
from source.sql.read_data_from_sql import load_table_as_df


def load_all_tables():
    """
    Load all SQL tables into Pandas DataFrames.
    
    Returns:
        dict: A dictionary with table names as keys and DataFrames as values.
    """
    tables = ['movies', 'comments', 'sessions', 'theaters', 'users', 'embedded_movies']
    return {table: load_table_as_df(table) for table in tables}


