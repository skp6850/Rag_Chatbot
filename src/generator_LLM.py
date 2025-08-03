# Here we are defining the function to create a generator using ChatOllama from LangChain.
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

# Creating a generator function that uses ChatOllama for text generation and returns a string output parser.
def create_generator(llm_model="llama3"):

    llm = ChatOllama(model=llm_model, temperature=0.3, streaming=True)
    return llm | StrOutputParser()