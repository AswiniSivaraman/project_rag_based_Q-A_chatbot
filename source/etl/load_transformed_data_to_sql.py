from source.sql.table_creation import create_all_tables
from source.sql.insert_data import insert_all_data

def load_transformed_data(cleaned_data):
    print("Creating MySQL tables...")
    create_all_tables()

    print("Inserting cleaned data into tables...")
    insert_all_data(cleaned_data)

    print("ETL load process completed.")
