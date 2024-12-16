import streamlit as st

def configure_sidebar():
    """Configure the sidebar with model parameters."""
    st.sidebar.header("Model Configuration")

    # Temperature slider
    st.sidebar.markdown("""
        <span style="font-size: 16px; font-weight: bold;">Temperature</span>
        <a href="#" title="Controls the randomness of the model's output. Higher values (e.g., 0.8) make output more random, while lower values (e.g., 0.2) make it more deterministic.">
            ℹ️
        </a>
    """, unsafe_allow_html=True)
    temperature = st.sidebar.slider(" ", 0.0, 1.0, 0.7, 0.1)

    # Top-K slider
    st.sidebar.markdown("""
        <span style="font-size: 16px; font-weight: bold;">Top-K</span>
        <a href="#" title="Limits the model to selecting from the top-K most probable tokens. Lower values restrict choices, while higher values allow more diversity.">
            ℹ️
        </a>
    """, unsafe_allow_html=True)
    top_k = st.sidebar.slider(" ", 1, 100, 40, 1)

    # Top-P slider
    st.sidebar.markdown("""
        <span style="font-size: 16px; font-weight: bold;">Top-P</span>
        <a href="#" title="Controls nucleus sampling, selecting tokens with cumulative probability ≤ top-p. Lower values create more deterministic outputs.">
            ℹ️
        </a>
    """, unsafe_allow_html=True)
    top_p = st.sidebar.slider(" ", 0.0, 1.0, 0.9, 0.1)

    return temperature, top_k, top_p