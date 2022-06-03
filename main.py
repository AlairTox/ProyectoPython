import json
from turtle import pos
import os

def simboloPared(laberinto):
    pared = laberinto[0][0]
    return pared
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
def movimiento(raton, nuevoEstado, salida, noFuncionales, posicionesVisitadas, vida, opcion):
    posicionesVisitadas.append(raton[:])
    contador = 0
    pared = simboloPared(nuevoEstado)
    arriba = 0
    derecha = 0
    izquierda = 0
    abajo = 0
    if opcion != 2:
        # print("\n")              
        for datos in nuevoEstado:
            print(datos)    
        print("\n")     
        
    if raton == salida: # Ya se encontró la salida
        return vida, 5
  
    if nuevoEstado[raton[0]-1][raton[1]] != pared and verificarFuncional(raton[0]-1, raton[1], noFuncionales):#Movimiento Arriba
        arriba = 1
    else:
        contador+=1

    if nuevoEstado[raton[0]][raton[1]+1] != pared and verificarFuncional(raton[0], raton[1]+1, noFuncionales):#Movimiento Derecha
        derecha = 1
    else:
        contador+=1

    if nuevoEstado[raton[0]][raton[1]-1] != pared and verificarFuncional(raton[0], raton[1]-1, noFuncionales):#Movimiento Izquierda
         izquierda = 1
    else:
        contador+=1

    if nuevoEstado[raton[0]+1][raton[1]] != pared and verificarFuncional(raton[0]+1, raton[1], noFuncionales):#Movimiento Abajo
        abajo = 1
    else:
        contador+=1

    if contador == 3:
        noFuncionales.append([raton[0], raton[1]])
    # HASTA AQUÍ VERIFICADO DE PAREDES, CONTINUA EL MOVIMIENTO

    if arriba == 1:
        if raton[0]-1 != posicionesVisitadas[-2][0]:
            if opcion == 3:
                vida-=1
            nuevoEstado[raton[0]-1][raton[1]] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[0] = raton[0]-1
            return vida, contador

    if derecha == 1:
        if raton[1]+1 != posicionesVisitadas[-2][1]:
            if opcion == 3:
                vida-=1 
            nuevoEstado[raton[0]][raton[1]+1] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[1] = raton[1]+1            
            return vida, contador

    if izquierda == 1:
        if raton[1]-1 != posicionesVisitadas[-2][1]:
            if opcion == 3:
                vida-=1
            nuevoEstado[raton[0]][raton[1]-1] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[1] = raton[1]-1            
            return vida, contador

    if abajo == 1:
        if raton[0]+1 != posicionesVisitadas[-2][0]:
            if opcion == 3:
                vida-=1
            nuevoEstado[raton[0]+1][raton[1]] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[0] = raton[0]+1            
            return vida, contador

    return vida, contador

def encontrarCamino(estado, salida, noFuncionales, raton, posicionesVisitadas, vida, opcion):
    # estado es el laberinto
    nuevoEstado = estado[:] #crea nuevo estado
            
    vida, contador = movimiento(raton, nuevoEstado, salida, noFuncionales, posicionesVisitadas, vida, opcion)
    if opcion == 3:
        print("Vida restante: " + str(vida))
        if vida == 0:
            print("Se ha terminado la vida del raton.")
            return vida, False

    if contador == 5: # Ya se encontró la salida
        print("Salida encontrada correctamente")
        return vida, True

    if contador <= 3: 
        encontrarCamino(nuevoEstado, salida, noFuncionales, raton, posicionesVisitadas, vida, opcion)
    else: 
        print("No hay salida posible")    
        return vida, False #si analizaste todas las posibilidades y ninguna funciona, termina

def cargarArchivo(rutaArchivo, listaLaberinto):
    with open(rutaArchivo) as archivo:
        contenido = json.load(archivo)
        for datos in contenido:
            listaLaberinto.append(datos.get("fila"))
    return

