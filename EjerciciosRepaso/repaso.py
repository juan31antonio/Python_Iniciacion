import json

#Ejercicio 1:
"""def funcionRecibe(parrafo):
    lista = parrafo.split()
    diccionario = {}
    for palabra in lista:
        if palabra.isalpha():
            if palabra in diccionario:
                diccionario[palabra] += 1
            else:
                diccionario[palabra] = 1

    diccionarioOrdenado = dict(sorted(diccionario.items(), key=lambda item: item[1], reverse=True))
    return diccionarioOrdenado

diccionario = funcionRecibe("Hola que tal estas, Hola que que 123 456")
print(diccionario)"""

#Ejercicio 2:

"""def guardarInDict():
    libros = [
        {"titulo": "Cien anios de soledad", "autor": "Gabriel Garcia Marquez", "anio": 1967, "precio": 15.99},
        {"titulo": "1984", "autor": "George Orwell", "anio": 1949, "precio": 12.50},
        {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "anio": 1605, "precio": 18.75},
        {"titulo": "El principito", "autor": "Antoine de Saint-Exupery", "anio": 1943, "precio": 10.99},
        {"titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "anio": 1813, "precio": 14.20}
    ]

    fichero = open("libros.json","w")
    json.dump(libros,fichero)
    fichero.close()

def conversionEurosDolares():
    fichero = open("libros.json","r")
    diccionario = json.load(fichero)
    for libro in diccionario:
        libro["precio"] = libro["precio"] * 1.04
    fichero.close()
    fichero = open("libros.json","w")
    json.dump(diccionario,fichero)
    fichero.close()

guardarInDict()
conversionEurosDolares()"""

#Ejercicio 3:

"""def pedirTexto():
    bucle = True
    while bucle:
        texto = input("Introduzca un texto: ")
        if not any(palabra.isdigit() for palabra in texto):
            bucle = False
        else:
            print("El texto no debe tener numeros")

    lista = []
    textoSplit = texto.split()

    for palabra in textoSplit:
        lista.append(palabra.lower().strip(".,!¡¿?;:"))
    print(lista)

pedirTexto()"""

#Ejercicio 4:

"""ventas = {
        "producto1": {"precio":10, "cantidad":5 },
        "producto2": {"precio":20, "cantidad":3 }
    }

def calcTotal(ventas):
    totalIngresos = 0
    for clave in ventas:
        producto = ventas[clave]
        totalIngresos += producto["precio"] * producto["cantidad"]
    return totalIngresos

def ventaProductos():
    totalIngresos = calcTotal(ventas)
    fichero = open("totalIngresos.json","w")
    json.dump({"totalIngresos": totalIngresos},fichero)
    

def restarProductosVendidos():
    productoRestar = input("Dime el producto que vas a restar: ")
    cantidad = int(input("Dime cuantos productos quieres restar: "))
    ventas[productoRestar]["cantidad"] -= cantidad 
    print(ventas)

ventaProductos()
restarProductosVendidos()"""

#Ejercicio 5:


#Ejercicio 6:
#Ejercicio 7:
#Ejercicio 8:
#Ejercicio 9:
#Ejercicio 10: