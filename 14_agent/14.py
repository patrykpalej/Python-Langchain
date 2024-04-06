from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from schema import add_schema, multiply_schema, subtract_schema
from helper import parse_function_call


model = ChatOpenAI(model_name="gpt-4-0613").bind(
    functions=[add_schema, multiply_schema, subtract_schema]
)

result = model.invoke([HumanMessage("2929590 + 129359")])

tools = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b
}

action = parse_function_call(result)
if action and tools[action["name"]]:
    result = tools[action["name"]](action["args"]["first"],
                                   action["args"]["second"])
    print(f"The result is {result}")
else:
    print(result.content)
