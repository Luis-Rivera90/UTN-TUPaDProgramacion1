#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola mundo!!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print (f"Hola {nombre}!!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")

print( f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

pi = 3.1416

radio = float(input("Ingrese el radio de una circunsferencia: "))

area = pi * (radio * radio)
perimetro = 2 * pi * radio

print(f"El área de la circunsferencia es {area} y el perímetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = float(input("Ingrese la cantidad de segundos: "))

horas = segundos / 3600

print(f"La cantidad de horas equivalente a {segundos} segundos es de {horas} horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num = int(input("Ingrese un número: "))

print( f"{num} x 1 = {num * 1}")
print( f"{num} x 2 = {num * 2}")
print( f"{num} x 3 = {num * 3}")
print( f"{num} x 4 = {num * 4}")
print( f"{num} x 5 = {num * 5}")
print( f"{num} x 6 = {num * 6}")
print( f"{num} x 7 = {num * 7}")
print( f"{num} x 8 = {num * 8}")
print( f"{num} x 9 = {num * 9}")
print( f"{num} x 10 = {num * 10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un segundo número: "))

suma = num1 + num2
print(f"La suma de {num1} + {num2} es = {suma}")

resta = num1 - num2 
print(f"La resta de {num1} - {num2} es = {resta}")

multiplicacion = num1 * num2
print(f"La multiplicación de {num1} * {num2} es = {multiplicacion}")

division = num1 / num2
print(f"La división de {num1} / {num2} es = {division}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 

peso = float(input("Ingrese su peso en kilos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura * altura)

print( f"Su índice de masa corporal (IMC) es = {imc}. ")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

celsius = float(input("Ingrese los grados en celsius: "))

fahrenheit = 9/5 * celsius +32

print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un segundo número: "))
num3 = float(input("Ingrese otro número: "))

suma = num1 + num2 + num3
promedio = suma / 3

print( f"El promedio es de {promedio}.")