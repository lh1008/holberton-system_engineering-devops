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
