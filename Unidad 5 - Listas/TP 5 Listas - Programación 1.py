#TP 5 Listas - Programación 1

# 1) Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas = [7,8,10,9,10,7.5,6.5,9.7,8.5,9.2]
print(notas)

suma = 0

for i in range(len(notas)):
    suma = suma + notas[i]

for i in range(len(notas) -1):
    for i_actual in range(len(notas) -1 - i):
        if notas[i_actual] > notas[i_actual + 1]:
            notas[i_actual], notas[i_actual +1] = notas[i_actual +1], notas[i_actual]

nota_alta = notas[9]
nota_baja = notas[0]

print(f"La suma de todas las notas es: {suma}")

promedio = suma / len(notas)
print(f"El promedio de notas es: {promedio}")

print(f"La nota mas baja fue {nota_baja}")
print(f"La nota mas alta fue {nota_alta}")

# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range(1,6):
    productos.append(input("Ingrese un producto: "))
    productos.sort()

print(productos)

opcion = int(input("Desea eliminar un producto de la lista? Ingrese (1) para confirmar (0) para salir: " ))

if opcion >= 0 and opcion <= 1:
    if opcion == 1:
        eliminar_producto = input("que producto desea eliminar?: ")
        if eliminar_producto in productos:
            productos.remove(eliminar_producto)
        else:
            print("Producto no encontrado")
    elif opcion == 0:
        pass
else:
    print("Ingrese una opcion correcta")

productos.sort()
print(productos)

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random 

numeros_aleatorios = [random.randint(1, 100) for i in range(15)]

numeros_pares = []
numeros_impares = []

for i in range(len(numeros_aleatorios)):
    if ( numeros_aleatorios[i] % 2) == 0:
        numeros_pares.append(numeros_aleatorios[i])
    elif (numeros_aleatorios[i] % 2) != 0:
        numeros_impares.append(numeros_aleatorios[i])

print(f"La lista de pares contiene {len(numeros_pares)} números")
print(numeros_pares)
print(f"La lista de impares contiene {len(numeros_impares)} números")
print(numeros_impares)

# 4) Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

datos_sin_repetidos = set(datos)

print(datos_sin_repetidos)

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Luis", "Mariano", "Iván", "Lorenzo", "Pedro", "Antonio", "Consuelo", "Lina", "Samuel", "Gabriel"]

estudiantes.sort()
print(estudiantes)

print("Desea modificar la lista de alumnos?")
print("(1). Para agregar un estudiante - (2). Para eliminar un estudiante - (0) Para salir")
modificar_lista = int(input("Ingrese una opción: "))

while modificar_lista != 0:
    if modificar_lista == 1:
        estudiantes.append(input("Ingrese el nombre del estudiante: "))
        modificar_lista = int(input("Ingrese una opción: "))
    elif modificar_lista == 2:
        remover_estudiante = input("Ingrese el nombre del estudiante a eliminar: ")
        if remover_estudiante in estudiantes:
            estudiantes.remove(remover_estudiante)
        else:
            print("El nombre no coincide. El estudiante no existe.")
        modificar_lista = int(input("Ingrese una opción: "))
    elif modificar_lista == 0:
        print("Hasta pronto!!")
    else:
        print("Opción incorrecta. Intente de nuevo.")
        modificar_lista = int(input("Ingrese una opción: "))

estudiantes.sort()
print(estudiantes)

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

import random 

numeros_aleatorios = [random.randint(1, 100) for i in range(7)]

print(numeros_aleatorios)

rotar_num = numeros_aleatorios[-1:] + numeros_aleatorios[0:-1]
print(rotar_num)

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [24, 9],   
    [29, 13],  
    [21, 13],  
    [23, 11],  
    [27, 16],  
    [27, 15],  
    [24, 10]   
]

suma_max = 0
suma_min = 0
mayor_amplitud = -1
dia_mayor_amplitud = -1

for i in range(len(temperaturas)):
    maxima = temperaturas[i][0]
    minima = temperaturas[i][1]

    suma_max = suma_max + maxima
    suma_min = suma_min + minima

    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1   

