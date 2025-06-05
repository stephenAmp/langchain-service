from langchain_google_genai import ChatGoogleGenerativeAI;
import os
from dotenv import load_dotenv;

load_dotenv()

def get_llm():
    return ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.7)