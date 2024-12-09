import streamlit as st
from utilities import generate_response_with_gemini

# Helper Function: Load External CSS
def load_css(css_file):
    """Loads and applies external CSS for styling."""
    with open(css_file, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize Session State
def initialize_session_state():
    """Initializes session state for chat history."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

# Display Chat Interface
def display_chat_interface():
    """Displays the chat interface with user and assistant messages."""
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f'<div class="user-bubble">{chat["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-bubble">{chat["content"]}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Chat Input Box
def get_user_input():
    """Creates a chat input box and returns user input."""
    with st.form(key="chat_form", clear_on_submit=True):
        user_query = st.text_input("Type your message here:", key="user_input")
        send_button = st.form_submit_button("Send")
    return user_query, send_button

# Chatbot Logic
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

# Main Function
def main():
    """Main function to run the Streamlit app."""
    # Configure the app
    st.set_page_config(page_title="Gemini Pro Q&A Chatbot", page_icon=":robot:", layout="wide")
    st.title("Gemini Pro Q&A Chatbot")

    # Load external CSS
    load_css("styles.css")

    # Initialize session state
    initialize_session_state()

    # Sidebar sliders for model configuration
    st.sidebar.header("Model Configuration")

    # Add information bubble for Temperature
    st.sidebar.markdown("""
        <span style="font-size: 16px; font-weight: bold;">Temperature</span>
        <a href="#" title="Controls the randomness of the model's output. Higher values (e.g., 0.8) make output more random, while lower values (e.g., 0.2) make it more deterministic.">
            ℹ️
        </a>
    """, unsafe_allow_html=True)
    temperature = st.sidebar.slider(" ", 0.0, 1.0, 0.7, 0.1)

    # Add information bubble for Top-K
    st.sidebar.markdown("""
        <span style="font-size: 16px; font-weight: bold;">Top-K</span>
        <a href="#" title="Limits the model to selecting from the top-K most probable tokens. Lower values restrict choices, while higher values allow more diversity.">
            ℹ️
        </a>
    """, unsafe_allow_html=True)
    top_k = st.sidebar.slider(" ", 1, 100, 40, 1)

    # Add information bubble for Top-P
    st.sidebar.markdown("""
        <span style="font-size: 16px; font-weight: bold;">Top-P</span>
        <a href="#" title="Controls nucleus sampling, selecting tokens with cumulative probability ≤ top-p. Lower values create more deterministic outputs.">
            ℹ️
        </a>
    """, unsafe_allow_html=True)
    top_p = st.sidebar.slider(" ", 0.0, 1.0, 0.9, 0.1)

    # Display chat interface
    display_chat_interface()

    # Get user input
    user_query, send_button = get_user_input()

    # Handle user query
    if send_button:
        if user_query.strip():
            handle_user_query(user_query, temperature, top_k, top_p)
            # Refresh chat interface after updating
            display_chat_interface()
        else:
            st.warning("Please enter a question first.")

# Run the app
if __name__ == "__main__":
    main()