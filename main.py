import json

def cargarArchivo(rutaArchivo, listaLaberinto):
    with open(rutaArchivo) as archivo:
        contenido = json.load(archivo)
        for datos in contenido:
            listaLaberinto.append(datos.get("fila"))
    return

# def ideaAvido(objetivo, raton, movimientos):
#     while(raton != objetivo):
#         if movimientoArriba != 'X':
#             raton = ratonArriba
#         elif movimientoIzquierda != 'X':
#             raton = ratonIzq
#         elif movimientoAbajo != 'X':
#             raton = ratonAbajo
#         elif movimientoDerecha != 'X':
#             raton = ratonDerecha
listaLaberinto = []
rutaArchivo = 'laberinto.json'

cargarArchivo(rutaArchivo, listaLaberinto)
for datos in listaLaberinto:
    print(datos)

print(listaLaberinto[2][2])

# backtrack visto en clase para referencia
# def busca(objetivo, alternativas, estado):
#     for opcion in alternativas:
#         nuevoEstado = estado[:] #crea nuevo estado
#         nuevoEstado.append(opcion) #pega alternativa que sí funca
#         if sum(nuevoEstado) == objetivo: #Si encuentro lo que busco, terminé
#             return nuevoEstado
#         if sum(nuevoEstado) > objetivo: #si ya te pasaste, se regresa al inicio buscando otra alternativa
#             print("Me regreso")
#             continue
#              al hacer backtrack, se libera memoria
#         recursividad:Aun no llega, aun no se pasa, llama a la funcion de nuevo para buscar la solucion 
#          suponiendo que el estado actual incluye la alternativa
#         print(nuevoEstado)
#         resultado = busca(objetivo, alternativas, nuevoEstado) 
#         if resultado != False:
#             return resultado
#         return False si analizaste todas las posibilidades y ninguna funca, termina


# funciones necesarios para poder hacer el proyecto:
# verificar arriba, derecha, abajo, izquierda. 
# si desbloqueado, se pasa a esa casilla
# si bloqueado/inexistente, continua checando
# si llega al final del chequeo y no pudo avanzar, se marca esta casilla como bloqueada. Se bloquea? 
# y se regresa a la casilla anterior. y asi
# ^ esto seria solo una funcion, si se rifa
# hacerla recursiva OTL 
# para eso seria que cuando avance se vuelva a llamar a la funcion
# problema seria como hacer el sistema de laberinto para avanzar y demas