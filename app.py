# eBay RAG Chatbot using Streamlit
import streamlit as st
from src.RAG_pipeline import create_rag_chain
from src.vector_db import load_vector_db

# Page config
st.set_page_config(
    page_title="eBay RAG Chatbot",
    page_icon="🚦",
    layout="wide"
)

# Sidebar
st.sidebar.title("📚 eBay Agreement Assistant")
selected_model = st.sidebar.selectbox(
    "Choose LLM",
    ["llama3.2", "mistral", "zephyr", "phi3"],
    index=0
)
st.sidebar.markdown(f"**Embedding:** `nomic-embed-text`")

# Show chunk count
try:
    db = load_vector_db()
    st.sidebar.markdown(f"**Chunks indexed:** {db._collection.count()}")
except:
    st.sidebar.markdown("**Chunks indexed:** N/A")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

# Title
st.title("eBay User Agreement Chatbot")
st.caption("Ask anything about eBay's Terms, Policies, and Legal Agreements")

# Load RAG chain
if st.session_state.rag_chain is None:
    with st.spinner("Loading vector database..."):
        try:
            vector_db = load_vector_db()
            st.session_state.rag_chain = create_rag_chain(vector_db, selected_model)
            st.success("✅ RAG pipeline ready!")
        except Exception as e:
            st.error(f"Vector DB not found. Run: `python preprocess.py`")
            st.stop()

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=msg.get("avatar")):
        st.markdown(msg["content"])
        if "sources" in msg:
            with st.expander("Source Passages"):
                for i, doc in enumerate(msg["sources"]):
                    st.markdown(f"**Relevance Snippet {i+1}:**")
                    st.text(doc.page_content)
                    st.divider()

# User input
if prompt := st.chat_input("Ask about eBay policies..."):
    st.chat_message("user", avatar="👤").markdown(prompt)
    st.session_state.messages.append({
        "role": "user",
        "content": prompt,
        "avatar": "👤"
    })

    # Stream response
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        full_response = ""

        # Get sources
        vector_db = load_vector_db()
        retriever = vector_db.as_retriever(search_kwargs={"k": 3})
        relevant_docs = retriever.invoke(prompt)

        # Stream tokens
        rag_chain = st.session_state.rag_chain
        for chunk in rag_chain.stream({"question": prompt}):
            full_response += chunk
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

        # Save with sources
        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response,
            "avatar": "🤖",
            "sources": relevant_docs
        })