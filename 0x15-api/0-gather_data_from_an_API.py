#!/usr/bin/python3
"""get api data python3"""

import json
import sys
import requests

if __name__ == "__main__":

    argv = sys.argv[1]
    name = (
        requests.get("https://jsonplaceholder.typicode.com/users/{}"
                     .format(argv))
        .json()
        .get("name")
    )

    taskEmploy = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    ).json()
    tasksDone = 0
    tasksTotal = 0
    nameTaskDone = []
    for task in taskEmploy:
        if task.get("completed") and task.get('userId') == int(argv):
            tasksDone += 1
            nameTaskDone.append(task.get("title"))
        if task.get('userId') == int(argv):
            tasksTotal += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, tasksDone, tasksTotal))
    print("\t ", end="")
    print("\n\t ".join(nameTaskDone))
