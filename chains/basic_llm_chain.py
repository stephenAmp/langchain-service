# Basic LLM chain
from llms.gemini_llm import get_llm
from langchain.prompts import(
ChatPromptTemplate, # For defining conversation structure 
MessagesPlaceholder # for reserving spot in prompt for injection of memory (chat history)
) 
from langchain_core.messages import HumanMessage, SystemMessage # For assigning role to LLM in prompt
from langchain_core.runnables import  RunnableMap, RunnableSequence # For chaining with langchain components pipe
from langchain_core.runnables.history import RunnableWithMessageHistory # Ties history into chain
import os
from dotenv import load_dotenv
from utils.memory_store import store #  script for handling memory store

load_dotenv()

#  Connecting prompts to LLM
def build_chain():
    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content="You are helpful movie recommendation assistant."),
        MessagesPlaceholder(variable_name="chat_history"),("human","{question}")
    ])

    # Create LLM instance
    llm = get_llm()


   # Properly wrap input dict to message list
    input_mapper = RunnableMap({
        "messages": lambda input: [
            HumanMessage(content=(input["question"] if isinstance(input, dict) and 'question' in input else ""))
        ]
    })


    # Chain without memory
    chain = input_mapper | prompt | llm

    # Wrap with memory from store
    chain_with_memory = RunnableWithMessageHistory(
        chain,
        lambda session_id: store.get_memory(session_id),
        input_messages_key="question",
        history_messages_key="chat_history"
    )

    return chain_with_memory

