import json
from datetime import datetime
from langchain.schema import SystemMessage
from langchain_openai.chat_models import ChatOpenAI


def rephrase(response, query):
    model = ChatOpenAI(model_name="gpt-3.5-turbo",
                       temperature=1)
    content = model.invoke([
        SystemMessage(f"""Answer the question ultra-briefly using casual, human-friendly tone:
                          ###{query}###
                          and act as if you just performed this action and confirming this fact to the user, using the following response:
                          ###{json.dumps(response)}###""")]
    )
    return content


def parse_function_call(result):
    if not result.additional_kwargs or 'function_call' not in result.additional_kwargs:
        return None

    function_call = result.additional_kwargs['function_call']
    return {
        'name': function_call['name'],
        'args': json.loads(function_call['arguments'])
    }


def current_date():
    now = datetime.now()

    weekday = now.strftime('%A')
    month = now.strftime('%m')
    day = now.strftime('%d')
    year = now.strftime('%Y')
    hours = now.strftime('%H')
    minutes = now.strftime('%M')

    return f"{weekday}, {month}/{day}/{year} {hours}:{minutes}"
