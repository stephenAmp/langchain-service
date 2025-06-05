# LangSmith Tracing
import os;
from langchain_core.tracers import LangChainTracer
from dotenv import load_dotenv

load_dotenv()

def _init_langsmith():
    os.environ['LANGCHAIN_TRACING_V2'] = "true"
    api_key = os.getenv('LANGCHIAN_API_KEY')
    if not api_key:
        raise ValueError('LANGCHAIN_API_KEY  not found in .env')
    os.environ['LANGCHAIN_API_KEY'] = api_key
    os.environ["LANGCHAIN_PROJECT"] = "langchain-qa"

