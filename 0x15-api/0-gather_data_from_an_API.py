#!/usr/bin/python3
"""get api data python3"""

import json
import sys
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://jsonplaceholder.typicode.com/todos')
    with urllib.request.urlopen(req) as response:
        tareas = response.read()
    tareas = tareas.decode('utf8')
    tareas = json.loads(tareas)
    req = urllib.request.Request('https://jsonplaceholder.typicode.com/users')
    with urllib.request.urlopen(req) as response:
        usuarios = response.read()
    usuarios = usuarios.decode('utf8')
    usuarios = json.loads(usuarios)
    nombre = ""
    completadas = 0
    total = 0
    titulos = []
    for i in range(0, len(usuarios)):
        if usuarios[i]['id'] == int(sys.argv[1]):
            nombre = usuarios[i]['name']
            break
    for x in range(0, len(tareas)):
        if tareas[x]['userId'] == int(sys.argv[1]):
            total += 1
            if tareas[x]['completed'] is True:
                completadas += 1
                titulos.append(tareas[x]['title'])
    print("Employee {} is done with tasks({}/{}):".format
        (nombre, completadas, total))
    for v in titulos:
        print("\t {}".format(v))
