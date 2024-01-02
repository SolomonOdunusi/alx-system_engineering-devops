#!/usr/bin/python3
"""Extend your python to export to Json"""
import json
import requests
from sys import argv


def export_to_json(user_id):
    """export to json"""
    # get the info of the users and tasks by his id in dict format
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
                user_id)).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                            user_id)).json()

    # create and open a file and fill with the info below
    file_name = "{}.json".format(user_id)
    with open(file_name, mode='w') as jsonfile:
        json.dump({user_id: [{
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": users.get('username')
        } for todo in todos]}, jsonfile)


if __name__ == "__main__":
    export_to_json(argv[1])
