# # app.py
# import streamlit as st
# from dotenv import load_dotenv
# from source.rag.rag_pipeline import (
#                             answer_movie_question_faiss,    # use this function if you are using FAISS (local storage of vectors)
#                             answer_movie_question_pinecone  # use this function if you are using Pinecone (cloud storage of vectors)
#                             )

# # Load environment variables
# load_dotenv()

# # Page setup
# st.set_page_config(page_title="🎥 Movie Chatbot RAG", layout="wide")
# st.title("🎬 Movie Intelligence Assistant")
# st.markdown("Ask any question about the movies in your database.")

# # Input
# query = st.text_input("💬 Ask your question:", placeholder="e.g., Who directed Interstellar?")

# if query:
#     with st.spinner("🤖 Thinking..."):
#         try:
#             answer = answer_movie_question_pinecone(query)  # Replace with answer_movie_question_faiss(query) if using FAISS
#             st.success("🧠 Answer:")
#             st.write(answer)
#         except Exception as e:
#             st.error(f"❌ Error: {e}")


# app.py
# Import necessary libraries
import streamlit as st
from dotenv import load_dotenv
from source.rag.rag_pipeline import (
    answer_movie_question_faiss,  # use this function if you are using FAISS (local storage of vectors)
    answer_movie_question_pinecone  # use this function if you are using Pinecone (cloud storage of vectors)
)

# Load environment variables
load_dotenv()

# --- Page Setup (MUST BE THE FIRST STREAMLIT COMMAND) ---
st.set_page_config(page_title="🎥 Movie Chatbot RAG", layout="wide")

# --- Custom Theme (Blue with Pink Mix) ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E0F2F7; /* Light Blue Background */
    }
    .stApp header {
        background-color: #1A5276; /* Darker Blue for header */
    }
    .stApp [data-testid="stHeader"] {
        background-color: #1A5276; /* Darker Blue for header */
    }
    .stApp [data-testid="stSidebar"] {
        background-color: #5DADE2; /* Medium Blue for sidebar */
        color: white;
    }
    .stApp [data-testid="stSidebar"] h2 {
        color: white;
    }
    .stApp [data-testid="stSidebar"] p {
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #F0F8FF; /* Alice Blue input background */
        color: #333333;
        border: 1px solid #A9D9F7; /* Light Blue border for input */
    }
    .stButton>button {
        background-color: #FF69B4; /* Hot Pink button */
        color: white;
        border-radius: 8px; /* Slightly more rounded */
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2); /* Subtle shadow */
    }
    .stButton>button:hover {
        background-color: #FF1493; /* Deeper Pink on hover */
        box-shadow: 2px 2px 8px rgba(0,0,0,0.3);
    }
    .stSuccess {
        background-color: #B0E0E6; /* Powder Blue for success messages */
        color: #333333;
        border-radius: 5px;
        padding: 10px;
    }
    .stError {
        background-color: #FFB6C1; /* Light Pink for error messages */
        color: #333333;
        border-radius: 5px;
        padding: 10px;
    }
    .chat-container {
        border: 2px solid #5DADE2; /* Medium Blue border for chat container */
        border-radius: 12px; /* More rounded corners for the chat box */
        padding: 20px;
        min-height: 400px;
        max-height: 600px;
        overflow-y: auto; /* Enable scrolling for conversation */
        background-color: #FFF5EE; /* White background for chat */
        box-shadow: 4px 4px 10px rgba(0,0,0,0.1); /* Soft shadow for depth */
        display: flex; /* Use flexbox for message alignment */
        flex-direction: column; /* Stack messages vertically */
    }
    .user-message {
        background-color: #ADD8E6; /* Light Blue for user messages */
        color: #333333;
        border-radius: 15px 15px 0 15px; /* Rounded corners, flat bottom-right */
        padding: 12px 18px;
        margin-bottom: 12px;
        align-self: flex-end; /* Align to the right */
        max-width: 75%; /* Slightly less wide */
        font-size: 1.05em;
    }
    .bot-message {
        background-color: #FFC0CB; /* Pink for bot messages */
        color: #333333;
        border-radius: 15px 15px 15px 0; /* Rounded corners, flat bottom-left */
        padding: 12px 18px;
        margin-bottom: 12px;
        align-self: flex-start; /* Align to the left */
        max-width: 75%;
        font-size: 1.05em;
    }

    /* --- Adjust spacing for titles/headers --- */
    h1 {
        margin-bottom: 0em; 
        margin-top: 0em; 
    }
    h2 {
        margin-top: 0.1em; 
        margin-bottom: 0.1em; 
    }
    /* Aggressive margin reduction for elements within the info box */
    h3 {
        margin-top: 0.2em; 
        margin-bottom: 0.2em; 
    }
    h4 {
        margin-top: 0.4em; 
        margin-bottom: 0.1em; 
    }
    p { /* Reduce paragraph margins to pull text closer to headers */
        margin-top: 0.1em;
        margin-bottom: 0.1em;
    }
    ul {
        margin-top: 0.1em; /* Reduced from 0.3em */
        margin-bottom: 0.1em; /* Reduced from 0.3em */
        padding-left: 1.5em; /* Keep some indent for list items */
    }
    /* Specific adjustment for the hr lines */
    hr {
        margin-top: 0.5em; /* Adjust as needed */
        margin-bottom: 0.5em; /* Adjust as needed */
    }
    /* You might also need to target the Streamlit internal div for headers */
    [data-testid="stHeader"] {
        padding-bottom: 0.5rem; /* Reduce padding below the Streamlit header */
    }
    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        gap: 0rem; /* Reduce gap between vertical blocks (might affect other elements) */
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --- Session State for Chat History ---
if "messages" not in st.session_state:
    # Initialize with a default greeting message from the bot
    st.session_state.messages = [
        {"role": "bot", "content": "Hi! I am your Movie Bot. How can I assist you today? Feel free to ask me anything about movies!"}
    ]

