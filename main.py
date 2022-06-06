import json
import os
import os.path
from os import system
from time import sleep
from colorama import init
from colorama import Fore, Back
init(autoreset=True)

#FUNCIONES RUTA EFICIENTE-----------------------------------------------------------------------------
def verificarVisitadaEfectiva (ratonFila, ratonColumna, ruta, paso):
    for key, value in ruta.items():
        if ratonFila == key[0]:
            if ratonColumna == key[1]:
                # se encontró la coordenada, retorno el paso que es de ahi y por lo tanto no debo sobreescribir nada.
                paso = value
                return True, paso
    # esto seria que no se encontró la coordenada, por lo que paso sería el anterior guardado.
    return False, paso

def obtenerRutaCorta(ruta, coordenada, rutaCorta, paso):

    ok, paso = verificarVisitadaEfectiva (coordenada[0], coordenada[1], ruta, paso)
    
    if paso == 1: #ya llegamos al inicio, yay!
        return paso, coordenada

    paso -= 1
    for key, value in ruta.items():
        if paso == value:
            if coordenada[0] == key[0]-1 and coordenada[1] == key[1]: #arriba
                coordenada = key[:]
                rutaCorta.append(key)
            elif coordenada[0] == key[0] and coordenada[1] == key[1]+1: #derecha
                coordenada = key[:]
                rutaCorta.append(key)
            elif coordenada[0] == key[0] and coordenada[1] == key[1]-1: #derecha
                coordenada = key[:]
                rutaCorta.append(key)
            elif coordenada[0] == key[0]+1 and coordenada[1] == key[1]: #abajo
                coordenada = key[:]
                rutaCorta.append(key)
    
    if paso > 1:
        paso, coordenada = obtenerRutaCorta(ruta, coordenada, rutaCorta, paso)

    return paso, coordenada 

def movimientoEfectivo(raton, nuevoEstado, salida, noFuncionales, posicionesVisitadas, ruta, pasos):

    posicionesVisitadas.append(raton[:])
    pared = simboloPared(nuevoEstado)
    contador = 0
    arriba = 0
    derecha = 0
    izquierda = 0
    abajo = 0
    raton2 = ()

    ok, pasos = verificarVisitadaEfectiva (raton[0], raton[1], ruta, pasos)

    if raton == salida: # Ya se encontró la salida
        pasos += 1
        return pasos, 5
  
    if nuevoEstado[raton[0]-1][raton[1]] != pared and verificarFuncional(raton[0]-1, raton[1], noFuncionales):#Movimiento Arriba
        arriba = 1
    else:
        contador += 1

    if nuevoEstado[raton[0]][raton[1]+1] != pared and verificarFuncional(raton[0], raton[1]+1, noFuncionales):#Movimiento Derecha
        derecha = 1
    else:
        contador += 1

    if nuevoEstado[raton[0]][raton[1]-1] != pared and verificarFuncional(raton[0], raton[1]-1, noFuncionales):#Movimiento Izquierda
         izquierda = 1
    else:
        contador += 1

    if nuevoEstado[raton[0]+1][raton[1]] != pared and verificarFuncional(raton[0]+1, raton[1], noFuncionales):#Movimiento Abajo
        abajo = 1
    else:
        contador += 1

    if contador == 3:
        noFuncionales.append([raton[0], raton[1]])

    # Hasta aquí verificado de paredes, continua el movimiento
    if arriba == 1:
        if raton[0]-1 != posicionesVisitadas[-2][0]:
            if ok == False:
                pasos+=1
                raton2 = tuple(raton)
                ruta.update({raton2:pasos})
                raton[0] = raton[0]-1
                return pasos, contador
            elif ok == True: 
                raton[0] = raton[0]-1
                return pasos, contador

    if derecha == 1:
        if raton[1]+1 != posicionesVisitadas[-2][1]:
            if ok == False:
                pasos+=1
                raton2 = tuple(raton)
                ruta.update({raton2:pasos})
                raton[1] = raton[1]+1            
                return pasos, contador
            elif ok == True: 
                raton[1] = raton[1]+1       
                return pasos, contador

    if izquierda == 1:
        if raton[1]-1 != posicionesVisitadas[-2][1]:
            if ok == False:
                pasos+=1
                raton2 = tuple(raton)
                ruta.update({raton2:pasos})
                raton[1] = raton[1]-1           
                return pasos, contador
            elif ok == True: 
                raton[1] = raton[1]-1             
                return pasos, contador

    if abajo == 1:
        if raton[0]+1 != posicionesVisitadas[-2][0]:
            if ok == False:
                pasos+=1
                raton2 = tuple(raton)
                ruta.update({raton2:pasos})
                raton[0] = raton[0]+1         
                return pasos, contador
            elif ok == True:  
                raton[0] = raton[0]+1             
                return pasos, contador

    return pasos, contador

