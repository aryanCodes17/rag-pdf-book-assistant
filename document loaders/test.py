from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import CharacterTextSplitter  
splitter=CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1
)

data=TextLoader("D:\AI Engineer\Gen AI\Part-02\RAG Project\document loaders\long-doc.txt")
docs=data.load()

chunks=splitter.split_documents(docs)
for i in chunks:
    print(i.page_content)
    print()
    print()
    print()