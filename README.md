# Movie-Based Question Answering System using RAG

An intelligent movie QA system built using **LangChain**, **OpenAI**, **FAISS**, **Pinecone**, **HuggingFace**, **Groq** integrated with data migrated from **MongoDB** to **MySQL**. This project leverages Retrieval-Augmented Generation (RAG) to enable natural language-based question answering from a movie dataset.

---

## Features

- MongoDB ➝ SQL Data Migration
- Semantic Embeddings using OpenAIEmbeddings/HuggingFaceEmbeddings
- FAISS-based Vector Search for Local
- Pinecone-based vector search for cloud deployment
- LangChain RAG Architecture
- Streamlit-Powered Web Interface
- Secure `.env`-based Configuration Handling

---

## Tech Stack

| Layer              | Tools/Tech Used                                   |
|-------------------|---------------------------------------------------|
| Database           | MongoDB, MySQL                        |
| Data Migration     | Python, Pandas, SQLAlchemy, Pymongo               |
| Embeddings         | OpenAI , FAISS , Pinecone, HuggingFace                     |
| Backend Logic      | LangChain, Vector Store Retrieval                 |
| Frontend UI        | Streamlit                                         |
| Environment Config | `.env`, python-dotenv                             |

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AswiniSivaraman/project_rag_based_movie_QA_chatbot.git
cd <file path>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a .env file in the root directory and add the following variables:

```env

MongoDB Config
mongodb_uri=mongodb+srv://<your-mongo-uri>
db_user=your_sql_username
db_password=your_sql_password
db_host=localhost
db_name=your_database_name

OpenAI API Keys (rotate if token limit hits)
api_key_1=sk-...
api_key_2=sk-...
api_key_3=sk-...
api_key_4=sk-...
api_key_5=sk-...

groq_api_key=your_groq_api_key
pinecone_api_key=your_pinecone_api_key
pinecone_env=your_pinecone_environment_name
pinecone_index_name=your_pinecone_indexname

```

⚠️ Important: Make sure your .env file is listed in .gitignore to avoid pushing sensitive info to GitHub.

---

## Run the Application

**Before you begin:**

 - Ensure your MongoDB cluster connection has been successfully established.
   
 - Make sure your Pinecone index connection has been successfully established.

 - Verify that the MySQL database you created is actively in use.

**Step 1**: Execute the backend setup script to:

- Extract data from MongoDB

- Transform and load it into SQL

- Generate and store embeddings

```bash
python main.py
```

**Step 2:** Launch the Streamlit interface to start asking questions:
```bash
streamlit run chatbot.py
```

Once the app is running, you can ask movie-related questions

---

## Project Libraries and Tools Documentation

This table lists the key libraries and tools used in this project, along with links to their official documentation for further reference.

| Library/Tool           | Documentation Link                                                                             |
| :--------------------- | :--------------------------------------------------------------------------------------------- |
| PyMongo                | [https://pymongo.readthedocs.io/en/stable/](https://pymongo.readthedocs.io/en/stable/)          |
| python-dotenv          | [https://saurabh-kumar.com/python-dotenv/](https://saurabh-kumar.com/python-dotenv/)            |
| pandas                 | [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)                             |
| SQLAlchemy             | [https://docs.sqlalchemy.org/en/20/](https://docs.sqlalchemy.org/en/20/)                       |
| mysql-connector-python | [https://dev.mysql.com/doc/connector-python/en/](https://dev.mysql.com/doc/connector-python/en/) |
| openai                 | [https://platform.openai.com/docs/libraries/python-sdk](https://platform.openai.com/docs/libraries/python-sdk) |
| langchain              | [https://python.langchain.com/docs/](https://python.langchain.com/docs/)                       |
| langchain-community    | [https://python.langchain.com/docs/modules/model_io/llms/integrations/](https://python.langchain.com/docs/modules/model_io/llms/integrations/) |
| tiktoken               | [https://github.com/openai/tiktoken](https://github.com/openai/tiktoken)                       |
| numpy                  | [https://numpy.org/doc/](https://numpy.org/doc/)                                               |
| streamlit              | [https://docs.streamlit.io/](https://docs.streamlit.io/)                                       |
| faiss-cpu              | [https://github.com/facebookresearch/faiss/wiki/](https://github.com/facebookresearch/faiss/wiki/) |
| fpdf                   | [https://pyfpdf.readthedocs.io/en/latest/](https://pyfpdf.readthedocs.io/en/latest/)            |
| langchain-groq         | [https://python.langchain.com/docs/integrations/llms/groq](https://python.langchain.com/docs/integrations/llms/groq) |
| sentence-transformers  | [https://www.sbert.net/docs/index.html](https://www.sbert.net/docs/index.html)                 |
| langchain-huggingface  | [https://python.langchain.com/docs/integrations/text_embedding/huggingface_embeddings](https://python.langchain.com/docs/integrations/text_embedding/huggingface_embeddings) |
| PyTorch (torch)        | [https://pytorch.org/docs/stable/index.html](https://pytorch.org/docs/stable/index.html)       |
| pinecone-client        | [https://docs.pinecone.io/docs/](https://docs.pinecone.io/docs/)                               |
| langchain-pinecone     | [https://python.langchain.com/docs/integrations/vectorstores/pinecone](https://python.langchain.com/docs/integrations/vectorstores/pinecone) |
| langchain-openai       | [https://python.langchain.com/docs/integrations/llms/openai](https://python.langchain.com/docs/integrations/llms/openai) |
| MongoDB Documentation  | [https://www.mongodb.com/docs/](https://www.mongodb.com/docs/)                                 |
| Pinecone Documentation | [https://docs.pinecone.io/](https://docs.pinecone.io/)                                         |
| Docker Documentation   | [https://docs.docker.com/](https://docs.docker.com/)                                           |
| Docker Hub Documentation | [https://docs.docker.com/docker-hub/](https://docs.docker.com/docker-hub/)                     |
| Amazon EC2 Documentation | [https://docs.aws.amazon.com/ec2/](https://docs.aws.amazon.com/ec2/)                           |

---

**Note**: To learn more about this project, please refer to the **project_document** file.
