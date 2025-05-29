import os
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from source.processing.embeddings import load_vectorstore, build_and_save_vectorstore

def answer_movie_question(query: str, k: int = 3) -> str:
    """
    Generates an answer to a movie question using RAG pipeline.
    Builds the vectorstore if not found.
    """
    # Load API Key
    load_dotenv()
    api_key = os.getenv("api_key_5")

    # Auto-build vectorstore if not exists
    vectorstore_path = "vectorstores/movie_index"
    index_file = os.path.join(vectorstore_path, "faiss.index")

    if not os.path.exists(index_file):
        print("📦 Vectorstore not found. Building now...")
        build_and_save_vectorstore()
    else:
        print("✅ Vectorstore found. Loading...")

    # Load the FAISS vectorstore
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})

    # Setup LLM + QA chain
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # Run the query
    return qa_chain.invoke({"query": query})
