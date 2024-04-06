from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from helper import current_date, parse_function_call, rephrase
from todoist import add_tasks, close_tasks, list_uncompleted, update_tasks
from schema import add_tasks_schema, finish_tasks_schema, get_tasks_schema, update_tasks_schema


model = ChatOpenAI(model_name="gpt-4-turbo-preview").bind(
    functions=[get_tasks_schema, add_tasks_schema, finish_tasks_schema, update_tasks_schema]
)

tools = {"get_tasks": list_uncompleted, "add_tasks": add_tasks,
         "close_tasks": close_tasks, "update_tasks": update_tasks}


def act(query):
    tasks = list_uncompleted(None)
    current_tasks = ', '.join([task["content"] + "(ID: " + task["id"] + ")"
                               for task in tasks])
    model_response = model.invoke([
        SystemMessage(f"""
        Fact: Today is {current_date()}
        Current tasks: ###{current_tasks}###
        """),
        HumanMessage(query)
    ])
    action = parse_function_call(model_response)
    if action:
        print(f"action: {action['name']}")
        response = tools[action["name"]](action["args"].get("tasks"))
        response = rephrase(response, query)
    else:
        response = model_response.content

    print(f"AI: {response}\n")
    return response


act('I need to write a newsletter about gpt-4 on Monday, can you add it?')
act('Need to buy milk, add it to my tasks')
act('Ouh I forgot! Beside milk I need to buy sugar. Update my tasks please.')
act('Get my tasks again.')
