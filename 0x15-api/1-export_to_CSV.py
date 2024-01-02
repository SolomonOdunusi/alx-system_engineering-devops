#!/usr/bin/python3
""" Extend your Python script to export data in the CSV format."""
import csv
import requests
from sys import argv

def export_csv(user_id):
    """export data in the CSV format"""
    # get the info of the users and tasks by his id in dict format
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
                user_id)).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                            user_id)).json()

    # create and open a file and fill with the info below
    file_name = "{}.csv".format(user_id)
    with open(file_name, mode='w') as csvfile:
        content = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            content.writerow(
                [user_id,
                    users.get('username'),
                    todo.get('completed'),
                    todo.get('title')])

if __name__ == "__main__":
    export_csv(argv[1])
