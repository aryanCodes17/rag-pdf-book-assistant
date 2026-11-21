from dotenv import load_dotenv  
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate

data=TextLoader(r"D:\AI Engineer\Gen AI\Part-02\RAG Project\document loaders\long-doc.txt",encoding="utf-8")
docs=data.load()

template=ChatPromptTemplate.from_messages([
    ('system','you are an AI the summarizes the text'),
    ('human','{data}')
])

model =ChatGroq(model="openai/gpt-oss-120b")

prompt=template.format_messages(data=docs[0].page_content)

result=model.invoke(prompt)
print(result.content)