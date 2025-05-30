#  3 – Función mejor_promedio(): Calcula el promedio de cada alumno y 
# determina cuál tiene el mejor promedio. Retorna el índice del alumno y 
# el valor del promedio. 

#importo todas las funciones del archivo main
import main

def mejor_promedio():
    # Cargo la matriz de notas desde el archivo main
    matriz = main.cargar_matriz_notas(2, 3)
    #hago un bucle for para tener una guia visual para el usuario de como es la matriz cargada.
    print("Matriz de notas:")
    for i in matriz:
        print(i)

    mejor_alumno = 0
    mejor_promedio = 0

    # creo un bucle for para recorrer la matriz en busca de los alumnos.
    for alumno in range(len(matriz)):
        suma = 0
        #el segundo bucle recorre las notas.
        for nota in matriz[alumno]:
            #sumo las notas a medida que avanza el bucle
            suma += nota  

        #defino la variable que va a hacer el promedio actual para luego compararlo mas adelante
        promedio = suma / len(matriz[alumno])
        print(f"Alumno {alumno}: promedio = {promedio}")

        #realizo una comparacion para buscar el mejor promedio y voy cambiando la asignacion a medida que aparece un alumno con mejores notas
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_alumno = alumno
    #mensaje final devolviendo los resultados
    print(f"\nEl alumno con mejor promedio es el alumno {mejor_alumno} con un promedio de {mejor_promedio}")
    return mejor_alumno, mejor_promedio

#inicializo la funcion
mejor_promedio()


