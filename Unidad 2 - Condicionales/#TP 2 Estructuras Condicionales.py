#TP 2 Estructuras Condicionales

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))

if edad >= 18: 
    print("Es mayor de edad.")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = float(input("Ingrese una calificación entre 0 y 10: "))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num = float(input("Ingrese un número par: "))

if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.

edad_usuario = int(input("Ingrese su edad: "))

if edad_usuario < 12:
    print("Niño/a")
elif edad_usuario >= 12 and edad_usuario < 18:
    print("Adolescente")
elif edad_usuario >= 18 and edad_usuario < 30:
    print("Adulto/a joven")
else:
    print("Adulto")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 

password = input("Ingrese una contraseña entre 8 a 14 caracteres: ")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mean, median, mode
import random 

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

num_media = mean(numeros_aleatorios)
num_mediana = median(numeros_aleatorios)
num_moda = mode(numeros_aleatorios)

print("Media:", num_media)
print("Mediana:", num_mediana)
print("Moda:", num_moda)

if num_media > num_mediana and num_mediana > num_moda:
    print("Hay sesgo positivo.")
elif num_media < num_mediana and num_mediana < num_moda:
    print("Hay sesgo negatrivo")
elif num_media == num_mediana and num_mediana == num_moda:
    print("Sin sesgo")
else:
    print("No se cumple ninguna condición de sesgo.")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

vocal = ["a","e","i","o","u"]
palabra = input("Ingrese una palabra o frase: ")
ultima_letra = palabra[-1]

if ultima_letra in vocal:
    print(f"{palabra}!")
else:
    print(palabra)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.

nombre = input("Ingrese su nombre: ")
print("Ingrese 1) Para su nombre en mayúscula")
print("Ingrese 2) Para su nombre en minúscula")
print("Ingrese 3) Si quiere su nombre solo con la primera letra en mayúscula")
num = int(input("Ingrese un número:"))

if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower())
elif num == 3:
    print(nombre.title())
else:
    print("Opción inválida.")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: ● Menor que 3: "Muy leve" (imperceptible). ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible). ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos). ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve.")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5: 
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano. 


hemisferio = input("Ingrese su hemisferio indicando si es norte con una N o sur con una S:").upper()
mes = int(input("Ingrese el mes utilizando el número correspondiente (1 - 12): "))
dia = int (input("Ingrese el día de la fecha: "))

if (mes == 3 and dia == 21) or (mes <= 6 and dia <= 20):
    if hemisferio == "N":
        print("Primavera")
    elif hemisferio == "S":
        print("Otoño")
elif (mes == 6 and dia == 21) or (mes <= 9 and dia <= 20):
    if hemisferio == "N":
        print("Verano")
    elif hemisferio == "S":
        print("Invierno")
elif (mes == 9 and dia == 21) or (mes <= 12 and dia <= 20):
    if hemisferio == "N":
        print("Otoño")
    elif hemisferio == "S":
        print("Primavera")
elif (mes == 12 and dia == 21) or (mes <= 3 and dia <= 20):
    if hemisferio == "N":
        print("Invierno")
    elif hemisferio == "S":
        print("Verano")
else:
    print("Los datos ingresados son inválidos. Intente de nuevo.")