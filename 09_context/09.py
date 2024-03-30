from langchain.document_loaders.text import TextLoader
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai.chat_models import ChatOpenAI


loader = TextLoader("09_context/memory.md")
doc = loader.load()[0]
chat = ChatOpenAI()
response = chat.invoke([
    SystemMessage(
        f"""Answer questions as truthfully using the context 
            below and nothing more. If you don't know the answer,
            say "don't know".
            context###{doc.page_content}###"""),
    HumanMessage("Who is overment?")
]).content

print(response)
