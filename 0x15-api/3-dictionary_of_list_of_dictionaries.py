#!/usr/bin/python3
""" Module that exports data in the JSON format """
import json
import requests
import urllib.request


def main():
    """ Method that records all tasks that are owned by employee """
    url = 'https://jsonplaceholder.typicode.com'
    user = '{}/users/'.format(url)
    todos = '{}/todos/'.format(url)

    # GET info from URLs
    res = requests.get(user)
    info = res.json()
    tasks = requests.get(todos)
    todo = tasks.json()
    file_name = 'todo_all_employess.json'

    user_id = {}
    user_name = {}

    for user in info:
        id = user.get('id')
        user_id[id] = []
        user_name[id] = user.get('username')

    for task in todo:
        task_id = {}
        id = task.get('userId')
        task_id = {'username': user_name.get(id), 'task': task.get('title'),
                   'completed': task.get('completed')}
        user_id.get(id).append(task_id)

    with open(file_name, 'w') as filename:
        json.dump(user_id, filename)

if __name__ == "__main__":
    main()
