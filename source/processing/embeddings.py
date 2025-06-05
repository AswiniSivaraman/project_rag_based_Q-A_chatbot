from langchain_openai import OpenAIEmbeddings  # use if you have OpenAI API access which is paid 
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings # use if you want to use free embeddings
from source.processing.merge_tables import get_final_merged_list
from source.processing.process_data import save_docs_as_pdf
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from dotenv import load_dotenv
import os
import numpy as np
import time
from tqdm import tqdm
import pinecone
from pinecone import Pinecone as pc_client
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from langchain_pinecone import PineconeVectorStore


# ------------------------------------ use this when you want to use FAISS and store the vectors in your local machine but if you are dockerizing the app, you need to use Pinecone -------------------------------------------------

# Load API Key
load_dotenv()
api_key = os.getenv("api_key_5")

def build_and_save_vectorstore(save_path="vectorstores/movie_index", batch_size=500):
    # 1. Load final merged list of strings
    all_sentences = get_final_merged_list()
    print(f"Loaded {len(all_sentences)} text entries")

    # 2. Convert to LangChain Documents and save as PDF
    # docs = [Document(page_content=sentence) for sentence in all_sentences]
    start = time.time()
    docs = [Document(page_content=txt) for txt in all_sentences if isinstance(txt, str) and len(txt.strip()) > 0]
    print(f"Docs created in {time.time() - start:.2f} seconds")
    
    start = time.time()
    save_docs_as_pdf(docs, output_path="vectorstores/faiss_merged_text.pdf") 
    print(f"PDF saved in {time.time() - start:.2f} seconds")

    # 3. Split into smaller chunks
    start = time.time()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(docs)
    save_docs_as_pdf(split_docs, output_path="vectorstores/faiss_splitted_docs.pdf") 
    print(f"Split into {len(split_docs)} chunks in {time.time() - start:.2f} seconds")


    # 4. Initialize embedding model
    # embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 5. Build vectorstore from documents
    start = time.time()
    vectorstore = None
    print(f"Embedding {len(split_docs)} chunks in batches of {batch_size}...\n")

    for i in tqdm(range(0, len(split_docs), batch_size), desc="Embedding Progress"):
        batch = split_docs[i:i + batch_size]
        if vectorstore is None:
            vectorstore = FAISS.from_documents(batch, embeddings)
        else:
            vectorstore.add_documents(batch)

    print(f"Vectorstore built in {time.time() - start:.2f} seconds")
    
    
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
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(load_path, embeddings, allow_dangerous_deserialization=True)
    print(f"Vectorstore loaded from: {load_path}")   
    return vectorstore


# ------------------------------------ use this when you want to use Pinecone because pinecone is best for production and scalable system ---------------------------------------


def build_and_save_vectorstore_pinecone(batch_size=500):

    # Pinecone init
    load_dotenv()
    pinecone_api = os.getenv("pinecone_api_key")
    pinecone_index_name = os.getenv("pinecone_index_name")

    # Load docs
    all_sentences = get_final_merged_list()
    # docs = [Document(page_content=txt) for txt in all_sentences if isinstance(txt, str) and len(txt.strip()) > 0]
    docs = []
    print("Converting text sentences to LangChain Documents...\n")
    for txt in tqdm(all_sentences, desc="Table to Document Conversion"):
        if isinstance(txt, str) and len(txt.strip()) > 0:
            docs.append(Document(page_content=txt))


    # # Save original docs as PDFs
    save_docs_as_pdf(docs, output_path="vectorstores/pinecone_merged_text.pdf")
    print("documents saved as PDF successfully: 'vectorstores/pinecone_merged_text.pdf'") 

    # Split
    print("Splitting documents into smaller chunks...\n")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
    split_docs = splitter.split_documents(docs)
    print(f"Split into {len(split_docs)} chunks")

    save_docs_as_pdf(split_docs, output_path="vectorstores/pinecone_splitted_docs.pdf", show_chunks=True)
    print("Splitted documents saved as PDF successfully: 'vectorstores/pinecone_splitted_docs.pdf'")

    # Embeddings
    print("Initializing embeddings...\n")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    print("Embeddings initialized successfully.")

    # Init Pinecone client
    print("Initializing Pinecone client...\n")
    pinecone_client = pc_client(api_key=pinecone_api)
    print("Pinecone client initialized successfully.")

    pinecone_index_object = pinecone_client.Index(pinecone_index_name)

    # Check if index exists
    print(f"Checking if Pinecone index '{pinecone_index_name}' exists...\n")
    index_names = [index.name for index in pinecone_client.list_indexes()]
    if pinecone_index_name not in index_names:
        raise ValueError(f"Pinecone index '{pinecone_index_name}' not found. Please create it from dashboard.")

     # Upload vectors
    print(f"Uploading {len(split_docs)} chunks to Pinecone index '{pinecone_index_name}'")
    vector_store = PineconeVectorStore(index=pinecone_index_object, embedding=embeddings, text_key="text")
    vector_store.add_documents(split_docs)
    print("Upload completed.")


def load_vectorstore_pinecone():
    load_dotenv()
    pinecone_api = os.getenv("pinecone_api_key")
    pinecone_env = os.getenv("pinecone_env")
    pinecone_index_name = os.getenv("pinecone_index_name")

    # Init Pinecone client (required by SDK, even if not directly used here)
    pinecone_client = pc_client(api_key=pinecone_api)
    pinecone_index_object = pinecone_client.Index(pinecone_index_name)

    print("Loading Pinecone vectorstore...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    print("Using HuggingFace embeddings for Pinecone vectorstore.")

    try:
        stats = pinecone_index_object.describe_index_stats()
        total_vectors = stats['total_vector_count']
        if total_vectors == 0:
            raise ValueError(f"Pinecone index '{pinecone_index_name}' is empty. Please build the vectorstore first.")

        print(f"Connecting to Pinecone environment: {pinecone_env}")
        vectorstore = PineconeVectorStore(index=pinecone_index_object, embedding=embeddings, text_key="text")
        # retriever = vectorstore.as_retriever()
        print(f"Loaded vectorstore from Pinecone index: {pinecone_index_name}")
        return vectorstore
    
    except Exception as e:
        print(f"Error ocuureed when retrieving vector from Pinecone vectorstore: {e}")
        raise e
