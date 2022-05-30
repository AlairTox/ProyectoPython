from importlib.metadata import FileHash
import json

def cargarArchivo(rutaArchivo):
    with open(rutaArchivo) as filas:
        contenido = json.load(filas)
        print(contenido)

rutaArchivo = 'laberinto.json'