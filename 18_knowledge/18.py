from langchain.document_loaders.text import TextLoader
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai.chat_models import ChatOpenAI
from search import search_docs
from langchain_core.documents import Document


loader = TextLoader("18_knowledge/knowledge.md")
doc = loader.load()[0]
documents = [Document(page_content=content)
             for content in doc.page_content.split("\n\n")]

query = "Can you write me a function that will generate random number in range for easy_?"
filtered = search_docs(documents, query.split(" "))

chat = ChatOpenAI()
content = chat.invoke([SystemMessage("""
    Answer questions as truthfully using the context below and nothing more. If you don't know the answer, say "don't know"
    
    context###{}###""".format(
    "\n\n".join([doc.page_content for doc in filtered]))),
    HumanMessage(query)]).content

print(content)
