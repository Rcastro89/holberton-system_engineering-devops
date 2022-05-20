#!/usr/bin/python3
"""accessing a url with employee ID to return information permision"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    ID = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()
    tareas = {argv[1]: []}
    lista_dic = []
    with open('{}.json'.format(ID), 'w') as archivo:
        for task in todo:
            elementos = {"task": task.get('title'),
                         "complete": task.get('completed'),
                         "username": user.get('username')}
            lista_dic.append(elementos)
        tareas[argv[1]] = lista_dic
        json.dump(tareas, archivo)
