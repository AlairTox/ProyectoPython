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
    print("\n")              
    for datos in nuevoEstado:
        print(datos)       
        
    if raton == salida: # Ya se encontró la salida
        return 5
  
    if nuevoEstado[raton[0]-1][raton[1]] != '#' and verificarFuncional(raton[0]-1, raton[1], noFuncionales):#Movimiento Arriba
        arriba = 1
    else:
        contador+=1

    if nuevoEstado[raton[0]][raton[1]+1] != '#' and verificarFuncional(raton[0], raton[1]+1, noFuncionales):#Movimiento Derecha
        derecha = 1
    else:
        contador+=1

    if nuevoEstado[raton[0]][raton[1]-1] != '#' and verificarFuncional(raton[0], raton[1]-1, noFuncionales):#Movimiento Izquierda
         izquierda = 1
    else:
        contador+=1

    if nuevoEstado[raton[0]+1][raton[1]] != '#' and verificarFuncional(raton[0]+1, raton[1], noFuncionales):#Movimiento Abajo
        abajo = 1
    else:
        contador+=1

    if contador == 3:
        noFuncionales.append([raton[0], raton[1]])
    # HASTA AQUÍ VERIFICADO DE PAREDES, CONTINUA EL MOVIMIENTO

    if arriba == 1:
        if raton[0]-1 != posicionesVisitadas[-2][0]:
            nuevoEstado[raton[0]-1][raton[1]] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[0] = raton[0]-1
            return contador

    if derecha == 1:
        if raton[1]+1 != posicionesVisitadas[-2][1]: 
            nuevoEstado[raton[0]][raton[1]+1] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[1] = raton[1]+1            
            return contador

    if izquierda == 1:
        if raton[1]-1 != posicionesVisitadas[-2][1]:
            nuevoEstado[raton[0]][raton[1]-1] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[1] = raton[1]-1            
            return contador

    if abajo == 1:
        if raton[0]+1 != posicionesVisitadas[-2][0]:
            nuevoEstado[raton[0]+1][raton[1]] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[0] = raton[0]+1            
            return contador
    print("No pude moverme :(")
    print(contador)
    return contador

def backtrack(estado, salida, noFuncionales, raton, posicionesVisitadas):
    # estado es el laberinto
    nuevoEstado = estado[:] #crea nuevo estado
            
    contador = movimiento(raton, nuevoEstado, salida, noFuncionales, posicionesVisitadas)

    if contador == 5: # Ya se encontró la salida
        print("Salida encontrada correctamente")
        return True

    if contador <= 3: 
        backtrack(nuevoEstado, salida, noFuncionales, raton, posicionesVisitadas)

    else: 
        print("No hay salida posible")    
        return False #si analizaste todas las posibilidades y ninguna funciona, termina

def cargarArchivo(rutaArchivo, listaLaberinto):
    with open(rutaArchivo) as archivo:
        contenido = json.load(archivo)
        for datos in contenido:
            listaLaberinto.append(datos.get("fila"))
    return

def eficiente(listaLaberintoEficiente, salidaEficiente, noFuncionalesEficiente, ratonEficiente, posicionesVisitadasEficiente):
    for items in listaLaberintoEficiente:
        print(items)
    print(salidaEficiente)
    print(noFuncionalesEficiente)
    print(ratonEficiente)
    print(posicionesVisitadasEficiente)
    return

def vidas(listaLaberinto, salida, noFuncionales, raton, posicionesVisitadas):
    
    return

########## MAIN #############################
listaLaberinto = []
rutaArchivo = 'laberinto.json'

cargarArchivo(rutaArchivo, listaLaberinto)
print("Impresión inicial del laberinto")
for datos in listaLaberinto:
    print(datos)

noFuncionales =[]
raton = encontrarUbicacion(listaLaberinto, 'R')
salida = encontrarUbicacion(listaLaberinto, 'S')
posicionesVisitadas = []
posicionesVisitadas.append(raton)

listaLaberintoEficiente = []
cargarArchivo(rutaArchivo, listaLaberintoEficiente)
salidaEficiente = salida[:]
noFuncionalesEficiente = noFuncionales[:]
ratonEficiente = raton[:]
posicionesVisitadasEficiente = posicionesVisitadas[:]

listaLaberintoVidas = []
cargarArchivo(rutaArchivo, listaLaberintoVidas)
salidaVidas = salida[:]
ratonVidas = raton[:]
noFuncionalesVidas = noFuncionales[:]
posicionesVisitadasVidas = posicionesVisitadas[:]

opcion = 0
while opcion != 4:
    print("Menu Inicial")
    opcion = int(input("Ingresa \n[1]: Busqueda de salida\n[2]: Busqueda de salida eficiente\n[3]: Laberinto con vidas\n[4]: Salir del Programa\n"))
    if opcion == 1:
        backtrack(listaLaberinto, salida, noFuncionales, raton, posicionesVisitadas)
        print(salida)
        print(noFuncionales)
        print(raton)
        print(posicionesVisitadas)
    if opcion == 2:
        eficiente(listaLaberintoEficiente, salidaEficiente, noFuncionalesEficiente, ratonEficiente, posicionesVisitadasEficiente)
    if opcion == 3:
        vidas(listaLaberintoVidas, salidaVidas, noFuncionalesVidas, ratonVidas, posicionesVisitadasVidas)