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
def movimiento(raton, nuevoEstado, salida, noFuncionales, posicionesVisitadas):
    posicionesVisitadas.append(raton[:])
    contador = 0
    arriba = 0
    derecha = 0
    izquierda = 0
    abajo = 0
    
    if raton == salida: # Ya se encontró la salida
        return 5
  
    if nuevoEstado[raton[0]-1][raton[1]] != '#' and verificarFuncional(raton[0]-1, raton[1], noFuncionales):#Movimiento Arriba
        # no hay pared ni bloqueado arriba
        print("no hay pared arriba")
        arriba = 1
    else:
        contador+=1

    if nuevoEstado[raton[0]][raton[1]+1] != '#' and verificarFuncional(raton[0], raton[1]+1, noFuncionales):#Movimiento Derecha
        # no hay pared ni bloqueado derecha
        print("no hay pared derecha")
        derecha = 1
    else:
        contador+=1

    if nuevoEstado[raton[0]][raton[1]-1] != '#' and verificarFuncional(raton[0], raton[1]-1, noFuncionales):#Movimiento Izquierda
         print("no hay pared izquierda")
         izquierda = 1
    else:
        contador+=1

    if nuevoEstado[raton[0]+1][raton[1]] != '#' and verificarFuncional(raton[0]+1, raton[1], noFuncionales):#Movimiento Abajo
        print("no hay pared abajo")
        abajo = 1
    else:
        contador+=1
    if contador == 3:
        noFuncionales.append([raton[0], raton[1]])
    # HASTA AQUÍ VERIFICADO DE PAREDES, CONTINUA EL MOVIMIENTO

    if arriba == 1:
        if raton[0]-1 != posicionesVisitadas[-2][0]:
            print("me muevo arr")
            nuevoEstado[raton[0]-1][raton[1]] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[0] = raton[0]-1
            print("\n")              
            for datos in nuevoEstado:
                print(datos)   
            print(contador) 
            return contador

    if derecha == 1:
        if raton[1]+1 != posicionesVisitadas[-2][1]: 
            print("me muevo der")
            nuevoEstado[raton[0]][raton[1]+1] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[1] = raton[1]+1
            print("\n")              
            for datos in nuevoEstado:
                print(datos)   
            print(contador)
            return contador

    if izquierda == 1:
        if raton[1]-1 != posicionesVisitadas[-2][1]:
            print("me muevo izq")
            nuevoEstado[raton[0]][raton[1]-1] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[1] = raton[1]-1 
            print("\n")              
            for datos in nuevoEstado:
                print(datos)    
            print(contador)
            return contador

    if abajo == 1:
        if raton[0]+1 != posicionesVisitadas[-2][0]:
            print("me muevo ab")
            nuevoEstado[raton[0]+1][raton[1]] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[0] = raton[0]+1 
            print("\n")              
            for datos in nuevoEstado:
                print(datos)  
            print(contador)
            return contador

    else:
        print("No pude moverme :(")
        print(contador)
        return contador

def backtrack(estado, salida, noFuncionales, raton, posicionesVisitadas):
    # estado es el laberinto
    nuevoEstado = estado[:] #crea nuevo estado
            
    print("Inicio Backtrack:")
    contador = movimiento(raton, nuevoEstado, salida, noFuncionales, posicionesVisitadas)
    print(contador)

    if contador == 5: # Ya se encontró la salida
        print("Ya se logro :]")
        return True

    if contador == 3: 
        print("Impresion movimiento == 3")
        #si la busqueda da 3, se anexa la posicion a no funcionales
        print("Estamos dentro del 3, imprimo las nofuncionales:")
        print(noFuncionales)
        print("y las visitadas:")
        print(posicionesVisitadas)
        print("Agrego a noFuncionales")
        backtrack(nuevoEstado, salida, noFuncionales, raton, posicionesVisitadas)
        
    elif contador <= 2: 
        print("Impresion movimiento <=2")
        #si la busqueda da 2 o menos, se continua la busqueda
        print("Estamos dentro del 2, imprimo las nofuncionales:")
        print(noFuncionales)
        print("y las visitadas:")
        print(posicionesVisitadas)
        backtrack(nuevoEstado, salida, noFuncionales, raton, posicionesVisitadas)

    else: 
        print("No hay salida")    
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
raton = encontrarUbicacion(listaLaberinto, 'R')
salida = encontrarUbicacion(listaLaberinto, 'S')
posicionesVisitadas = []
posicionesVisitadas.append(raton)

backtrack(listaLaberinto, salida, noFuncionales, raton, posicionesVisitadas)