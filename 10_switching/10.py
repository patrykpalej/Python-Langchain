from langchain.schema import SystemMessage
from langchain_openai.chat_models import ChatOpenAI


chat = ChatOpenAI()
query = "Where Jakub works?"
sources = [
    {"name": "Adam (overment)", "source": "adam.md"},
    {"name": "Jakub (unknow)", "source": "jakub.md"},
    {"name": "Mateusz (MC)", "source": "mateusz.md"}
]

newline = "\n"
source = chat.invoke([SystemMessage(
    f"""Pick one of the following sources related to the query
        and return filename and nothing else. Sources###
        {newline.join([src["name"] + " file: " + src["source"] for src in sources])}
        ###
        Query: {query}\n\n
        Source file name:
    """
)]).content

print(source)
