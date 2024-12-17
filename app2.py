import streamlit as st
from parse_file_typ import parse_vtt_file
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

    # Sidebar for model configuration
    temperature, top_k, top_p = configure_sidebar()

    # Section for uploading .vtt files
    with st.sidebar.expander("Upload Context File (.vtt)", expanded=False):
        uploaded_file = st.file_uploader("Upload a .vtt file for context-based Q&A", type=["vtt"])
        if uploaded_file:
            # Parse and store the .vtt file content
            context = parse_vtt_file(uploaded_file)
            st.session_state["context"] = context
            st.success("File uploaded and context extracted!")
            st.write("Extracted Context Preview:")
            st.text(context[:500])  # Display the first 500 characters as a preview

    # Display the chat interface
    display_chat_interface()

    # Get user input
    user_query, send_button = get_user_input()

    # Handle user query
    if send_button and user_query.strip():
        # Use uploaded context if available; otherwise, answer without context
        context = st.session_state.get("context", "")
        handle_user_query(user_query, temperature, top_k, top_p, context)

    # Warn the user if the input is empty
    if send_button and not user_query.strip():
        st.warning("Please enter a question first.")


# Run the app
if __name__ == "__main__":
    main()