def eficiente(listaLaberintoEficiente, salidaEficiente, noFuncionalesEficiente, ratonEficiente, posicionesVisitadasEficiente, vida, opcion):
    print(posicionesVisitadasEficiente)
    encontrarCamino(listaLaberintoEficiente, salidaEficiente, noFuncionalesEficiente, ratonEficiente, posicionesVisitadasEficiente, vida, opcion)
    posicionesEliminar = []
    if posicionesVisitadas[0] == salida:
        posicionesVisitadas.remove(salida)       
         
    print(posicionesVisitadasEficiente)
    
    for i in range(len(posicionesVisitadasEficiente)):
        if i != posicionesVisitadasEficiente.index(posicionesVisitadasEficiente[i]):
            print("Posición repetida: ", posicionesVisitadasEficiente.index(posicionesVisitadasEficiente[i]))    
            print("Posicion en donde se repite:", i)

def eficienteVersionMia(listaLaberintoEficiente,salidaEficiente, noFuncionalesEficiente, ratonEficiente, posicionesVisitadasEficiente, vida, opcion):
    encontrarCamino(listaLaberintoEficiente, salidaEficiente, noFuncionalesEficiente, ratonEficiente, posicionesVisitadasEficiente, vida, opcion)
    temporal = []  
    posicionesCaminoEficiente = []     
    
    for item in posicionesVisitadasEficiente: 
        if not item in noFuncionalesEficiente:
            temporal.append(item)

    for elemento in temporal:
        if elemento not in posicionesCaminoEficiente:
            posicionesCaminoEficiente.append(elemento) 

    print("Ruta más efectiva: ")
    print(posicionesCaminoEficiente)
    print("Numero de pasos: " + str(len(posicionesCaminoEficiente)))
    return True

def vidas(listaLaberinto, salida, noFuncionales, raton, posicionesVisitadas, vida, opcion):
    vida = encontrarCamino(listaLaberinto, salida, noFuncionales, raton, posicionesVisitadas, vida, opcion)
    return vida
    


########## MAIN #############################
listaLaberinto = []
rutaArchivo = 'laberinto.json'

cargarArchivo(rutaArchivo, listaLaberinto)

print("Impresión inicial del laberinto")
for datos in listaLaberinto:
    print(datos)


opcion = 0

while opcion != 4:
    print("Menu Inicial")
    
    opcion = int(input("Ingresa \n[1]: Busqueda de salida\n[2]: Busqueda de salida eficiente\n[3]: Laberinto con vidas\n[4]: Salir del Programa\n"))
    if opcion == 1:
        noFuncionales =[]
        raton = encontrarUbicacion(listaLaberinto, 'R')
        salida = encontrarUbicacion(listaLaberinto, 'S')
        posicionesVisitadas = []
        posicionesVisitadas.append(raton)
        encontrarCamino(listaLaberinto, salida, noFuncionales, raton, posicionesVisitadas, 0, opcion) 
        os.system("pause")
        listaLaberinto = []
        cargarArchivo(rutaArchivo, listaLaberinto)
    if opcion == 2:
        listaLaberintoEficiente = []
        cargarArchivo(rutaArchivo, listaLaberintoEficiente)
        salidaEficiente = salida[:]
        noFuncionalesEficiente = noFuncionales[:]
        ratonEficiente = raton[:]
        posicionesVisitadasEficiente = posicionesVisitadas[:]
        eficienteVersionMia(listaLaberintoEficiente, salidaEficiente, noFuncionalesEficiente, ratonEficiente, posicionesVisitadasEficiente, 0, opcion)
        os.system("pause")
    if opcion == 3:
        listaLaberintoVidas = []
        cargarArchivo(rutaArchivo, listaLaberintoVidas)
        salidaVidas = encontrarUbicacion(listaLaberinto, 'S')
        ratonVidas = encontrarUbicacion(listaLaberinto, 'R')
        noFuncionalesVidas = []
        posicionesVisitadasVidas = []
        posicionesVisitadasVidas.append(raton)
        print("En esta version, por cada vez que el raton se mueva, perdera un punto de vida")
        vida = int(input("Ingrese la vida que se le desea asignar al raton: "))
        vidas(listaLaberintoVidas, salidaVidas, noFuncionalesVidas, ratonVidas, posicionesVisitadasVidas, vida, opcion)
        listaLaberintoVidas = []
        os.system("pause")