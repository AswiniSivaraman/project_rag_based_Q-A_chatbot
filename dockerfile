# Base Python image
FROM python:3.10-slim

# Disable .pyc and stdout buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy only necessary files
COPY requirements.txt /app/
COPY chatbot.py /app/
COPY source/rag/rag_pipeline.py /app/source/rag/
COPY source/processing/embeddings.py /app/source/processing/
COPY source/processing/merge_tables.py /app/source/processing/
COPY source/processing/process_data.py /app/source/processing/
COPY source/processing/load_data_from_sql.py /app/source/processing/
COPY source/sql/read_data_from_sql.py /app/source/sql/
COPY source/sql/create_connection.py /app/source/sql/
COPY helper_func/comment_data_transform.py /app/helper_func/
COPY helper_func/movies_data_transform.py /app/helper_func/
COPY helper_func/sessions_data_transform.py /app/helper_func/
COPY helper_func/theaters_data_transform.py /app/helper_func/
COPY helper_func/users_data_transform.py /app/helper_func/
COPY helper_func/embedded_movies_data_transform.py /app/helper_func/

 
# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run the app (replace chatbot.py if needed)
CMD ["streamlit", "run", "chatbot.py"]
