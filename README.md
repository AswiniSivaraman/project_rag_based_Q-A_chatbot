# Movie-Based Question Answering System using RAG

An intelligent movie QA system built using **LangChain**, **OpenAI**, and **FAISS**, integrated with data migrated from **MongoDB** to **SQL**. This project leverages Retrieval-Augmented Generation (RAG) to enable natural language-based question answering from a movie dataset.

---

## Features

- MongoDB ➝ SQL Data Migration
- Semantic Embeddings using OpenAI
- FAISS-based Vector Search
- LangChain RAG Architecture
- Streamlit-Powered Web Interface
- Secure `.env`-based Configuration Handling

---

## Tech Stack

| Layer              | Tools/Tech Used                                   |
|-------------------|---------------------------------------------------|
| Database           | MongoDB, MySQL                        |
| Data Migration     | Python, Pandas, SQLAlchemy, Pymongo               |
| Embeddings         | OpenAI , FAISS                      |
| Backend Logic      | LangChain, Vector Store Retrieval                 |
| Frontend UI        | Streamlit                                         |
| Environment Config | `.env`, python-dotenv                             |

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-qa-rag.git
cd movie-qa-rag
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
```

⚠️ Important: Make sure your .env file is listed in .gitignore to avoid pushing sensitive info to GitHub.
