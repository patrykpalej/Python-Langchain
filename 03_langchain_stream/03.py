from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.callbacks import StdOutCallbackHandler


class MyCustomHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        print(f"My custom handler, token: {token}")


chat = ChatOpenAI(streaming=True, callbacks=[MyCustomHandler])

messages = [HumanMessage("Hey there!")]
response = chat.invoke(messages)
