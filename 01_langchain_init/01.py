import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
response = chat.invoke("Hey there!")
print(response.content)
