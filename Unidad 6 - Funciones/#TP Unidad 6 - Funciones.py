#TP Unidad 6 - Funciones
# Luis Rivera - Comisión 10 - 1er Semestre

# 1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!!")

imprimir_hola_mundo()

# 2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}")

nombre_usuario = input("Ingrese su nombre:").title()

saludar_usuario(nombre_usuario)

# 3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre_usuario = input("Ingrese su nombre:").title()
apellido_usuario = input("Ingrese su apellido: ").title()
edad_usuario = int(input("Ingrese su edad: "))
residencia_usuario = input("Ingrese su lugar de residencia: ").title()

informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)

# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

pi = 3.1416

def calcular_area_circulo(radio):
    return pi * (radio * radio)

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

radio_circulo = float(input("Ingrese el radio de la circunferencia: "))

print(f"El área de la circunferencia es {calcular_area_circulo(radio_circulo)} ")
print(f"El perímetro de la circunferencia es: {calcular_perimetro_circulo(radio_circulo)} ")

# 5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

seconds = float(input("Ingrese la cantidad de segundos: "))

print(f"La conversión de {seconds} segundos a horas es de: {segundos_a_horas(seconds)} horas.")

# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}") 

num = int(input("Ingrese un número: "))

tabla_multiplicar(num)

# 7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(x, y):
    suma = x + y
    resta = x - y
    producto = x * y
    if y != 0:
        division = x / y
    else:
        division = "No se puede dividir entre 0."
    return(suma, resta, producto, division)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = operaciones_basicas(num1, num2)

for valor in resultado:
    print(valor)

# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura**2)

peso_kg = float(input("Ingrese su peso en Kg: "))
altura_mtrs = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso_kg, altura_mtrs)

print(f"Su índice de masa corporal es: {imc}")

# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return celsius * (9/5) + 32

grados_celsius = float(input("Ingrese la temperatura en grados celsius: "))

print(f"La temperatura es de {celsius_a_fahrenheit(grados_celsius)} fahrenheit")

# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    suma = a + b + c
    promedio = suma / 3
    return promedio

notas = []
for i in range(3):
    nota = float(input(f"Ingrese la calificación {i + 1}: "))
    notas.append(nota)

print(f"El promedio es de: {calcular_promedio(notas[0], notas[1], notas[2])}")
