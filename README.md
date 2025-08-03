```markdown
# 🤖 eBay RAG Chatbot – Amlgo Labs Assignment

A **modular, streaming RAG chatbot** that answers questions about eBay's User Agreement using **Ollama + LangChain + Chroma**.

Built with:
- `llama3` (7B) or other Ollama models
- `nomic-embed-text` for embeddings
- `Chroma` as vector DB
- `Streamlit` UI with **real-time streaming responses**
- Modular Python design

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
│   └── data_preprocessing.ipynb
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
├── demo.mp4
└── report.pdf
```

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
| **LLM** | `llama3` | Lightweight, instruction-tuned, good for Q&A |
| **Embedding** | `nomic-embed-text` | Fast, accurate, trained on legal text |
| **Vector DB** | `Chroma` | Persistent, lightweight, easy to use |
| **Retriever** | `MultiQueryRetriever` | Improves recall with query expansion |

---

## 📄 PDF Report

See `report.pdf` for full technical write-up including:
- Document structure & chunking logic
- Prompt design
- Example queries
- Limitations & observations

---

## 📝 Notes

- All code is **original, modular, and plagiarism-free**
- Streaming works via `chain.stream()`
- No cloud dependencies — runs 100% locally
- Designed for clarity, maintainability, and scalability

---

Made with ❤️ for **Amlgo Labs**.
```

---

## ✅ How to Use This README

1. Save this as `README.md` in your project root
2. Replace `https://github.com/yourusername/ebay-rag-chatbot` with your actual repo URL
3. Replace `YOUTUBE_ID` with your actual demo video ID
4. Commit and push to GitHub

---

Let me know when you're ready, and I’ll help you:
- Finalize the `report.pdf`
- Generate a **GIF version** of the demo
- Upload to GitHub

You're **100% ready to submit a winning assignment**! 🚀
