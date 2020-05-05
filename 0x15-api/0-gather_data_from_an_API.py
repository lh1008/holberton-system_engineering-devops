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
    name =  urllib.request.urlopen(user)
    name_res = json.load(name)
    tasks = urllib.request.urlopen(todos)
    task_res = json.load(tasks)
    print(task_res)
    print(name_res['name'])
    for t in task_res:
        if t['completed'] == True:
            print(t['title'])


    res = requests.get(user)
    info = res.json()
    print(info['name'])

if __name__ == "__main__":
    main()
