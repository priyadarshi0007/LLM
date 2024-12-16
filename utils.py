import streamlit as st

def load_css(css_file):
    """Loads and applies external CSS for styling."""
    with open(css_file, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def initialize_session_state():
    """Initializes session state for chat history."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def display_chat_interface():
    """Displays the chat interface with user and assistant messages."""
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        role_class = "user-bubble" if chat["role"] == "user" else "assistant-bubble"
        st.markdown(f'<div class="{role_class}">{chat["content"]}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def get_user_input():
    """Creates a chat input box and returns user input."""
    with st.form(key="chat_form", clear_on_submit=True):
        user_query = st.text_input("Type your message here:", key="user_input")
        send_button = st.form_submit_button("Send")
    return user_query, send_button