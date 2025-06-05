# Basic LLM chain
from llms.gemini_llm import get_llm
from langchain.prompts import PromptTemplate;
import os
from dotenv import load_dotenv

load_dotenv()

#  Connecting prompts to LLM
def build_chain():
    prompt = PromptTemplate(input_variables=['question'], template=open('prompts/prompt_template.txt','r').read())

    # Create LLM instance
    llm = get_llm()
    return prompt | llm

# # Create prompt template
# prompt = PromptTemplate(
#     input_variables=['question'],
#     template='Answer the following question:\n{question}'
# )

# # Define chain using runnable sequence
# chain = prompt | llm

# # Run prompt
# def response(question):
#     return chain.invoke({'question':question})

