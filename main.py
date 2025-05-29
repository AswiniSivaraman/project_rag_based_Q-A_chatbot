# import necessary libraries
from source.etl.mongodb_extract import fetch_multiple_collections
from source.etl.transform_extracted_data import clean_extracted_data
from source.etl.load_transformed_data_to_sql import load_transformed_data
from source.rag.rag_pipeline import answer_movie_question


# This script orchestrates the ETL process by calling the necessary functions to extract, transform, and load data.
collections = ['comments', 'embedded_movies', 'movies', 'sessions', 'theaters', 'users']
data = fetch_multiple_collections(collections)  # Extract data from MongoDB
cleaned_data = clean_extracted_data(data)       # Transform the extracted data
load_transformed_data(cleaned_data)             # Load the cleaned data into MySQL



# Example usage of the RAG pipeline to answer a movie-related question
# query = input("💬 Ask a movie-related question: ")
query = "list the movies with the highest imbd rating"
answer = answer_movie_question(query)
print("\n🧠 Answer:")
print(answer)