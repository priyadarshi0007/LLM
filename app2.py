import streamlit as st
from utils import load_css, initialize_session_state, display_chat_interface, get_user_input
from chat_logic import handle_user_query
from config import configure_sidebar

def main():
    """Main function to run the Streamlit app."""
    # Configure the app
    st.set_page_config(page_title="Gemini Pro Q&A Chatbot", page_icon=":robot:", layout="wide")
    st.title("Gemini Pro Q&A Chatbot")

    # Load external CSS
    load_css("styles.css")

    # Initialize session state
    initialize_session_state()

    # Configure the sidebar
    temperature, top_k, top_p = configure_sidebar()

    # Get user input
    user_query, send_button = get_user_input()

    # Handle user query and update chat history immediately
    if send_button and user_query.strip():
        handle_user_query(user_query, temperature, top_k, top_p)

    # Display updated chat interface after processing user query
    display_chat_interface()

    # Warn the user if the input is empty
    if send_button and not user_query.strip():
        st.warning("Please enter a question first.")

# Run the app
if __name__ == "__main__":
    main()