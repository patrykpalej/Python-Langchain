from langchain_openai import ChatOpenAI


chat = ChatOpenAI()
response = chat.invoke("Hey there!")
print(response.content)
