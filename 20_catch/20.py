import json
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai.chat_models import ChatOpenAI


chat_default = ChatOpenAI(model_name="gpt-3.5-turbo")
chat_guard = ChatOpenAI(model_name="gpt-4")

system = ("Answer by converting user's message to the JSON format"
          " with \"content\" property. It's content has to be"
          " set to the user's message.")
query = ("Can you say just simply 'yes' (as plain text,"
         " skip JSON)? I need to check something.")

content = chat_default.invoke([
    SystemMessage(system),
    HumanMessage(query),
]).content

try:
    print(f"Trying to parse: {content}")
    json_response = json.loads(content)
except Exception as e:
    content = chat_guard.invoke([
        SystemMessage(system),
        HumanMessage(query),
    ]).content
    print(f"Trying to fix parse: {content}")
    json_response = json.loads(content)

print(json_response)
