#TP 9 - Recursividad 
#Luis Rivera - Comisión 10 - 1er Semestre

#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

def factorial(numero):
    return 1 if numero == 0 else numero * factorial(numero - 1)

num_factorial = int(input("Ingrese un número: "))
print(f"El factorial de {num_factorial} es: {factorial(num_factorial)}")

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)
        
    
posicion = int(input("Ingrese un número de posición: "))
for i in range(posicion +1):
    print(f"Posición: {i} = {fibonacci(i)}")

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(numero, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return numero
    else:
        return numero * potencia(numero, exponente - 1)

base = int(input("Ingrese un número como base: "))
exponente = int(input("Ingrese un número como exponente: "))

print(f"El número {base} potenciado a {exponente} es igual a: {potencia(base, exponente)}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def binario(numero):
    if numero == 0:
        return ""
    else:
        return binario(numero // 2) + str(numero % 2)

numero = int(input("Ingrese un número: "))
resultado = binario(numero)
print(f"El número {numero} en binario es: {resultado}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):

    palabra = palabra.replace(" ", "").lower()

    if len(palabra) <= 1:
        return True

    if palabra[0] != palabra[-1]:
        return False

    medio = ""

    for i in range(1, len(palabra) - 1):
        medio += palabra[i]

    return es_palindromo(medio)


frase = input("Ingrese una frase: ")
if es_palindromo(frase):
    print(f"{frase} es palíndromo")
else:
    print(f"{frase} no es palíndromo")

#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(numero):
    
    if numero < 10:
        return numero
    
    return (numero % 10) + suma_digitos(numero // 10)

numero = int(input("Ingrese un número: "))

print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

#7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(numero):
    
    if numero == 1:
        return 1
    
    return numero + contar_bloques(numero - 1)


bloques = int(input("Ingresa el número de bloques de la base de tu pirámide: "))

print(f"Necesitas en total {contar_bloques(bloques)} bloques para contruir tu pirámide!!")

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):

    if numero < 10:
        return 1 if numero == digito else 0

    ultimo = numero % 10
    resto = numero // 10

    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)


numero = int(input("Ingrese un número: "))
digito= int(input("Ingrese el dígito que quieres contabilizar: "))

print(f"El número {numero} aparece {contar_digito(numero, digito)} veces.")