from langchain.memory import ConversationBufferWindowMemory
from langchain.chains.conversation.base import ConversationChain
from langchain_openai import OpenAI


chat = OpenAI()
memory = ConversationBufferWindowMemory(k=1)
chain = ConversationChain(llm=chat, memory=memory)

response1 = chain.invoke({"input": "Hey there! I'm Adam"})["response"]
print("AI", response1)

response2 = chain.invoke({"input": "Hold on."})["response"]
print("AI", response2)

response3 = chain.invoke({"input": "Do you know my name?"})["response"]
print("AI", response3)