promedio_max = suma_max / len(temperaturas)
promedio_min = suma_min / len(temperaturas)

print(f"El promedio de la suma de las temperaturas máximas es: {promedio_max}")
print(f"El promedio de la suma de las temperaturas mínimas es: {promedio_min}")
print(f"El día con mayor amplitud térmica fue: día {dia_mayor_amplitud}, amplitud {mayor_amplitud})")

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [
    [8.5, 9, 9.2],
    [7.4, 8.3, 8.7],
    [9.1, 9.6, 9.5],
    [6.8, 7.6, 8],
    [8.3, 9.4, 9.1]
]

promedio_cada_estudiante = []

promedio_cada_materia = []

for i in range(len(notas)):
    nota_estudiante1 = notas[i][0]
    nota_estudiante2 = notas[i][1]
    nota_estudiante3 = notas[i][2]

    promedio_estudiante = (nota_estudiante1 + nota_estudiante2 + nota_estudiante3) / len(notas[0])
    promedio_cada_estudiante.append(promedio_estudiante)


for i in range(len(notas[0])): 
    suma = 0
    for j in range(len(notas)): 
        suma += notas[j][i]
    promedio = suma / len(notas)
    promedio_cada_materia.append(promedio)



print(f"Promedio de los estudiantes: \n {promedio_cada_estudiante}")
print(f"Promedio de las materias: \n {promedio_cada_materia}")

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

filas = len(tablero)
columnas = len(tablero[0])

for fila in range(filas):
        for columna in range(columnas):
            print(tablero[fila][columna], end = "    ")
        print()

print("Ingrese: (1) para Jugar. \nIngrese: (0) para Salir")
start = int(input("Ingrese una opción: "))

while start != 0:
        
    if start == 1:

        posicion_fila = int(input("Ingrese un índice entre 0 y 2: "))
        posicion_columna = int(input("ingrese una posición entre 0 y 2: "))

        if (posicion_fila >= 0 and posicion_fila <= 2) and (posicion_columna >= 0 and posicion_columna <= 2):
            jugada = input("Ingrese X o O para jugar: ").upper()
            
            if jugada == "X" or jugada == "O":

                tablero[posicion_fila][posicion_columna] = jugada

                for fila in range(filas):
                    for columna in range(columnas):
                        print(tablero[fila][columna], end = "    ")
                    print()
                start = int(input("Continuar?: "))
            else:
                print("Opción inválida. Intente de nuevo.")
        else:
            print("Opción inválida. Intente de nuevo.")
            start = int(input("Continuar?: "))
    
    else:
        print("Opción inválida. Intente de nuevo.")
        start = int(input("Continuar?: "))
print("Gracias por jugar!!")

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

productos = [
    [10, 8, 9, 7, 13, 18, 14],
    [2, 4, 6, 8, 11, 7, 16],
    [0, 8, 2, 6, 10, 9, 12],
    [4, 7, 5, 11, 9, 18, 10]
]

ventas_por_producto = []
venta_por_dia = 0
dia_mas_ventas = -1
producto_mas_vendido = -1

for i in range(len(productos)):
    suma_ventas_dia = 0

    for j in range(len(productos[0])):
        suma_ventas_dia += productos[i][j]
    
    if suma_ventas_dia > venta_por_dia:
        venta_por_dia = suma_ventas_dia
        dia_mas_ventas = i + 1


for i in range(len(productos[0])):
    suma_ventas_producto = 0

    for j in range(len(productos)):
        suma_ventas_producto += productos[j][i]
    
    ventas_por_producto.append(suma_ventas_producto)
    if suma_ventas_producto > producto_mas_vendido:
        producto_mas_vendido = i + 1

print(f"Ventas totales por producto: {ventas_por_producto}")
print(f"El día con más ventas fue el día {dia_mas_ventas} con {venta_por_dia} ventas totales")
print(f"El producto más vendido fue el producto {producto_mas_vendido}")