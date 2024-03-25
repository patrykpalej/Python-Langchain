import os
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate

from _02_context import context


system_template = """
As a {role} who answers the questions ultra-concisely using CONTEXT below 
and nothing more and truthfully says "don't know" when the CONTEXT is not enough to give an answer.

context###{context}###
"""
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages(
    [("system", system_template),
     ("human", human_template)])

formatted_chat_prompt = chat_prompt.format_messages(
    context=context,
    role="Senior JavaScript Programmer",
    text="What is Vercel AI?")

chat = ChatOpenAI()
response = chat.invoke(formatted_chat_prompt)
print(response.content)
