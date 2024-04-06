import json
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage


query_enrichment_schema = {
    "name": "query_enrichment",
    "description": "Describe users query with semantic tags and classify with type",
    "parameters": {
        "type": "object",
        "properties": {
            "command": {
                "type": "boolean",
                "description": "Set to 'true' when query is direct command for AI. Set to 'false' when queries asks for saying/writing/translating/explaining something and all other."
            },
            "type": {
                "type": "string",
                "description": "memory (queries about the user and/or AI), notes|links (queries about user's notes|links). By default pick 'memory'.",
                "enum": ["memory", "notes", "links"]
            },
            "tags": {
                "type": "array",
                "description": "Multiple semantic tags/keywords that enriches query for search purposes (similar words, meanings). When query refers to the user, add 'overment' tag, and when refers to 'you' add tag 'Alice'",
                "items": {
                    "type": "string"
                }
            }
        },
        "required": [
            "type", "tags", "command"
        ]
    }
}

model = ChatOpenAI(model="gpt-4-0613").bind(
    functions=[query_enrichment_schema],
    function_call={"name": "query_enrichment"})

print({
    "functions": [query_enrichment_schema],
    "function_call": {"name": "query_enrichment"}
}, "\n\n")

result = model.invoke([HumanMessage("Hey there!")])


def parse_function_call(result):
    if not result.additional_kwargs or 'function_call' not in result.additional_kwargs:
        return None
    return {
        'name': result.additional_kwargs['function_call']['name'],
        'args': json.loads(result.additional_kwargs['function_call']['arguments'])
    }


action = parse_function_call(result)
if action:
    print(action['name'], action['args'])