def encontrarCaminoEficiente(listaLaberintoEficiente, salidaEficiente, noFuncionalesEficiente, posicionesVisitadasEficiente, ratonEficiente, ruta, pasos):
    
    nuevoEstado = listaLaberintoEficiente[:] 
    pasos, contador = movimientoEfectivo(ratonEficiente, nuevoEstado, salidaEficiente, noFuncionalesEficiente, posicionesVisitadasEficiente, ruta, pasos)

    if contador == 5: 
        print(f"{Back.GREEN}¡Salida encontrada correctamente!")
        return pasos

    if contador <= 3: 
        pasos = encontrarCaminoEficiente(nuevoEstado, salidaEficiente, noFuncionalesEficiente, posicionesVisitadasEficiente, ratonEficiente, ruta, pasos)
    else: 
        print(f"{Back.RED}No hay salida posible")    
        return 1987

    return pasos

def rutaEficiente(listaLaberintoEficiente, salidaEficiente, noFuncionalesEficiente, posicionesVisitadasEficiente, ratonEficiente, ruta, pasos, rutaCorta):
    print("\n")
    pasos = encontrarCaminoEficiente(listaLaberintoEficiente, salidaEficiente, noFuncionalesEficiente, posicionesVisitadasEficiente, ratonEficiente, ruta, pasos)
    if pasos == 1987:
        return False
    coordenada = tuple(salidaEficiente[:])
    obtenerRutaCorta(ruta, coordenada, rutaCorta, pasos) 
    print(f"{Fore.YELLOW}La ruta corta es:")
    print(rutaCorta)
    return

def eficiente(listaLaberintoEficiente,salidaEficiente, noFuncionalesEficiente, ratonEficiente, posicionesVisitadasEficiente):
    rutaCorta = []
    pasos = 0
    ruta = {}
    completado = rutaEficiente(listaLaberintoEficiente, salidaEficiente, noFuncionalesEficiente, posicionesVisitadasEficiente, ratonEficiente, ruta, pasos, rutaCorta)
    if completado == False:
        return
    coordenada = rutaCorta[0]

    for item in rutaCorta:
        if listaLaberintoEficiente[coordenada[0]][coordenada[1]] != 'S':
            coordenada = item[:]
            listaLaberintoEficiente[coordenada[0]][coordenada[1]] = chr(215)
            
    listaLaberintoEficiente[coordenada[0]][coordenada[1]] = 'R'  
    
    print(f"{Fore.YELLOW}Impresión de ruta")  
    for datos in listaLaberintoEficiente:
        print(datos)

#FUNCIONES GLOBALES-----------------------------------------------------------------------------------------------
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
            columna += 1
        fila += 1
        columna = 0 

def cargarArchivo(rutaArchivo, listaLaberinto):
    file_exists = os.path.exists(rutaArchivo)
    if file_exists == True:
        with open(rutaArchivo) as archivo:
            contenido = json.load(archivo)
            for datos in contenido:
                listaLaberinto.append(datos.get("fila"))
    else:
        print("El json no se ha encontrado.")
        os.system("pause")
        exit()

    return
        
