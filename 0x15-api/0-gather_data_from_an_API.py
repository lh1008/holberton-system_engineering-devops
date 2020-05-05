#!/usr/bin/python3
""" Module that returns information about TODO list progress """
import json
import requests
from sys import argv
import urllib.request


def main():
    """ Method that prints TODO list """
    url = 'https://jsonplaceholder.typicode.com'
    user = '{}/users/{}'.format(url, argv[1])
    todos = '{}/todos/?userId={}'.format(url, argv[1])

    # GET info from URLs
    name = urllib.request.urlopen(user)
    name_res = json.load(name)
    tasks = urllib.request.urlopen(todos)
    task_res = json.load(tasks)
    print(type(task_res))

    # Lengths
    task_len = len(task_res)
    count = 0
    for v in task_res:
        if v['completed'] is True:
            count += 1

    # Prints
    print('Employee {} is done with tasks({}/{}):'.format(name_res['name'],
                                                          count, task_len))
    for t in task_res:
        if t['completed'] is True:
            print('\t {}'.format(t['title']))

    # GET info from URLs
    res = requests.get(user)
    info = res.json()
    tasks = requests.get(todos)
    todo = tasks.json()

    # Counter
    counter = 0
    for v in todo:
        if v.get('completed') is True:
            counter += 1

    # Prints
    print('Employee {} is done with tasks({}/{}):'.format(info.get('name'),
                                                          counter, len(todo)))

    for k in todo:
        if k.get('completed') is True:
            print('\t {}'.format(k.get('title')))

if __name__ == "__main__":
    main()
