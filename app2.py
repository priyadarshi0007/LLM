import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables (make sure you have a .env file with your API key)
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

# Set up the Streamlit app
st.set_page_config(page_title="Gemini Pro Q&A Chatbot", page_icon=":robot:")
st.title("Gemini Pro Q&A Chatbot")

# Define custom CSS for styling the chat interface
st.markdown("""
    <style>
        .user-bubble {
            background-color: #e1ffc7;
            padding: 10px;
            border-radius: 20px;
            max-width: 70%;
            margin-bottom: 10px;
            margin-left: auto;
            display: inline-block;
            font-size: 16px;
        }
        .assistant-bubble {
            background-color: #f1f1f1;
            padding: 10px;
            border-radius: 20px;
            max-width: 70%;
            margin-bottom: 10px;
            margin-right: auto;
            display: inline-block;
            font-size: 16px;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
            padding: 20px;
            max-height: 500px;
            overflow-y: auto;
            margin-bottom: 70px; /* Make space for the input box */
        }
        .chat-input-box {
            position: fixed;
            bottom: 20px;
            left: 20px;
            right: 20px;
            background-color: white;
            padding: 10px;
            border-radius: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .chat-input-box input {
            width: 85%;
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #ccc;
        }
        .chat-input-box button {
            width: 10%;
            padding: 10px;
            margin-left: 10px;
            border: none;
            border-radius: 10px;
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }
        .chat-input-box button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for storing chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display previous chat history in chat bubbles
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f'<div class="user-bubble">{chat["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="assistant-bubble">{chat["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Create a chat input box and send button inside a fixed container
with st.form(key='chat_form', clear_on_submit=True):
    user_query = st.text_input("Type your message here:", key='user_input')
    send_button = st.form_submit_button("Send")

# Handle the message submission
if send_button:
    if user_query:
        try:
            # Append the user's message to the chat history
            st.session_state.chat_history.append({"role": "user", "content": user_query})

            # Generate response from the model
            answer = model.generate_content(user_query)

            # Append the assistant's response to the chat history
            st.session_state.chat_history.append({"role": "assistant", "content": answer.text})

            # Update the chat window with the new message and response
            st.markdown('<div class="chat-container">', unsafe_allow_html=True)
            st.markdown(f'<div class="user-bubble">{user_query}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="assistant-bubble">{answer.text}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question first.")