import json


def parse_function_call(result):
    if not result.additional_kwargs or 'function_call' not in result.additional_kwargs:
        return None

    function_call = result.additional_kwargs['function_call']
    return {
        'name': function_call['name'],
        'args': json.loads(function_call['arguments'])
    }
