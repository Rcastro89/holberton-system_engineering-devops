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
         json.dump({argv[1]: [{
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": user.get('username')
                } for i in todo]}, archivo)
