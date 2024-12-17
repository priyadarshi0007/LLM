import streamlit as st
from Utilities import generate_response_with_gemini

def handle_user_query(user_query, temperature, top_k, top_p, context=""):
    """
    Handles user query and updates chat history efficiently.
    """
    try:
        # Append the user's message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_query})

        # Combine context and query
        query_with_context = f"Context: {context}\n\nQuestion: {user_query}" if context else user_query

        # Generate response
        response_text = generate_response_with_gemini(query_with_context, temperature, top_k, top_p)

        # Append assistant's response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response_text})

    except Exception as e:
        st.error(f"An error occurred: {e}")