# TP4 Estructuras Repetitivas

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(1,101,1):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = int(input("Ingrese un número: "))

digitos = 0

while num != 0:
    num = int(num / 10)
    digitos += 1
    
print(digitos)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número:"))

if num1 < num2:
    mayor = num2
    menor = num1
elif num1 > num2:
    mayor = num1
    menor = num2

suma = 0

for i in range(menor + 1, mayor, 1):
    suma = suma + i
    print(suma)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

num = int(input("Ingrese un número entero. Ingrese 0 para detener la operación: "))
suma = 0

while num != 0:
    suma = suma + num
    num = int(input("Ingrese otro número: "))

print (f"El total de la suma es {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

num_secreto = 7
intentos = 0
num = int(input("Ingrese un número entre 0 y 9: "))

if num >= 0 and num <= 9:
    while num != num_secreto:
        print("Intenta de nuevo")
        intentos += 1
        num = int(input("Ingrese un número entre 0 y 9: "))
    print(f"Has acertado!! tardaste {intentos} intentos.")
else:
    print("El número ingresado no es válido")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100, -1,-2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num = int(input("Ingrese un número: "))

suma = 0

for i in range(0, num, 1):
    suma = suma + i
    print(suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

num_par = 0
num_impar = 0
num_positivo = 0
num_negativo = 0

for i in range(1,101,1):
    num = int(input("Ingrese un número: "))
    if num > 0:
        if num % 2 == 0:
            num_par += 1
        else:
            num_impar += 1
        num_positivo += 1
    elif num < 0:
        if num % 2 == 0:
            num_par += 1
        else:
            num_impar += 1
        num_negativo +=1

print(f"La cantidad de números par fue {num_par}")
print(f"La cantidad de números impares fue {num_impar}")
print(f"La cantidad de números positivos fue {num_positivo}")
print(f"La cantidad de números negativos fue {num_negativo}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

suma = 0

for i in range(1,101,1):
    num = int(input("Ingrese un número: "))
    suma = suma + num

promedio = suma / i
print(f"El promedio de la suma es {promedio}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num_invertido = 0
unidad = 0
num = int(input("Ingrese un número: "))

while num != 0:
    unidad = num % 10
    num_invertido = num_invertido * 10 + unidad
    num = int(num / 10)

print(num_invertido)