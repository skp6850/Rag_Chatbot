```markdown
# 🤖 eBay RAG Chatbot – Amlgo Labs Assignment

A ** RAG chatbot** that answers questions about eBay's User Agreement using **Ollama + LangChain + Chroma**.

Built with:
- `llama3` (7B) or other Ollama models
- `nomic-embed-text` for embeddings
- `Chroma` as vector DB
- `Streamlit` UI with **real-time streaming responses**


---

## 🏗️ Architecture Flow

1. **Document Loader** → Extracts text from `AI Training Document.pdf`
2. **Text Splitter** → Chunks into 100–300 word segments
3. **Embedding** → `nomic-embed-text` via Ollama
4. **Vector DB** → Chroma (persistent)
5. **Retriever** → Multi-query expansion for better recall
6. **Generator** → `llama3` with streaming
7. **UI** → Streamlit with real-time response + source passages

---

## 🚀 How to Run

### 1. Prerequisites

- Install [Ollama](https://ollama.com):  
  ```bash
  ollama run llama3
  ```
  Or: `ollama run zephyr`, `ollama run mistral`

- Install Python 3.10+ and `pip`

### 2. Setup

```bash
git clone https://github.com/yourusername/ebay-rag-chatbot.git
cd ebay-rag-chatbot
pip install -r requirements.txt
```

### 3. Add PDF

Place the provided `AI Training Document.pdf` in the `data/` folder:

```
data/
└── AI Training Document.pdf
```

### 4. Run Preprocessing

```bash
python preprocess.py
```

This will:
- Load and clean the PDF
- Split into 100–300 word chunks
- Generate embeddings
- Save to `vectordb/`

### 5. Launch App

```bash
streamlit run app.py
```

✅ The app will open in your browser.

---

## 🧪 Sample Queries

| Query | Expected Answer Snippet |
|------|-------------------------|
| Summary of the policies? | 
| Are vehicles covered under eBay Money Back Guarantee? |
| tell me about the returning policies?|

## 📂 Project Structure

```
rag-chatbot/
├── data/
│   └── AI Training Document.pdf
├── chunks/
│   ├── all_chunks.txt
│   └── chunks.json
├── vectordb/                 # Chroma DB
├── notebooks/
│   └── FAST_rag_notebook.ipynb
├── src/
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── generator.py
│   └── rag_pipeline.py
├── preprocess.py             # One-time preprocessing
├── app.py                    # Streamlit UI
├── requirements.txt
├── README.md
```

> Run Fast_rag_notebook.ipynb file. This file is w/o the UI.
---

## 🎥 Demo

[![Demo Video](https://img.youtube.com/vi/YOUTUBE_ID/0.jpg)](https://youtu.be/L39cFqPAWLU)



> The video shows:
> - App loading and preprocessing
> - Asking: *"Tell me about ebay's returning Policies?"*
> - Streaming response with source passages
> - Model selector and chunk count in sidebar

---

## 🛠 Model & Embedding Choices

| Component | Choice | Justification |
|--------|--------|-------------|
| **LLM** | `llama3.2` | Lightweight, instruction-tuned, good for Q&A |
| **Embedding** | `nomic-embed-text` | Fast, accurate, trained on legal text |
| **Vector DB** | `Chroma` | Persistent, lightweight, easy to use |
| **Retriever** | `MultiQueryRetriever` | Improves recall with query expansion |

---
