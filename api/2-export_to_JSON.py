#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format.

Requirements:

Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
File name must be: USER_ID.json
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    id = int(argv[1])
    uri = "https://jsonplaceholder.typicode.com"
    data_users = requests.get(f"{uri}/users/{id}").json()
    data_todos = requests.get(f"{uri}/todos?userId={id}").json()

    name = data_users.get("username")
    dct = {str(id): []}
    for data in data_todos:
        completed = data["completed"]
        title = data["title"]
        dct[str(id)].append({
            "task": title,
            "completed": completed,
            "username": name
        })
    with open(f'{id}.json', 'w') as teemo:
        json.dump(dct, teemo)
