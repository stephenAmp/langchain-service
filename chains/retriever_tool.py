from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.tools.retriever import create_retriever_tool
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

from data.movies_db import get_movie_data

def create_movie_retriever_tool():
    """
    Creates a retriever tool for a movie database.

    This function performs the core RAG setup:
    1. Loads movie data.
    2. Converts the data into LangChain Document objects.
    3. Generates numerical embeddings for each document's content.
    4. Stores the documents and their embeddings in a FAISS vector store.
    5. Creates a retriever from the vector store.
    6. Creates a tool from the retriever that an agent can use.

    Returns:
        A LangChain tool that can retrieve movie information.
    """
    # 1. Load the movie data from our source file.
    movies = get_movie_data()

    # 2. Convert the raw data into LangChain's Document format.
    # We create a single content string for each movie that the LLM can search through.
    # The 'metadata' dictionary holds the structured data we want to keep.
    documents = [
        Document(
            page_content=f"{movie['title']}: {movie['description']}",
            metadata={
                "title": movie["title"],
                "genre": movie["genre"],
                "year": movie["year"]
            }
        )
        for movie in movies
    ]

    # 3. Initialize the embedding model.
    # This model will convert our text (page_content) into vectors (lists of numbers).
    # We'll use Google's embedding model, which is configured via environment variables.
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # 4. Create the FAISS vector store.
    # 'from_documents' is a factory method that handles the embedding and indexing process for us.
    # This creates a searchable index of our movie documents.
    vector_store = FAISS.from_documents(documents, embeddings)

    # 5. Create a retriever from the vector store.
    # A retriever is a component that knows how to fetch documents from a store based on a query.
    # 'k=2' means it will retrieve the top 2 most relevant documents for any given query.
    retriever = vector_store.as_retriever(k=2)
    
    # 6. Create a tool from the retriever.
    # This wraps the retriever in a Tool object that the LangChain Agent can understand and use.
    # We give it a name and a clear description so the agent knows when to use this tool.
    tool = create_retriever_tool(
        retriever,
        "movie_database_retriever",
        "Searches and returns information about movies from a database. Use it for any questions about movie recommendations, plots, genres, or years."
    )

    return tool
