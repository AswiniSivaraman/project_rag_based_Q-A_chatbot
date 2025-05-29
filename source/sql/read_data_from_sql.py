import pandas as pd
from source.sql.create_connection import connection

def load_table_as_df(table_name):
    """
    Load a SQL table as a Pandas DataFrame using the provided connection() function.

    Args:
        table_name (str): Name of the table to read.

    Returns:
        pd.DataFrame: Table content as DataFrame.
    """
    try:
        conn = connection()
        if conn is None:
            print("❌ No connection established.")
            return pd.DataFrame()
        
        query = f"SELECT * FROM {table_name};"
        df = pd.read_sql(query, conn)
        print(f"✅ Loaded {len(df)} records from '{table_name}' table.")
        conn.close()
        return df

    except Exception as e:
        print(f"❌ Error while reading {table_name}: {e}")
        return pd.DataFrame()
