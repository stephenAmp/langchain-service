from chains.basic_llm_chain import build_chain;
from utils.langsmith import _init_langsmith

def main():
    #load_dotenv() why?
    # _init_langsmith() try it
    chain = build_chain()
    while 2 > 1:
        question = input("Ask a question (or 'exit'): ").strip()
        if question.lower() in ['exit','quit']:
            break
        answer = chain.invoke({"question":question})
        print("Answer: ", answer.content)

if __name__=='__main__':
    main()