#FUNCIONES RUTA NORMAL Y VIDAS---------------------------------------------------------------------------        
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
                      
        for datos in nuevoEstado:
            print(datos)   
        print("\n")     
        sleep(.5)
        system('cls')  
        
    if raton == salida: # Ya se encontró la salida
        return vida, 5
  
    if nuevoEstado[raton[0]-1][raton[1]] != pared and verificarFuncional(raton[0]-1, raton[1], noFuncionales):#Movimiento Arriba
        arriba = 1
    else:
        contador += 1

    if nuevoEstado[raton[0]][raton[1]+1] != pared and verificarFuncional(raton[0], raton[1]+1, noFuncionales):#Movimiento Derecha
        derecha = 1
    else:
        contador += 1

    if nuevoEstado[raton[0]][raton[1]-1] != pared and verificarFuncional(raton[0], raton[1]-1, noFuncionales):#Movimiento Izquierda
         izquierda = 1
    else:
        contador += 1

    if nuevoEstado[raton[0]+1][raton[1]] != pared and verificarFuncional(raton[0]+1, raton[1], noFuncionales):#Movimiento Abajo
        abajo = 1
    else:
        contador += 1

    if contador == 3:
        noFuncionales.append([raton[0], raton[1]])
    #Hasta aquí verificado de paredes, continua el movimiento
    
    if arriba == 1:
        if raton[0]-1 != posicionesVisitadas[-2][0]:
            if opcion == 3:
                vida -= 1
            nuevoEstado[raton[0]-1][raton[1]] = chr(9608)
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[0] = raton[0]-1
            return vida, contador

    if derecha == 1:
        if raton[1]+1 != posicionesVisitadas[-2][1]:
            if opcion == 3:
                vida -= 1 
            nuevoEstado[raton[0]][raton[1]+1] = chr(9608)
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[1] = raton[1]+1            
            return vida, contador

    if izquierda == 1:
        if raton[1]-1 != posicionesVisitadas[-2][1]:
            if opcion == 3:
                vida -= 1
            nuevoEstado[raton[0]][raton[1]-1] = chr(9608)
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[1] = raton[1]-1            
            return vida, contador

    if abajo == 1:
        if raton[0]+1 != posicionesVisitadas[-2][0]:
            if opcion == 3:
                vida -= 1
            nuevoEstado[raton[0]+1][raton[1]] = chr(9608)
            nuevoEstado[raton[0]][raton[1]] = ' '
            raton[0] = raton[0]+1            
            return vida, contador

    return vida, contador

def encontrarCamino(estado, salida, noFuncionales, raton, posicionesVisitadas, vida, opcion):
    # estado es el laberinto
    nuevoEstado = estado[:] #crea nuevo estado
            
    vida, contador = movimiento(raton, nuevoEstado, salida, noFuncionales, posicionesVisitadas, vida, opcion)
    if opcion == 3:
        print("Vida restante: " + Fore.CYAN +str(vida))
        if vida == 0:
            errmsg = "¡UPS!"
            centradoerrmsg=errmsg.center(60)
            print(Back.RED + centradoerrmsg)
            print(Fore.RED + "Se le ha terminado la vida al ratón :(")
            return vida, False

    if contador == 5: # Ya se encontró la salida
        winmsg = "¡BIEN!"
        centradowinmsg = winmsg.center(60)
        print(Back.GREEN + centradowinmsg)
        print(Fore.GREEN + "Salida encontrada correctamente")
        return vida, True

    if contador <= 3: 
        encontrarCamino(nuevoEstado, salida, noFuncionales, raton, posicionesVisitadas, vida, opcion)
    else: 
        errmsg2 = "No hay salida posible :("
        centradoerrmsg2 = errmsg2.center(60)
        print(Back.RED + centradoerrmsg2)  
        return vida, False #si analizaste todas las posibilidades y ninguna funciona, termina

def vidas(listaLaberinto, salida, noFuncionales, raton, posicionesVisitadas, vida, opcion):
    vida = encontrarCamino(listaLaberinto, salida, noFuncionales, raton, posicionesVisitadas, vida, opcion)
    return vida


#MAIN------------------------------------------------------------------------------------------------------------------------


listaLaberinto = []
rutaArchivo = 'laberinto.json'

cargarArchivo(rutaArchivo, listaLaberinto)
labt = "Laberinto detectado:"
centradoLabt = labt.center(60)
print(Back.YELLOW + centradoLabt)

