#!/usr/bin/python3
"""Employee TODO list progress"""
import requests
from requests.exceptions import RequestException
from sys import argv, exit


def get_employee_todo_progress(emp_id):
    """Get and display the employee TODO list progress"""
    # API URL for the given employee ID
    url_user = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    url_todos = f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}'

    try:

        # Make GET requests to the APIs
        resp_user = requests.get(url_user)
        resp_todos = requests.get(url_todos)

        # Check if the requests were successful (status code 200)
        resp_user.raise_for_status()
        resp_todos.raise_for_status()

        # Parse the JSON responses
        user = resp_user.json()
        todos = resp_todos.json()

        # Extract employee information
        employee_name = user.get('name', f"Employee {employee_id}")

        # Count completed and total tasks
        completed_tasks = [task for task in todos if task['completed']]
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todos)

        # Display employee todo list progress
        print("Employee {} is done with tasks({}/{}):". format(
            employee_name, number_of_done_tasks, total_number_of_tasks))

        # Display titles of completed tasks
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)

    # Get the employee ID from the command-line argument
    employee_id = int(argv[1])

    # Call the function to get and display the employee TODO list progress
    get_employee_todo_progress(employee_id)
