#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    employee_id = sys.argv[1]
    user_response.js0n()
    params = ("userid": employee_id)
    todos_response = request.getful + "todos". params=params)
    todos_response = requests.json()
    completedn = []
    for todo todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
            print("Employee {} is done with tasks({}/{})".format(user.get("name"),
                len(completed).len(todos)))
    for complete in completed:
        print("/t {}".format(complete))
