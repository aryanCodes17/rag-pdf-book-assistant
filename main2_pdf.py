from dotenv import load_dotenv  
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

data=PyPDFLoader(r"D:\AI Engineer\Gen AI\Part-02\RAG Project\document loaders\algebra_book.pdf")
docs=data.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=splitter.split_documents(docs)

template=ChatPromptTemplate.from_messages([
    ('system','you are an AI the summarizes the text'),
    ('human','{data}')
])

model =ChatGroq(model="openai/gpt-oss-120b")

prompt=template.format_messages(data=docs[45].page_content)

result=model.invoke(prompt)
print(result.content)