from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from source.processing.merge_tables import get_final_merged_list
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from dotenv import load_dotenv
import os
import numpy as np

# Load API Key
load_dotenv()
api_key = os.getenv("api_key_5")

def build_and_save_vectorstore(save_path="vectorstores/movie_index"):
    # 1. Load final merged list of strings
    all_sentences = get_final_merged_list()
    print(f"Loaded {len(all_sentences)} text entries")

    # 2. Convert to LangChain Documents
    docs = [Document(page_content=sentence) for sentence in all_sentences]

    # 3. Split into smaller chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(docs)
    print(f"Split into {len(split_docs)} chunks")

    # 4. Initialize embedding model
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)

    # 5. Build vectorstore from documents
    vectorstore = FAISS.from_documents(split_docs, embeddings)

    # 6. Save vectorstore
    vectorstore.save_local(save_path)
    print(f"Vectorstore saved to '{save_path}'")



def load_vectorstore(load_path="vectorstores/movie_index"):
    """
    Load FAISS vectorstore from the specified path.

    Args:
        load_path (str): Path where the vectorstore is stored.

    Returns:
        vectorstore: A FAISS vectorstore object
    """
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = FAISS.load_local(load_path, embeddings, allow_dangerous_deserialization=True)
    return vectorstore
