#!/usr/bin/python3
"""accessing a url with employee ID to return information permision"""


if __name__ == "__main__":
    import json
    import requests

    user = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    with open('todo_all_employees.json', 'w') as archivo:
        json.dump({x['id']: list({
            "username": x['username'],
            "task": i["title"],
            "completed": i["completed"]
        } for i in todo if i['userId'] == x['id']) for x in user}, archivo)
