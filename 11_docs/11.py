import json
from langchain.document_loaders.text import TextLoader
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.documents import Document
from langchain.schema import HumanMessage, SystemMessage

loader = TextLoader("11_docs/docs.md")
doc = loader.load()[0]

documents = [Document(content)
             for content in doc.page_content.split("\n\n")]

model = ChatOpenAI()

keywords = []
for doc in documents:
    keywords.append(model.invoke([
        SystemMessage("""
            Describe the following document with one of the following keywords:
            Mateusz, Jakub, Adam. Return the keyword and nothing else."""),
        HumanMessage(
            f"Document: {doc.page_content}"
        )
    ]).content)

for doc, kw in zip(documents, keywords):
    doc.metadata = {"source": kw}

with open("11_docs/docs_python.json", "w") as f:
    json.dump([dict(doc) for doc in documents], f, indent=4)
