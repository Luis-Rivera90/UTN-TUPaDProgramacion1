# TP 7 - Datos Complejos
# Luis Rivera - Comisión 10 - 1er Semestre

# 1) Dado el siguiente diccionario, añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 

precios_frutas ["Naranja"] = 1200
precios_frutas ["Manzana"] = 1500
precios_frutas ["Pera"] = 2300

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 

#Frutas agregadas
precios_frutas ["Naranja"] = 1200
precios_frutas ["Manzana"] = 1500
precios_frutas ["Pera"] = 2300

# Actualizando precios
precios_frutas ["Banana"] = 1330
precios_frutas ["Manzana"] = 1700
precios_frutas ["Melón"] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

print(precios_frutas.keys())

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

for i in range(5):
    nombre = input("Ingrese el nombre de contacto: ")
    num_tlf = int(input("Ingrese el número de contacto: "))
    contactos[nombre] = num_tlf

print(contactos)

contacto = input("Buscar el número del contacto: ")
if contacto in contactos:
    print(f"El número del contacto es: {contactos[contacto]}")
else:
    print("El Contacto no existe.")

# 5) Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

palabras = frase.split()
palabras_unicas = set(palabras)
cantidad_repetida = {}

print(palabras_unicas)

for palabra in palabras:
    if palabra not in cantidad_repetida:
        cantidad_repetida[palabra] = 1
    else:
        cantidad_repetida[palabra] += 1

print(cantidad_repetida)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.


alumnos = {}
promedios = {}

for i in range(3):
    alumno = input(f"Ingrese el nombre del alumno {i + 1}: ")
    notas = []
    for j in range(3):
       
        nota = float(input(f"Ingrese la nota {j + 1} "))
        notas.append(nota)
        
    alumnos[alumno] = tuple(notas)

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    promedios[alumno] = promedio

print(alumnos)
print(f"Promedios :{promedios}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {
            "Luis" : 10,
            "Mariano" : 8,
            "Pedro" : 7,
            "Coni" : 6,
            "Fran" : 4,
            "Lula" : 5
        }

parcial2 = {
            "Luis" : 9,
            "Mariano" : 5,
            "Pedro" : 4,
            "Coni" : 8,
            "Fran" : 9,
            "Lula" : 8
        }

min_aprobado = 6

aprobados_parcial1 = []
for alumno, nota in parcial1.items():
    if nota >= min_aprobado:
        aprobados_parcial1.append(alumno)

aprobados_parcial2 = []
for alumno, nota in parcial2.items():
    if nota >= min_aprobado:
        aprobados_parcial2.append(alumno)

aprobados_set1 = set(aprobados_parcial1)
aprobados_set2 = set(aprobados_parcial2)

ambos = aprobados_set1 & aprobados_set2
solo_uno = aprobados_set1 ^ aprobados_set2
al_menos_uno = aprobados_set1 | aprobados_set2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.

productos = {
    "laptop" : 5,
    "tablet" : 4,
    "iphone" : 6,
    "switch" : 5
}

menu = [
    "1) Consultar stock\n" 
    "2) Agregar Stock\n"
    "3) Agregar nuevo producto\n"
    "4) Salir\n"
]

opcion = ""

while opcion != "4":

    for opciones in menu:
        print(opciones)
    print("------------------------------\n")

    opcion = input("Ingrese una opción: ")
    print("------------------------------\n")

    match opcion:
        case "1":

            for producto, stock in productos.items():
                print(f"{producto}\n")
            print("------------------------------\n")

            consulta = input("Ingrese el nombre del producto: ")
            if consulta in productos:
                print(f"Stock disponible: {productos[consulta]}")
                print("------------------------------\n")
                input("Presione Enter para continuar.")
            else:
                print("El producto no está disponible o no existe")
                print("------------------------------\n")
                input("Presione Enter para continuar.")
                continue

        case "2":

            for producto, stock in productos.items():
                print(producto, stock)
            print("------------------------------\n")

            producto = input("Ingrese el nombre del producto: ")
            if producto in productos:
                nuevo_stock = input("Ingrese la cantidad a agregar al stock: ")
                print("------------------------------\n")
                nuevo_stock.isdigit()
                while not nuevo_stock.isdigit():
                    print("Ingrese la cantidad en números")
                    nuevo_stock = input("Ingrese la cantidad a agregar al stock: ")
                    print("------------------------------\n")
            
            nuevo_stock = int(nuevo_stock)

            productos[producto] += nuevo_stock

            for producto, stock in productos.items():
                print(producto, stock)
            print("------------------------------\n")
            input("Presione Enter para continuar.")

        case "3":
            
            for producto, stock in productos.items():
                print(producto, stock)
            print("------------------------------\n")

            nuevo_producto = input("Ingrese el nombre de producto a agregar: ")
            print("------------------------------\n")
            if nuevo_producto not in productos:
                productos[nuevo_producto] = 0
                nuevo_stock = input("Ingrese la cantidad a agregar al stock: ")
                print("------------------------------\n")
                nuevo_stock.isdigit()
                while not nuevo_stock.isdigit():
                    print("Ingrese la cantidad en números")
                    nuevo_stock = input("Ingrese la cantidad a agregar al stock: ")
                    print("------------------------------\n")
            
            nuevo_stock = int(nuevo_stock)

            productos[nuevo_producto] += nuevo_stock

            for producto, stock in productos.items():
                print(producto, stock)
            print("------------------------------\n")
            input("Presione Enter para continuar.")

        case "4":
            print("Gracias, vuelva pronto")
        case _:
            print("Opción inválida. Vuelva a intentar.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "09:00") : "reunión",
    ("martes", "15:00") : "consulta médica",
    ("miércoles", "10:00") : "pago programado",
    ("jueves", "22:00") : "fútbol",
    ("viernes", "18:00") : "entrega del tp de programación",
    ("sábado", "21:00") : "cena familiar"
}


buscar_dia = input("Ingrese el día que desea consultar:").lower()
print("------------------------------\n")
buscar_horario = input("Ingrese la hora que desea consultar:")
hora = buscar_horario.replace(":","")
hora.isdigit()
while not hora.isdigit():
    print("Ingrese la hora con números en horas:minutos")
    buscar_horario = input("Ingrese la hora que desea consultar:")
    hora = buscar_horario.replace(":","")
    hora.isdigit()
print("------------------------------\n")

busqueda = (buscar_dia, buscar_horario)
if busqueda in agenda:
    print(f"Actividad registrada: {agenda[busqueda]}")
else:
    print("No tienes actividades registradas.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.

paises = {
    "Argentina" : "Buenos Aires",
    "Venezuela" : "Caracas",
    "España" : "Madrid"
}

invertidos = {}

for pais, capital in paises.items():
    invertidos[capital] = pais

print(invertidos)

