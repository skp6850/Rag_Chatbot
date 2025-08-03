# Here we are defining the function to create a retriever using MultiQueryRetriever from LangChain.
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# This function creates a retriever that generates multiple query variations
def create_retriever(vector_db, llm_model="llama3"):

    llm = ChatOllama(model=llm_model, temperature=0.3)

    # Define the prompt template for generating query variations
    # We are using MultiQueryRetriever to generate 3 different versions of the user's question
    # so that we can improve retrieval by capturing semantic variations.
    # This is a key step in enhancing the retrieval process.
    QUERY_PROMPT = PromptTemplate.from_template("""
You are an AI assistant helping retrieve relevant documents.
Generate exactly 3 different versions of the user's question to improve retrieval.
Focus on semantic variations, synonyms, and rephrasing.

Original question: {question}

Provide each variant on a new line.
    """)

    retriever = MultiQueryRetriever.from_llm(
        retriever=vector_db.as_retriever(search_kwargs={"k": 3}),
        llm=llm,
        prompt=QUERY_PROMPT
    )
    return retriever