# 4 – Función buscar_nota(): Recibe la matriz y una nota buscada, y 
# retorna una lista con todas las posiciones (fila, columna) donde aparece 
# esa nota exacta. 

#importo todas las funciones del archivo main
import main

#la nota que se ingrese va a ser el valor a buscar
def buscar_nota(pedido_busqueda: int):
    # Cargo la matriz de notas desde el archivo main
    matriz = main.cargar_matriz_notas(2,3)
    #recorre las filas de la matriz
    for i in range(len(matriz)):
        #recorre las columnas de la matriz
        for j in range(len(matriz[i])):
            #realizo una condicion para la busqueda de la nota
            if matriz[i][j] == pedido_busqueda:
                #print final
                print(f"coincidencia en el alumno {i},en el examen {j}")
            elif matriz[i][j] != pedido_busqueda:
                #en caso de no haber coincidencias se imprime un mensaje de error
                print(f"NO hubo coincidencias en el alumno {i}, en el examen {j}")
                
buscar_nota(5)