#!/usr/bin/python3
"""accessing a url with employee ID to return information permision"""

from asyncore import write
from csv import QUOTE_ALL


if __name__ == "__main__":
    import requests
    from sys import argv
    import csv

    ID = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()
    tasks = []
    with open('{}.csv'.format(ID), 'w', newline='') as archivo:
        cabeceras = ['userId', 'name', 'completed', 'title']
        escribir = csv.DictWriter(
            archivo, fieldnames=cabeceras, quoting=csv.QUOTE_ALL)
        for task in todo:
            escribir.writerow({'userId': str(task.get('userId')),
                               'name': user.get('name'),
                               'completed': task.get('completed'),
                               'title': task.get('title')})
