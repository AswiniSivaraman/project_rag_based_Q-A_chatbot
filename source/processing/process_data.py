import pandas as pd
from source.processing.load_data_from_sql import load_all_tables



# Function to format each row as a string "col1: val1, col2: val2, ..."
def row_to_string(row):
    return ', '.join([f"{col} : {str(row[col])}" for col in row.index if pd.notnull(row[col])])


def get_merged_all_tables():
    """
    Returns a dictionary of lists, each containing merged row strings for one table.
    """
    all_data = load_all_tables()
    merged_data = {}

    for table_name, df in all_data.items():
        merged_data[table_name] = df.apply(row_to_string, axis=1).tolist()

    return merged_data