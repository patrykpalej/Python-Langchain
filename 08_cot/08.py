from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


chat = ChatOpenAI(model_name="gpt-4")
zero_shot = chat.invoke([
    SystemMessage("Answer the question ultra-briefly"),
    HumanMessage("48*62-9")]).content

cot = chat.invoke([
    SystemMessage(
        """Take a deep breath and answer the question
            by carefully explaining your logic step by step.
            Then add the separator: ### and answer the question 
            ultra-briefly with a single number:"""),
    HumanMessage("48*62-9")
]).content

if isinstance(cot, str) and isinstance(zero_shot, str):
    cot = cot.split("\n###")[1]
    print(f"Zero shot: {zero_shot} | {'passed' if zero_shot == '2967' else 'failed'}")
    print(f"Chain of thought: {cot} | {'passed' if cot == '2967' else 'failed'}")
