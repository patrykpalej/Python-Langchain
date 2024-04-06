get_tasks_schema = {
    "name": "get_tasks",
    "description": "Get (unfinished) tasks from Todoist",
    "parameters": {
        "type": "object",
        "properties": {}
    }
}

add_tasks_schema = {
    "name": "add_tasks",
    "description": "Add multiple tasks to Todoist",
    "parameters": {
        "type": "object",
        "properties": {
            "tasks": {
                "type": "array",
                "description": "List of tasks that needs to be added to the Todoist",
                "items": {
                    "type": "object",
                    "properties": {
                        "content": {
                            "type": "string",
                            "description": "Format: task description"
                        },
                        "due_string": {
                            "type": "string",
                        }
                    }
                }
            }
        }
    }
}

finish_tasks_schema = {
    "name": "close_tasks",
    "description": "Finish/Complete tasks in Todoist",
    "parameters": {
        "type": "object",
        "properties": {
            "tasks": {
                "type": "array",
                "description": "List of IDs of tasks that needs to be finished/completed",
                "items": {
                    "type": "number",
                }
            }
        }
    }
}

update_tasks_schema = {
    "name": "update_tasks",
    "description": "Update multiple tasks in Todoist based on the current tasks mentioned in the conversation",
    "parameters": {
        "type": "object",
        "properties": {
            "tasks": {
                "type": "array",
                "description": "List of tasks that needs to be updated in the Todoist",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "number",
                            "description": "ID of the task to update"
                        },
                        "content": {
                            "type": "string",
                            "description": "Format: task description"
                        },
                        "due_string": {
                            "type": "string",
                        }
                    }
                }
            }
        }
    }
}