for datos in listaLaberinto:
    print(datos)
    
opcion = 0
print("\n")


while opcion != 4:
    
    texto = "EL RATÓN Y SU QUESO"
    centrado = texto.center(60)
    print(Back.YELLOW + centrado)
    titulo = "Menú principal"
    centradoTitulo = titulo.center(60)
    print(Fore.YELLOW + centradoTitulo)
    print("Ingrese: ")
    
    print(f"{Fore.RED}[1] {Fore.RESET} Búsqueda de salida")
    print(f"{Fore.YELLOW}[2] {Fore.RESET} Búsqueda de salida eficiente")
    print(f"{Fore.CYAN}[3] {Fore.RESET} Laberinto con vidas")
    print(f"{Fore.GREEN}[4] {Fore.RESET} Salir del programa")
   
    opcion = int(input())
 
    if opcion == 1:
        
        system('cls')
        op1 = "Búsqueda de salida"
        centradoOp1 = op1.center(60)
        print(Back.RED + centradoOp1)
        print(f"{Fore.RED} El ratón intentará salir del laberinto")
        sleep(2)
        noFuncionales =[]
        raton = encontrarUbicacion(listaLaberinto, 'R')
        salida = encontrarUbicacion(listaLaberinto, 'S')
        posicionesVisitadas = []
        posicionesVisitadas.append(raton)
        
        encontrarCamino(listaLaberinto, salida, noFuncionales, raton, posicionesVisitadas, 0, opcion) 
        
        os.system("pause")
        system('cls')
        listaLaberinto = []
        cargarArchivo(rutaArchivo, listaLaberinto)
   
    if opcion == 2:
        
        system('cls')
        op2 = "Búsqueda de salida eficiente"
        centradoOp2 = op2.center(60)
        print(Back.YELLOW + centradoOp2)
        listaLaberintoEficiente = []
        cargarArchivo(rutaArchivo, listaLaberintoEficiente)
        salidaEficiente = encontrarUbicacion(listaLaberintoEficiente, 'S')
        noFuncionalesEficiente = []
        ratonEficiente = encontrarUbicacion(listaLaberintoEficiente, 'R')
        posicionesVisitadasEficiente = []
        posicionesVisitadasEficiente.append(ratonEficiente)
        
        eficiente(listaLaberintoEficiente, salidaEficiente, noFuncionalesEficiente, ratonEficiente, posicionesVisitadasEficiente)
        
        os.system("pause")
        system('cls')
    
    if opcion == 3:
        
        system('cls')
        op3 = "Laberinto con vidas"
        centradoOp3 = op3.center(60)
        print(Back.CYAN + centradoOp3)
        listaLaberintoVidas = []
        cargarArchivo(rutaArchivo, listaLaberintoVidas)
        salidaVidas = encontrarUbicacion(listaLaberintoVidas, 'S')
        ratonVidas = encontrarUbicacion(listaLaberintoVidas, 'R')
        noFuncionalesVidas = []
        posicionesVisitadasVidas = []
        posicionesVisitadasVidas.append(ratonVidas)
        print("En esta versión, por cada vez que el ratón se mueva, perderá un punto de vida")
        vida = int(input("Ingrese la vida que se le desea asignar al ratón: "))
        
        vidas(listaLaberintoVidas, salidaVidas, noFuncionalesVidas, ratonVidas, posicionesVisitadasVidas, vida, opcion)
        
        listaLaberintoVidas = []
        os.system("pause")
        system('cls')
   
    if opcion == 4:
        
        system('cls')
        op1 = "¡Hasta luego!"
        centradoOp1 = op1.center(60)
        print(Back.GREEN + centradoOp1)
        print("\n")
        creditos = "CRÉDITOS"
        centradoCreditos = creditos.center(60)
        print(Back.YELLOW + centradoCreditos)
        print(f"{Fore.RED}Escamilla Suárez Magally")
        print(f"{Fore.GREEN}Luna Alberto Darwin Leonel")
        print(f"{Fore.CYAN}Toxtega Muñoz Alair")

        sleep(1)