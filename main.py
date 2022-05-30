import json

def cargarArchivo(rutaArchivo):
    with open(rutaArchivo) as archivo:
        contenido = json.load(archivo)
        print(type(contenido))
        for datos in contenido:
            print(datos.get("intento"))

rutaArchivo = 'laberinto.json'

cargarArchivo(rutaArchivo)
