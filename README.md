<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1a2e,50:16213e,100:0f3460&height=200&section=header&text=Chat%20with%20PDF%20🗂️&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=RAG-powered%20PDF%20Chatbot%20using%20LangChain%20%2B%20Gemini%20API&descAlignY=58&descSize=16" />

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_API-4285F4?style=for-the-badge&logo=google&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B35?style=for-the-badge&logo=databricks&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

</div>

---

## 📌 What is this?

**Chat with PDF** is an AI-powered document chatbot that lets you upload any PDF and ask questions about it in plain English — and get accurate, grounded answers instantly.

No more manually searching through 100-page documents. Just ask.

> **Built using RAG (Retrieval Augmented Generation)** — one of the most in-demand GenAI patterns in the industry today.

---

## 🎬 Demo

> Upload a PDF → Ask a question → Get a grounded answer

```
User:  "What are the key findings of this research paper?"
Bot:   "Based on the document, the key findings are..."

User:  "What is the methodology used?"
Bot:   "The paper describes a methodology involving..."

User:  "Who are the authors?"
Bot:   "I could not find this in the PDF."  ← Honest! No hallucination.
```

---

## 🧠 How it works — RAG Pipeline

```
📄 PDF Upload
     ↓
📖 Text Extraction       (PyPDF2)
     ↓
✂️  Text Chunking         (RecursiveCharacterTextSplitter — 1000 chars, 200 overlap)
     ↓
🔢 Embeddings             (Gemini embedding-001 model)
     ↓
🗃️  Vector Store           (ChromaDB — stores semantic vectors)
     ↓
❓ User Question
     ↓
🔍 Similarity Search      (Top 4 relevant chunks retrieved)
     ↓
🤖 LLM Answer             (Gemini Pro — grounded to PDF context)
     ↓
💬 Answer displayed in Streamlit chat UI
```

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Language | Python 3.10+ | Core programming |
| LLM | Gemini Pro (Google) | Answer generation |
| Embeddings | Gemini embedding-001 | Text vectorization |
| Orchestration | LangChain | RAG pipeline management |
| Vector DB | ChromaDB | Semantic search storage |
| PDF Parsing | PyPDF2 | Text extraction |
| UI | Streamlit | Web interface |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Yashreddy05/chat-with-pdf.git
cd chat-with-pdf
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Get your Gemini API key

Go to [aistudio.google.com](https://aistudio.google.com) → Get API Key → Copy it

### 4. Create a `.env` file

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 5. Run the app

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 📁 Project Structure

```
chat-with-pdf/
│
├── app.py                  # Main Streamlit application
├── .env                    # API key (not pushed to GitHub)
├── .gitignore              # Excludes .env and chroma_db
├── requirements.txt        # All dependencies
└── README.md               # You are here
```

---

## 📦 Requirements

```txt
streamlit
langchain
langchain-google-genai
langchain-community
chromadb
pypdf2
python-dotenv
```

---

## ✨ Key Features

- 📄 Upload any PDF document
- 💬 Natural language Q&A interface
- 🔍 Semantic search — finds meaning, not just keywords
- 🛡️ Hallucination prevention via custom prompt engineering
- 🧠 Context-aware answers grounded to your document
- ⚡ Fast responses using chunked retrieval

---

## 🔍 What I Learned

- How **RAG (Retrieval Augmented Generation)** works end to end
- How to convert text into **vector embeddings** using Gemini
- How **ChromaDB** stores and retrieves semantic vectors
- How to use **LangChain's RetrievalQA chain** to orchestrate LLM pipelines
- How to write **prompt templates** that prevent hallucination
- How to build and deploy AI apps with **Streamlit**

---

## 🚧 Future Improvements

- [ ] Support multiple PDF uploads at once
- [ ] Add document summarization feature
- [ ] Deploy to Streamlit Cloud
- [ ] Add support for scanned PDFs (OCR)
- [ ] Chat history export

---

## 👨‍💻 Author

**Yashwanth Reddy**
- GitHub: [@Yashreddy05](https://github.com/Yashreddy05)
- LinkedIn: [yashwanth-reddyy05](https://www.linkedin.com/in/yashwanth-reddyy05)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f3460,50:16213e,100:1a1a2e&height=100&section=footer"/>

⭐ If this project helped you understand RAG, please give it a star!

</div>
