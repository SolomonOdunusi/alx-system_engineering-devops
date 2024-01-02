#!/usr/bin/python3
"""
Get data from an API
on an employee's tasks
"""
import requests
from sys import argv


def gather_data_from_api(employee_id):
    """Get employee's tasks(data) from API"""
    EMPLOYEE_NAME = ""
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    # get the employee name by his id
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    for user in users:
        if user['id'] == int(employee_id):
            EMPLOYEE_NAME = user['name']
            break

    # get the necessary information of the todo api
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for todo in todos:
        if todo['userId'] == int(employee_id):
            if todo['completed'] is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(todo['title'])
            TOTAL_NUMBER_OF_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME,
        NUMBER_OF_DONE_TASKS,
        TOTAL_NUMBER_OF_TASKS))

    for quote in TASK_TITLE:
        print("\t {}".format(quote))


if __name__ == "__main__":
    gather_data_from_api(argv[1])
