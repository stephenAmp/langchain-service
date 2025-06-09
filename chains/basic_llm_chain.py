
from llms.gemini_llm import get_llm
from langchain.prompts import (
    ChatPromptTemplate, 
    MessagesPlaceholder
)
from chains.retriever_tool import create_movie_retriever_tool
from langchain.agents import initialize_agent, AgentType
from langchain_core.runnables.history import RunnableWithMessageHistory
import os
from dotenv import load_dotenv
from utils.memory_store import store # The updated script for handling memory

load_dotenv()

#  Connecting prompts to LLM
def build_chain():
    """
    Builds a LangChain runnable that includes chat history management.
    """
    # Define the prompt template for the conversation.
    # It includes a system message to set the AI's role, a placeholder for chat history,
    # and a placeholder for the user's current question.
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful movie recommendation assistant."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}")
    ])

    # Create an instance of the language model.
    llm = get_llm()

    # Create the main chain by piping the prompt to the language model.
    # The input to this chain is expected to be a dictionary containing 'question' and 'chat_history'.
    chain = prompt | llm


    # Creating agent with retriever tools and LLM
    movie_retriever_tool = create_movie_retriever_tool()
    agent = initialize_agent(
        tools=[movie_retriever_tool],
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        agent_kwargs={
            "system_message":"You are a movie recommendation assistant in an app"
        }
    )
    # Wrap the base chain with RunnableWithMessageHistory to add memory.
    # This runnable automatically manages loading history for a session and saving new messages.
    agent_with_memory = RunnableWithMessageHistory(
        agent,
        # The factory function to get the history object for a given session_id.
        # It now correctly retrieves the ChatMessageHistory object from our store.
        lambda session_id: store.get_history(session_id),
        # The key in the input dictionary that contains the user's message.
        input_messages_key="input",
        # The key in the prompt template where the history should be injected.
        history_messages_key="chat_history"
    )

    return agent_with_memory
