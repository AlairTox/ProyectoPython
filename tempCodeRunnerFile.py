def busca(objetivo, alternativas, estado):
#     for opcion in alternativas:
#         nuevoEstado = estado[:] #crea nuevo estado
#         nuevoEstado.append(opcion) #pega alternativa que sí funca
#         if sum(nuevoEstado) == objetivo: #Si encuentro lo que busco, terminé
#             return nuevoEstado
#         if sum(nuevoEstado) > objetivo: #si ya te pasaste, se regresa al inicio buscando otra alternativa
#             print("Me regreso")
#             continue
#             # al hacer backtrack, se libera memoria
#         #recursividad:Aun no llega, aun no se pasa, llama a la funcion de nuevo para buscar la solucion 
#         # suponiendo que el estado actual incluye la alternativa
#         print(nuevoEstado)
#         resultado = busca(objetivo, alternativas, nuevoEstado) 
#         if resultado != False:
#             return resultado
#         return False #si analizaste todas las posibilidades y ninguna funca, termina