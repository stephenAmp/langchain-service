from chains.basic_llm_chain import build_chain;
from utils.langsmith import _init_langsmith
import uuid

def main():
    #load_dotenv() why?
    # _init_langsmith() try it
    chain = build_chain()
    session_id = uuid.uuid4()
    while 2 > 1:
        question = input("Ask a question (or 'exit'): ").strip()
        if question.lower() in ['exit','quit']:
            break
        answer = chain.invoke({"input":question}, config={"configurable":{"session_id":session_id}})
        print("\nAI: ", answer['output'])

if __name__=='__main__':
    main()