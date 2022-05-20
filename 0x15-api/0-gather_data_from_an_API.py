#!/usr/bin/python3
"""Escriba un script de Python que, utilizando esta API REST,
para una ID de empleado determinada, devuelva información
sobre el progreso de su lista TODO."""

import requests
import sys

if __name__ == "__main__":

    did = sys.argv[1]
    url = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(did))
    nombre = url.json().get('name')
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    total = 0
    completed = 0
    for tareas in todos:
        if tareas.get('userId') == int(did):
            total += 1
            if tareas.get('completed'):
                completed += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(nombre, completed, total))
    print("\n".join(["\t " + tareas.get('title') for tareas in todos
                     if tareas.get('userId') == int(did)
                     and tareas.get('completed')]))