# --- Page Title ---
st.title("🎬 Movie Intelligence Assistant BOT")

# --- Layout with Columns ---
col1, col2 = st.columns([3, 1]) # 3 parts for main content, 1 part for sidebar/panel

with col1:
    st.markdown("---") # Separator. Consider removing if spacing is tight enough.
    st.subheader("💬... Chat with the Movie Bot")

    # Construct the HTML for the entire chat container with messages inside
    chat_history_html = '<div class="chat-container">'
    for message in st.session_state.messages:
        if message["role"] == "user":
            chat_history_html += f'<div class="user-message">👤 {message["content"]}</div>'
        else:
            chat_history_html += f'<div class="bot-message">🤖 {message["content"]}</div>'
    chat_history_html += '</div>'

    # Render the entire chat history as one markdown block
    st.markdown(chat_history_html, unsafe_allow_html=True)


    st.markdown("---") # Separator
    # Input form to prevent repeated queries
    with st.form(key="chat_form", clear_on_submit=True):
        query = st.text_input("Ask your question about movies:", placeholder="e.g., Who directed Interstellar?", key="movie_question_input")
        submit_button = st.form_submit_button(label="Send ➡️")

        if submit_button and query:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": query})

            with st.spinner("🤖 Thinking..."):
                try:
                    # --- Choose your RAG function here ---
                    # Using Pinecone as per previous example. Change if you use FAISS.
                    answer = answer_movie_question_pinecone(query)
                    st.session_state.messages.append({"role": "bot", "content": answer})
                    st.rerun()
                except Exception as e:
                    error_message = f"❌ Error: {e}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "bot", "content": error_message})
                    st.rerun()

        elif submit_button and not query:
            st.warning("Please type a question before sending!")

    # Clear Button - moved outside the form to keep its state independent
    if st.button("🗑️ Clear Chat", key="clear_chat_button"):
        # When clearing, reset to the default greeting message
        st.session_state.messages = [
            {"role": "bot", "content": "Hi! I am your Movie Bot. How can I assist you today? Feel free to ask me anything about movies!"}
        ]
        st.rerun()

with col2:
    st.markdown("---") # Separator
    st.subheader("ℹ️ Bot Information")
    st.markdown(
        """
        <div style="background-color: #4169E1; padding: 20px; border-radius: 10px; color: white; box-shadow: 4px 4px 10px rgba(0,0,0,0.1);">
            <h3>🎥 Movie Chatbot RAG</h3>
            <p><strong>Purpose:</strong> This chatbot is designed to provide intelligent answers to your movie-related questions using a Retrieval-Augmented Generation (RAG) system. It leverages a sample_mflix data from MongoDB to deliver accurate and relevant responses.</p>
            <hr style="border-color: #A9D9F7;">
            <h4>❓ What can I ask?</h4>
            <p>You can ask questions like:</p>
            <ul>
                <li>"List movies starring *Emma Stone*."</li>
                <li>"Who starred in *La La Land*?"</li>
                <li>"What genre is *The Godfather*?"</li>
            </ul>
            <hr style="border-color: #A9D9F7;">
            <h4>☁️ Vector Database Information</h4>
            <p>This bot currently utilizes the **'movie-qa-index'** from Pinecone for efficient information retrieval. Pinecone is a cloud-based vector database where movie data is stored as vectors, enabling fast and relevant search results.</p>
        </div>
        """,
        unsafe_allow_html=True
    )


