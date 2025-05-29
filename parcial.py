# PARTE 2 – EJERCICIO PRÁCTICO 
# Contexto: Una institución educativa necesita registrar las notas de sus 
# alumnos en distintos exámenes. Cada fila de una matriz representa un 
# alumno y cada columna un examen. 

# Requisitos Generales para Todos los Puntos: - Se deben modularizar todas las operaciones. No se permite resolver 
# todo en el main. - No está permitido el uso de funciones propias de Python como max, 
# min, sum, enumerate, etc. - La validación debe hacerse en la función de carga, verificando que 
# cada nota sea un número entero entre 1 y 10. - Se debe implementar un menú con opciones para ejecutar cada punto 
# de forma separada. - Usar estructuras adecuadas, acumuladores, contadores y recorrido 
# doble. - Nombrar las funciones tal como se indican a continuación. 

# 1 – Función cargar_matriz_notas(): Recibe dos enteros n y m y permite 
# cargar n x m notas válidas entre 1 y 10 inclusive. La validación debe 
# hacerse dentro de esta función. 

# 2 – Función porcentaje_aprobados(): Calcula el porcentaje de 
# exámenes aprobados (nota ≥ 6) por cada alumno y muestra un resumen 
# individual. Usar contadores y acumuladores. 

#  3 – Función mejor_promedio(): Calcula el promedio de cada alumno y 
# determina cuál tiene el mejor promedio. Retorna el índice del alumno y 
# el valor del promedio. 

# 4 – Función buscar_nota(): Recibe la matriz y una nota buscada, y 
# retorna una lista con todas las posiciones (fila, columna) donde aparece 
# esa nota exacta. 

#Creo la funcion, ademas creo y valido que los parametros alumnos y examenes deban ser numeros enteros.
def cargar_matriz_notas(cant_alumnos:int, cant_examenes:int) -> list:
    #creo la matriz vacia donde se van a cargar los datos de los parametros ingresados una vez pasados por el bucle donde van a recibir valor los examenes.
    matriz = []
    #el primer for va a recorrer la cantidad de alumnos
    for i in range(cant_alumnos):
        fila_alumnos = []
    #el segundo for va a recorrer la cantidad de examenes
        for j in range(cant_examenes):
            #valido que la nota ingresada para el alumno no sea menor a 1 ni mayor a 10 creando un bucle con bandera en el caso de ingresar muchas veces un numero erroneo
            bandera = False
            while bandera == False: 
                #pido que el usuario ingrese la nota para el alumno
                nota = int(input(f"Ingrese la nota para el alumno {i}(1-10) en el examen {j}: "))
                if nota >= 1 and nota <= 10:
                    #si se cumple la condicion de que la nota este entre el 1 y el 10 la bandera se activa y da finalizado el bucle de validacion
                    bandera = True
                    #añado a la lista de alumnos la nota del alumno actual
                    fila_alumnos.append(nota)
                else:
                    #si no se cumple la condicion, solicito nuevamente la nota al usuario
                    nota = int(input(f"error, Ingrese la nota para el alumno {i}(1-10) en el examen {j}: "))
        #añado el alumno a la matriz principal
        matriz.append(fila_alumnos)
    return matriz

#en el parametro ya coloco la matriz con los datos de los alumnos cargados.
def porcentaje_aprobados(matriz):
    #creo un bucle for para recorrer las notas de los alumnos e ir buscando los examenes aprobados
    for i in range(len(matriz)):
        #creo una variable que almacene la cantidad de examenes aprobados(contador)
        examenes_aprobados = 0
        #creo una variable que almacene la cantidad de examenes dentro de una lista para luego recorrerla en busca de los aprobados
        lista_de_examenes = len(matriz[i])
        for j in range(lista_de_examenes):
            #recorro la matriz en busca de examenes aprobados(mayor o igual a 6) y luego lo sumo al contador.
            if matriz[i][j] >= 6:
                examenes_aprobados += 1
        #calculo el porcentaje de aprobados y devuelvo un print dando un informe por cada alumno
        porcentaje = (examenes_aprobados / lista_de_examenes) * 100
        print(f"el alumno {i} aprobo {examenes_aprobados} y obtuvo un porcentaje de aprobado del {porcentaje}%")
