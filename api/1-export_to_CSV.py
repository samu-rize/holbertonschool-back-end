#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import requests
from sys import argv

if __name__ == "__main__":
    id = int(argv[1])
    uri = "https://jsonplaceholder.typicode.com"
    data_users = requests.get(f"{uri}/users/{id}").json()
    data_todos = requests.get(f"{uri}/todos?userId={id}").json()

    name = data_users.get("name")
    with open(f'{id}.csv', 'w') as teemo:
        for data in data_todos:
            completed = data["completed"]
            title = data["title"]
            teemo.write(f'"{id}","{name}","{completed}","{title}"\n')
