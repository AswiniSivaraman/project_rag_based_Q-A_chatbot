import os
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI # Use OpenAI's chat model if you wan to use it for paid
from langchain_groq import ChatGroq # Use Groq's chat model if you want to use it for free
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
from source.processing.embeddings import load_vectorstore, build_and_save_vectorstore  # Use this if you want to use FAISS (local storage of vectors)
from source.processing.embeddings import load_vectorstore_pinecone, build_and_save_vectorstore_pinecone # Use this if you want to use Pinecone (cloud storage of vectors)
import time


# ----------------------------------------------------------------------------------------- LOCAL FAISS STORAGE -----------------------------------------------------------------------------------------
# -------------------------- Use this if you're developing locally and want to store vector data inside the container. ----------------------------------------------------------------------------------
# -------------------------- NOTE: Not suitable for Dockerized or production deployments, as local files may not persist. -------------------------------------------------------------------------------


def answer_movie_question_faiss(query: str, k: int = 3) -> str:
    """
    Generates an answer to a movie question using RAG pipeline.
    If the vectorstore is not found, it builds one from scratch.
    """
    start_total = time.time()
    # Load API Key
    load_dotenv()
    api_key = os.getenv("groq_api_key")
    model_name = "llama3-8b-8192"

    # Auto-build vectorstore if not exists
    vectorstore_path = "vectorstores/movie_index"
    # index_file = os.path.join(vectorstore_path, "faiss.index")
    index_file = os.path.join(vectorstore_path, "index.faiss")

    start_vs = time.time()
    if not os.path.exists(index_file):
        print("Vectorstore not found. Building now...")
        build_and_save_vectorstore()
    else:
        print("Vectorstore found. Loading...")
    print(f"Vectorstore setup completed in {time.time() - start_vs:.2f} seconds")


    # Load the FAISS vectorstore
    start_load = time.time()
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    print(f"Vectorstore loaded in {time.time() - start_load:.2f} seconds")


    # Setup LLM + QA chain
    start_llm = time.time()
    llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)

    prompt_template = ChatPromptTemplate.from_template("""
    You are a helpful assistant that answers questions based on movie data.
    The context contains information in key-value format, like "directors: name", "title: name", etc.
    Search for relevant fields carefully before answering.

    <context>
    {context}
    </context>

    Question: {input}
    """)

    doc_chain = create_stuff_documents_chain(llm, prompt=prompt_template)
    retriever_chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=doc_chain)
    qa_chain = retriever_chain
    print(f"LLM & QA chain initialized in {time.time() - start_llm:.2f} seconds")


    # Step 4: Run query
    start_query = time.time()
    answer = qa_chain.invoke({"input": query})
    print(f"Query answered in {time.time() - start_query:.2f} seconds")
    print(f"Total pipeline time: {time.time() - start_total:.2f} seconds")

    print(f"User Query: {query}")
    print(f"Answer: {answer}")

    return answer['answer']



# ------------------------------------------------------------------------------------ CLOUD PINECONE STORAGE ------------------------------------------------------------------------------------------
# ------------------------------------------------  Use this when you're deploying or scaling your app. Pinecone provides persistent and scalable vector storage. --------------------------------------


def answer_movie_question_pinecone(query: str, k: int = 5) -> str:
    """
    Generates an answer to a movie question using Pinecone-based RAG pipeline.
    If the Pinecone vectorstore is not available, it builds and uploads one.
    """
    start_total = time.time()

    # Load .env variables
    load_dotenv()
    api_key = os.getenv("groq_api_key")
    model_name = "gemma2-9b-it"

    # Step 1: Load or build Pinecone vectorstore
    try:
        print("Trying to load vectorstore from Pinecone...")
        start_vs = time.time()
        vectorstore = load_vectorstore_pinecone()
        print(f"Pinecone vectorstore loaded in {time.time() - start_vs:.2f} seconds")
    except Exception as e:
        print(f"Failed to load Pinecone vectorstore. Reason: {e}")
        print("Building and uploading new vectorstore to Pinecone...")
        build_and_save_vectorstore_pinecone()
        vectorstore = load_vectorstore_pinecone()

    # Step 2: Setup Retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})

    # Step 3: Setup LLM
    start_llm = time.time()
    llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)

    # Step 4: Prompt Template
    prompt_template = ChatPromptTemplate.from_template("""
    You are a helpful assistant that answers questions based on movie data.
    The context contains information in natural language form such as movie details, plot, actors, etc.
    Answer based on the context provided and avoid guessing if information is unavailable.

    <context>
    {context}
    </context>

    Question: {input}
    """)

    # Step 5: Create RetrievalQA chain
    doc_chain = create_stuff_documents_chain(llm, prompt=prompt_template)
    retriever_chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=doc_chain)
    qa_chain = retriever_chain
    print(f"LLM & QA chain initialized in {time.time() - start_llm:.2f} seconds")

    # Step 6: Run Query
    start_query = time.time()
    answer = qa_chain.invoke({"input": query})
    print(f"Query answered in {time.time() - start_query:.2f} seconds")
    print(f"Total pipeline time: {time.time() - start_total:.2f} seconds")

    print(f"User Query: {query}")
    print(f"Answer: {answer}")

    return answer['answer']

