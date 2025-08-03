# Here we are defining the function to create a RAG (Retrieval-Augmented Generation) chain using LangChain.
# Generator and retriever are combined to create a complete RAG pipeline.
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from src.query_retriever import create_retriever
from src.generator_LLM import create_generator

# Function to create a RAG chain using LangChain
def create_rag_chain(vector_db, llm_model="llama3"):

    retriever = create_retriever(vector_db, llm_model)
    generator = create_generator(llm_model)

    prompt = ChatPromptTemplate.from_template("""
You are an AI assistant answering questions about eBay's User Agreement.
Answer **only** based on the following context.
If the answer isn't in the context, say 'I don't know based on the provided document.'

Context:
{context}

Question:
{question}

Answer:
    """)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | generator
    )
    return rag_chain