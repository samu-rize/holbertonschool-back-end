#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json
"""
from json import dump
from requests import get

if __name__ == "__main__":
    uri = "https://jsonplaceholder.typicode.com"
    data_users = get(f"{uri}/users").json()
    dct = {}

    for user in data_users:
        user_id = user["id"]
        name = user["username"]
        data_todos = get(f"{uri}/todos?userId={user_id}").json()
        todo_list = []

        for data in data_todos:
            completed = data["completed"]
            title = data["title"]
            todo_list.append({
                "username": name,
                "task": title,
                "completed": completed,
            })
        dct[user_id] = todo_list
    with open('todo_all_employees.json', 'w') as teemo:
        dump(dct, teemo)
