#!/usr/bin/python3
"""accessing a url with employee ID to return information."""

if __name__ == "__main__":
    import requests
    from sys import argv

    ID = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()
    tasks = []
    for task in todo:
        if task.get('completed') is True:
            tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(tasks), len(todo)))
    for task in tasks:
        print("\t {}".format(task))
