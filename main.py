import json

# Funcion que verifica si una casilla que no está bloqueada sigue siendo funcional.
def verificarFuncional (ratonFila, ratonColumna, noFuncionales):
    for item in range(len(noFuncionales)):
        if ratonFila == noFuncionales[item][0]:
            if ratonColumna == noFuncionales[item][1]:
                return False
    return True

# ESTA FUNCION YA NO SIRVE DE NADA <33333
def agregarNoFuncional (ratonFila, ratonColumna, noFuncionales): #horrible nombre, toca cambiarlo
    for item in range(len(posicionesVisitadas)):
        if ratonFila == posicionesVisitadas[item][0]:
            if ratonColumna == posicionesVisitadas[item][1]:
                noFuncionales.append([posicionesVisitadas[item][0], posicionesVisitadas[item][1]])
                print("coordenada agregada")
                print(noFuncionales)

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
    
    if raton == salida: # Ya se encontró la salida
        return 5
  
  
    if nuevoEstado[raton[0]-1][raton[1]] != '#' and verificarFuncional(raton[0]-1, raton[1], noFuncionales):#Movimiento Arriba
        if raton[0]-1 != posicionesVisitadas[-2][0]:
            nuevoEstado[raton[0]-1][raton[1]] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[0] = raton[0]-1
            print("\n")              
            for datos in nuevoEstado:
                print(datos)    
            return contador
    else:
        contador+=1
            
    if nuevoEstado[raton[0]][raton[1]+1] != '#' and verificarFuncional(raton[0], raton[1]+1, noFuncionales):#Movimiento Derecha
        if raton[1]+1 != posicionesVisitadas[-2][1]: 
            nuevoEstado[raton[0]][raton[1]+1] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[1] = raton[1]+1
            print("\n")              
            for datos in nuevoEstado:
                print(datos)   
            return contador
    else:
        contador+=1

    if nuevoEstado[raton[0]][raton[1]-1] != '#' and verificarFuncional(raton[0], raton[1]-1, noFuncionales):#Movimiento Izquierda
        if raton[1]-1 != posicionesVisitadas[-2][1]:
            nuevoEstado[raton[0]][raton[1]-1] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[1] = raton[1]-1 
            print("\n")              
            for datos in nuevoEstado:
                print(datos)    
            return contador
    else:
        contador+=1
                    
    if nuevoEstado[raton[0]+1][raton[1]] != '#' and verificarFuncional(raton[0]+1, raton[1], noFuncionales):#Movimiento Abajo
        if raton[0]+1 != posicionesVisitadas[-2][0]:
            nuevoEstado[raton[0]+1][raton[1]] = 'R'
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[0] = raton[0]+1 
            print("\n")              
            for datos in nuevoEstado:
                print(datos)  
            return contador
    else:
        contador+=1
        
    return contador

def backtrack(estado, salida, noFuncionales, raton, posicionesVisitadas):
    # estado es el laberinto
    nuevoEstado = estado[:] #crea nuevo estado
            
    print("Prueba de movimiento:")
    contador = movimiento(raton, nuevoEstado, salida, noFuncionales, posicionesVisitadas)

    if contador == 5: # Ya se encontró la salida
        print("Ya se logro :]")
        return True

    if contador == 3: 
        print("Impresion movimiento == 3")
        print(contador)
        #si la busqueda da 3, se anexa la posicion a no funcionales
        noFuncionales.append([raton[0], raton[1]]) 
        print("Estamos dentro del 3, imprimo las nofuncionales:")
        print(noFuncionales)
        print("y las visitadas:")
        print(posicionesVisitadas)
        backtrack(nuevoEstado, salida, noFuncionales, raton, posicionesVisitadas)
        
    elif contador <= 2: 
        print("Impresion movimiento <=2")
        print(contador)
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