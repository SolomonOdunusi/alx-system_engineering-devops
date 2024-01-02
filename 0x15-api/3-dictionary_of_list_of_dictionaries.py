#!/usr/bin/python3
"""
Extend your Python script to export data in the JSON format
and record all tasks from all employees
"""
import json
import requests


def export_all_to_json():
    """export all to json"""
    # get the info of the users and tasks by his id in dict format
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    # create and open a file and fill with the info below
    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as jsonfile:
        json.dump(
            {user.get('id'): [
                {
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": user.get('username')
                }
                for todo in todos if user.get('id') == todo.get('userId')
            ] for user in users
            },
            jsonfile
        )


if __name__ == "__main__":
    export_all_to_json()
