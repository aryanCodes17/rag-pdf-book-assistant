#load pdf
#split into chunks
#create the embeddings
#store into chroma

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

data=PyPDFLoader(r"D:\AI Engineer\Gen AI\Part-02\RAG Project\document loaders\algebra_book.pdf")
docs=data.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=splitter.split_documents(docs)


embedding_model=HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

vectorstore=Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

