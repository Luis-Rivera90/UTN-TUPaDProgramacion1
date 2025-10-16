# TP Unidad 8 Archivos
# Luis Rivera - Comisión 10 - 1er Semestre

# 1) Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad.

with open("productos.txt", "w") as archivo:
    archivo.write("Nombre,Precio,Stock\n")
    archivo.write("Notebook,1200,18\n")
    archivo.write("Tablet,650,22\n")
    archivo.write("Switch,450,15\n")

# 2) Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

def leer_archivo(archivo):
    with open("productos.txt", "r") as archivo:
        next(archivo)
        for linea in archivo:
            nombre, precio, stock = linea.strip().split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Stock: {stock}")

leer_archivo("productos.txt")
print("--------------------------------------\n")

# 3) Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.

opcion = input("Desea agregar un producto a la lista? Ingrese (C) para Continuar o (S) para Salir: ").upper()
while opcion != "C" and opcion != "S":
    print("Opción Inválida")
    opcion = input("Desea agregar un producto a la lista? Ingrese (C) para Continuar o (S) para Salir: ").upper()

if opcion == "S":
    print("No se cargaron datos")
    print("--------------------------------------\n")
else:
    nombre_producto = input("Ingrese el nombre del producto: ").title()

    precio_producto = input("Ingrese el precio del producto: ")
    precio_producto.isdigit()
    while not precio_producto.isdigit():
        print("Ingrese valores numéricos.")
        precio_producto = input("Ingrese el precio del producto: ")
        precio_producto.isdigit()

    stock_producto = input("Ingrese la cantidad de stock a agregar: ")
    stock_producto.isdigit()
    while not stock_producto.isdigit():
        print("Ingrese valores numéricos.")
        stock_producto = input("Ingrese la cantidad de stock a agregar: ")
        stock_producto.isdigit()

    nuevo_producto = f"{nombre_producto}, {precio_producto}, {stock_producto}"

    with open("productos.txt", "a") as archivo:
        archivo.write(nuevo_producto)

print("--------------------------------------\n")
leer_archivo("productos.txt")
print("--------------------------------------\n")

#4) Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

import csv

productos = []

with open("productos.txt", "r") as archivo:
    lectura = csv.DictReader(archivo)
    for linea in lectura:
        productos.append(linea)

print(productos)
print("--------------------------------------\n")

# 5) Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.

buscar = input("Desea buscar un producto? Ingrese (C) para Continuar o (S) para Salir: ").upper()
while buscar != "C" and buscar != "S":
    print("Opción Inválida")
    buscar = input("Desea buscar un producto? Ingrese (C) para Continuar o (S) para Salir: ").upper()

if buscar == "S":
    print("No se buscaron productos")
    print("--------------------------------------\n")
else:
    buscar_producto = input("Ingrese el nombre del producto: ").title()
    encontrado = False

    for producto in productos:
        for clave in producto.items():
            if buscar_producto in clave:
                print(f"{producto}")
                print("--------------------------------------\n")
                encontrado = True

    if not encontrado: 
        print("No hay productos disponibles.")
        print("--------------------------------------\n")
       
# 6) Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.


def sobreescritura(archivo):
    with open("productos.txt", "w") as archivo:
        archivo.write("Nombre,Precio,Stock\n")
        for producto in productos:
            linea = f"{producto['Nombre']}, {producto['Precio']}, {producto['Stock']}\n"
            archivo.write(linea)

sobreescritura("productos.txt")
leer_archivo("productos.txt")

