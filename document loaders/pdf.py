from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import TokenTextSplitter

data=PyPDFLoader(r"D:\AI Engineer\Gen AI\Part-02\RAG Project\document loaders\MTA.pdf")

splitter=TokenTextSplitter(
    chunk_size=500,
    chunk_overlap=10
)


docs=data.load()
chunks=splitter.split_documents(docs)
print(len(chunks))
