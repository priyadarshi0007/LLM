from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

def initialize_rag_pipeline(text_content):
    """
    Initializes RAG pipeline by splitting, embedding, and setting up a retriever.

    Args:
        text_content (str): Combined text content extracted from .vtt file.

    Returns:
        retriever: LangChain retriever for querying the text chunks.
    """
    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(text_content)

    # Embed and store in Chroma
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_texts(chunks, embeddings)

    # Return retriever
    return vectorstore.as_retriever()