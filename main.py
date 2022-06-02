import json

# Funcion que verifica si una casilla que no está bloqueada sigue siendo funcional.
def verificarFuncional (ratonFila, ratonColumna, noFuncionales):
    for item in range(len(noFuncionales)):
        if ratonFila == noFuncionales[item][0]:
            if ratonColumna == noFuncionales[item][1]:
                return False
    return True

def encontrarUbicacion(estado, objeto):
    columna = 0
    fila = 0
    coordenadas = []
    for item in range(len(estado)):#aqui seria avanzar de fila en fila
        for x in estado[item]:#aqui seria recorrer la fila caracter por caracter
            if x == objeto:
                coordenadas.append(fila)
                coordenadas.append(columna)
                return coordenadas
            columna+=1
        fila+=1
        columna = 0
        
# Función que checa las 4 casillas adyacentes para ver a donde moverse
def movimiento(raton, nuevoEstado, salida, noFuncionales, posicionAnterior):

    nuevoEstado[raton[0]][raton[1]] = ' '
    contador = 0
                    
    if nuevoEstado[raton[0]-1][raton[1]] != "#" and verificarFuncional(raton[0]-1, raton[1], noFuncionales) and ((raton[0]-1) != posicionAnterior[0]):#Movimiento Arriba
        nuevoEstado[raton[0]-1][raton[1]] = 'R'
        raton[0] = raton[0]-1
        print(contador)
        return contador
    else:
        contador+=1
            
    if nuevoEstado[raton[0]][raton[1]+1] != "#" and verificarFuncional(raton[0], raton[1]+1, noFuncionales) and ((raton[1]+1) != posicionAnterior[1]):#Movimiento Derecha
        nuevoEstado[raton[0]][raton[1]+1] = 'R'
        raton[1] = raton[1]+1
        print(contador)        
        return contador
    else:
        contador+=1

    if nuevoEstado[raton[0]][raton[1]-1] != "#" and verificarFuncional(raton[0], raton[1]-1, noFuncionales) and ((raton[1]-1) != posicionAnterior[1]):#Movimiento Izquierda
        nuevoEstado[raton[0]][raton[1]-1] = 'R'
        raton[1] = raton[1]-1
        print(contador)        
        return contador
    else:
        contador+=1
                    
    if nuevoEstado[raton[0]+1][raton[1]] != "#" and verificarFuncional(raton[0]+1, raton[1], noFuncionales) and ((raton[0]+1) != posicionAnterior[0]):#Movimiento Abajo
        nuevoEstado[raton[0]+1][raton[1]] = 'R'
        raton[0] = raton[0]+1
        print(contador)        
        return contador
    else:
        contador+=1

    if raton == salida:
        return 5

def backtrack(estado, salida, noFuncionales, raton):
    #Objetivo es que R y S esten en la misma posición #esto ya queda con la linea 70, procedo a eliminarlo
    # estado es el laberinto
    nuevoEstado = estado[:] #crea nuevo estado
    posicionAnterior = raton[:]
    # importante: ver si backtrack recibe o inicializa raton
    if movimiento(raton, nuevoEstado, salida, noFuncionales, posicionAnterior) <= 2: 
        #si la busqueda da 2 o menos, se continua la busqueda
        backtrack(nuevoEstado, salida, noFuncionales, raton)
        print("Impresion final backtrack")
    if movimiento(raton, nuevoEstado, salida, noFuncionales, posicionAnterior) >= 3: 
        print("Impresion movimiento >=3")
        #si la busqueda da 3, se anexa la posicion a no funcionales
        noFuncionales.append([raton[0], raton[1]]) 
    print("Impresion de nuevo Estado")
    for datos in nuevoEstado:
        print(nuevoEstado, "\n") 
    if movimiento(raton, nuevoEstado, salida, noFuncionales, posicionAnterior) == 5: # Ya se encontró la salida
        return True
    return False #si analizaste todas las posibilidades y ninguna funciona, termina


def cargarArchivo(rutaArchivo, listaLaberinto):
    with open(rutaArchivo) as archivo:
        contenido = json.load(archivo)
        for datos in contenido:
            listaLaberinto.append(datos.get("fila"))
    return

listaLaberinto = []
rutaArchivo = 'laberinto.json'

cargarArchivo(rutaArchivo, listaLaberinto)
for datos in listaLaberinto:
    print(datos)

noFuncionales =[]
backtrack(listaLaberinto,[5,10], noFuncionales, [3,1])