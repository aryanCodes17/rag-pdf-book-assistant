# 📚 RAG-Based PDF Book Assistant

A PDF-based question-answering application built using **Python, LangChain, ChromaDB, HuggingFace, and Groq**. Upload a PDF book, ask questions about its content, and get answers based on the information in the document.

## 🚀 Features

- **PDF Upload:** Upload PDF books through a Streamlit interface.
- **Text Splitting:** Split documents into smaller chunks with overlapping text.
- **Text Embeddings:** Use HuggingFace's `BAAI/bge-small-en-v1.5` model to convert text into embeddings.
- **Vector Database:** Store document embeddings in ChromaDB.
- **MMR Retrieval:** Find relevant text chunks while reducing repeated information.
- **AI-Powered Answers:** Use Groq's GPT-OSS-120B model to generate answers from retrieved document content.
- **Context-Based Responses:** Instruct the LLM to answer using the provided document context.

## ⚙️ How It Works

The application follows a Retrieval-Augmented Generation (RAG) workflow.

```text
          Upload PDF
              |
              v
        Extract Text
              |
              v
        Split into Chunks
              |
              v
      Generate Embeddings
              |
              v
       Store in ChromaDB
              |
              v
        User Asks Question
              |
              v
       MMR-Based Retrieval
              |
              v
      Retrieve Relevant Text
              |
              v
      Send Context to Groq
              |
              v
        Generate Answer
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| LangChain | Document processing and RAG workflow |
| ChromaDB | Store and search document embeddings |
| HuggingFace | Generate text embeddings |
| BAAI/bge-small-en-v1.5 | Embedding model |
| Groq | Run the LLM |
| GPT-OSS-120B | Generate answers |
| Streamlit | Build the user interface |
| PyPDFLoader | Load PDF documents |

## 📂 Project Structure

```text
RAG Project/
│
├── app.py
├── main3.py
├── create_database.py
├── requirements.txt
│
├── document loaders/
│   ├── page.py
│   ├── pdf.py
│   ├── test.py
│   └── long-doc.txt
│
├── retrievers/
│   ├── arixv.py
│   ├── mmr.py
│   └── multiquery.py
│
├── vector store/
│   └── DB.py
│
├── chroma_db/          # Created locally
├── .env                # API keys (not uploaded)
└── .gitignore
```

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/aryanCodes17/rag-pdf-book-assistant.git

cd rag-pdf-book-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Create a `.env` file in the project folder:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/).

**Note:** Never upload your `.env` file or share your API key publicly.

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Then:

1. Open the local URL shown in your terminal.
2. Upload a PDF book.
3. Click **Create Vector Database**.
4. Wait for the document processing to finish.
5. Enter a question about the uploaded book.
6. Get an answer based on the document content.

## 🧪 Additional Experiments

The project also includes separate scripts to explore different LangChain features:

- **Similarity Search:** Retrieve documents based on their similarity to a query.
- **MMR Retrieval:** Retrieve relevant documents while reducing repeated results.
- **MultiQuery Retrieval:** Generate different versions of a query to search for relevant documents.
- **Arxiv Search:** Search for research papers using the Arxiv API.
- **Document Summarisation:** Summarise text and PDF content using Groq.

These are separate experiments and are not all part of the main Streamlit application.

## 🔮 Future Improvements

- Add page numbers and source references to answers.
- Support multiple PDF uploads.
- Improve document search and retrieval.
- Add chat history for follow-up questions.
- Deploy the application online.

## 👨‍💻 Author

**Aman Aryan**

[GitHub](https://github.com/aryanCodes17)

---

⭐ If you find this project useful, consider giving the repository a star.