import streamlit as st
from Utilities import generate_response_with_gemini

def handle_user_query(user_query, temperature, top_k, top_p):
    """Handles user query by generating a response and updating chat history."""
    try:
        # Append the user's message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_query})

        # Display typing indicator
        typing_placeholder = st.empty()
        typing_placeholder.markdown('<div class="typing-indicator">Bot is typing...</div>', unsafe_allow_html=True)

        # Generate response with the specified parameters
        response_text = generate_response_with_gemini(user_query, temperature, top_k, top_p)

        # Remove typing indicator
        typing_placeholder.empty()

        # Append the assistant's response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response_text})

    except Exception as e:
        st.error(f"An error occurred: {e}")