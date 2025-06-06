# Import necessary libraries
import pandas as pd
from source.processing.load_data_from_sql import load_all_tables
from fpdf import FPDF
import os
from helper_func.comment_data_transform import comments_to_sentence
from helper_func.movies_data_transform import movies_to_sentence
from helper_func.sessions_data_transform import sessions_to_sentence
from helper_func.theaters_data_transform import theaters_to_sentence
from helper_func.users_data_transform import users_to_sentence
from helper_func.embedded_movies_data_transform import embedded_movies_to_sentence
from tqdm import tqdm

# Function to format each row as a string 
def row_to_string(row, table_name):
    if table_name == "movies":
        return movies_to_sentence(row)
    elif table_name == "comments":
        return comments_to_sentence(row)
    elif table_name == "sessions":
        return sessions_to_sentence(row)
    elif table_name == "theaters":
        return theaters_to_sentence(row)
    elif table_name == "users":
        return users_to_sentence(row)
    elif table_name == "embedded_movies":
        return embedded_movies_to_sentence(row)
    else:
        return "" 



def get_merged_all_tables():
    """
    Returns a dictionary of lists, each containing natural language row strings for one table.
    """
    all_data = load_all_tables()
    merged_data = {}

    for table_name, df in all_data.items():
        merged_data[table_name] = df.apply(lambda row: row_to_string(row, table_name), axis=1).tolist()

    return merged_data


def save_docs_as_pdf(docs, output_path="vectorstores/merged_text.pdf", show_chunks=False):
    """
    Save LangChain documents as a single PDF file with progress tracking.
    Optionally adds visual separators between chunks if show_chunks is True.

    Args:
        docs (list): List of Document objects.
        output_path (str): Path to save the output PDF.
        show_chunks (bool): If True, adds a separator line between documents/chunks.
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    print(f"Saving {len(docs)} documents to PDF...\n")
    for i, doc in enumerate(tqdm(docs, desc="Writing PDF")):
        content = doc.page_content.strip()
        lines = content.split('\n')
        for line in lines:
            if line.strip():
                pdf.multi_cell(0, 10, line)

        # Add a separator if showing chunks and it's not the last document
        if show_chunks and i < len(docs) - 1:
            pdf.ln(5) # Add some space
            pdf.set_font("Arial", 'B', 10) # Make the separator bold
            pdf.cell(0, 10, "-" * 50, 0, 1, 'C') # Centered line of dashes
            pdf.set_font("Arial", size=12) # Reset font size
            pdf.ln(5) # Add more space

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)
    print(f"\nPDF saved to '{output_path}'")
