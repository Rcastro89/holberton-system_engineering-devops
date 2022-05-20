#!/usr/bin/python3
"""get api data python3"""

import json
import sys
import requests

if __name__ == "__main__":
    ruta = 'https://jsonplaceholder.typicode.com/users/'
    usuarios = requests.get(ruta + sys.argv[1])
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    user_name = json.loads(usuarios.text)['name']
    todo = json.loads(todo.text)
    tasks = list(i for i in todo if i['userId'] == int(sys.argv[1]))
    succed_tasks = list(i for i in tasks if i['completed'] is True)

    print('Employee {} is done with tasks({}/{}):'
          .format(user_name, len(succed_tasks), len(tasks)))
    [print('\t ' + task['title']) for task in succed_tasks]
