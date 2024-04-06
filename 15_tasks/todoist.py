import requests
import os


def api_call(endpoint='/me', method='GET', body=None):
    if body is None:
        body = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.environ["TODOIST_API_KEY"]}'
    }
    url = f'https://api.todoist.com/rest/v2{endpoint}'
    try:
        if method == 'POST':
            response = requests.post(url, headers=headers, json=body)
        else:
            response = requests.get(url, headers=headers)
        return True if response.status_code == 204 else response.json()
    except Exception as err:
        print(err)


def list_uncompleted(_):
    uncompleted = api_call('/tasks', 'GET')
    return [
        {
            'id': task['id'],
            'content': task['content'],
            'due': task['due']['string'] if task.get('due') else None
        } for task in uncompleted if task
    ]


def add_tasks(tasks):
    added_tasks = [api_call('/tasks', 'POST', {
        'content': task['content'],
        'due_string': task.get('due_string')
    }) for task in tasks]

    return [
        {
            'id': added_task['id'],
            'content': added_task['content'],
            'due_string': added_task.get('due', {}).get('string'),
        } for added_task in added_tasks
    ]


def update_tasks(tasks):
    updated_tasks = [api_call(f'/tasks/{task["id"]}', 'POST', {
        'content': task['content'],
        'due_string': task.get('due_string'),
        'is_completed': task.get('is_completed')
    }) for task in tasks]

    return [
        {
            'id': updated_task['id'],
            'content': updated_task['content'],
            'due_string': updated_task.get('due', {}).get('string'),
        } for updated_task in updated_tasks
    ]


def close_tasks(task_ids):
    closed_tasks = [api_call(f'/tasks/{task_id}/close', 'POST') for task_id in task_ids]

    try:
        return [{str(closed_task): 'completed'}
                for closed_task in closed_tasks]
    except Exception as e:
        return 'No tasks were closed (maybe they were already closed)'
