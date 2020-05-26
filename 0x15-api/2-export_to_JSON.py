#!/usr/bin/python3
""" Module that exports data in the JSON format """
import json
import requests
from sys import argv
import urllib.request


def main():
    """ Method that records all tasks that are owned by employee """
    url = 'https://jsonplaceholder.typicode.com'
    user = '{}/users/{}'.format(url, argv[1])
    todos = '{}/todos/?userId={}'.format(url, argv[1])

    # GET info from URLs
    res = requests.get(user)
    info = res.json()
    tasks = requests.get(todos)
    todo = tasks.json()
    id = info.get('id')
    username = info.get('username')
    file_name = '{}.json'.format(id)

    task_id = {}
    task_list = []

    for tasks in todo:
        json_task = {}
        if id == tasks.get('userId'):
            json_task["task"] = tasks.get('title')
            json_task["completed"] = tasks.get('completed')
            json_task["username"] = username
            task_list.append(json_task)

    task_id[id] = task_list

    with open(file_name, 'w') as filename:
        json.dump(task_id, filename)

if __name__ == "__main__":
    main()
