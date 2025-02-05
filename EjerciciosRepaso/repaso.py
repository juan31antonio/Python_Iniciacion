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

"""personas = [
    ("Juan", 25, 175),
    ("Ana", 30, 160),
    ("Luis", 22, 180),
    ("Marta", 28, 165)
]

def convertirListaDicc():
    diccionario = {}
    for nombre, edad, altura in personas:
        diccionario[nombre] = {"edad": edad, "altura": altura}
    fichero = open("personas.json","w")
    json.dump(diccionario,fichero)
    fichero.close()

def personaMas():
    fichero = open("personas.json","r")
    diccionario = json.load(fichero)
    personaAlta = None
    personaEdad = None
    alturaMaxima = -1
    edadMaxima = -1

    for nombre in diccionario:
        if diccionario[nombre]["altura"] > alturaMaxima:
            alturaMaxima = diccionario[nombre]["altura"]
            personaAlta = nombre
    
    for nombre in diccionario:
        if diccionario[nombre]["edad"] > edadMaxima:
            edadMaxima = diccionario[nombre]["edad"]
            personaEdad = nombre
    fichero.close()
    print("La persona mas alta es: ",personaAlta," y la de mas edad es: ",personaEdad)

convertirListaDicc()
personaMas()"""

#Ejercicio 6:

"""def numerosEspacios():
    try:
        numeros = input("Dime una lista de numeros separados por espacios: ")
        lista = []
        suma = 0
        promedio = 0
        for numero in numeros.split():
            suma += int(numero)
            lista.append(int(numero))
        promedio = suma/len(lista)
        print("La suma es: ",suma," y el promedio es: ",promedio)
    except ValueError:
        print("Debes introducir solo numeros enteros")
numerosEspacios()"""

#Ejercicio 7:

"""peliculas = [
    ("El Padrino", 1972, "Crimen"),
    ("El Padrino: Parte II", 1974, "Crimen"),
    ("El Senior de los Anillos: El Retorno del Rey", 2003, "Fantasia"),
    ("El Caballero Oscuro", 2008, "Accion"),
    ("Pulp Fiction", 1994, "Crimen"),
    ("Forrest Gump", 1994, "Drama"),
    ("Inception", 2010, "Ciencia Ficcion")
]

def admin(peliculas):
    diccionario = {}
    for titulo, anio, genero in peliculas:
        if genero not in diccionario:
            diccionario[genero] = []
        diccionario[genero].append({"titulo": titulo, "anio": anio})

    fichero = open("peliculas.json", "w")
    json.dump(diccionario, fichero)

    genero = input("Dime de que genero quieres buscar: ")
    if genero in diccionario:
        for pelicula in diccionario[genero]:
            print("El titulo es: ",pelicula["titulo"]," y el anio es: ",pelicula["anio"])
    else:
        print("No se han encontrado peliculas de ese genero")
    fichero.close()
admin(peliculas)"""

#Ejercicio 8:
"""
def leerVentas():
    fichero = open("productos.txt","r")
    lista = fichero.readlines()
    listaProductos = []
    for linea in lista:
        producto = linea.split(",")
        listaProductos.append({
            "producto": producto[0],
            "cantidad": int(producto[1]),
            "precio": float(producto[2])
        })
    
    totalVentas = {}
    for producto in listaProductos:
        nombre = producto["producto"]
        total = producto["cantidad"] * producto["precio"]
        if nombre in totalVentas:
            totalVentas[nombre] += total
        else:
            totalVentas[nombre] = total
    fichero = open("informe.txt","w")
    for producto in totalVentas:
        total = totalVentas[producto]
        texto = "Producto: " + producto + " Ventas: " + str(total) + "\n"
        fichero.write(texto)
    fichero.close()
    
leerVentas()"""
#Ejercicio 9:

"""def compras():
    diccionario = {
        "Cliente1": {
            "nombre": "Roberto",
            "correo": "roberto@example.com",
            "compras": ["Manzana", "Banana", "Naranja"]
        },
        "Cliente2": {
            "nombre": "Godofredo",
            "correo": "godofredo@example.com",
            "compras": ["Manzana", "Banana"]
        },
        "Cliente3": {
            "nombre": "Manu",
            "correo": "manu@example.com",
            "compras": ["Naranja", "Banana", "Manzana", "Uva"]
        }
    }
    fichero = open("compras.json","w")
    json.dump(diccionario, fichero)
    fichero.close()

def leerJson():
    fichero = open("compras.json","r")
    diccionario = json.load(fichero)

    maxCompras = 0
    clienteMax = None
    
    for cliente in diccionario:
        info = diccionario[cliente]
        numCompras = len(info["compras"])
        if numCompras > maxCompras:
            maxCompras = numCompras
            clienteMax = info["nombre"]
    fichero.close()
    print("El cliente con mayot numero de compras es: ", clienteMax)
compras()
leerJson()"""
#Ejercicio 10:

registro = {}

def registrarTemperaturas(diccionario):
    bucle = True
    while bucle:
        fecha = input("Dime la fecha o salir para terminar: ")
        if fecha.lower() == 'salir':
            break
        temperatura = input("Dime la temperatura: ")
        try:
            diccionario[fecha] = float(temperatura)
        except ValueError:
            print("Temperatura no valida")

    fichero = open("temperaturas.json","w")
    json.dump(diccionario, fichero)
    fichero.close()

def promedioUltimaSemana():
    fichero = open("temperaturas.json", "r")
    diccionario = json.load(fichero)

    ultimasFechas = sorted(diccionario.keys(), reverse=True)[:7]

    temperaturas = []
    for fecha in ultimasFechas:
        temperaturas.append(diccionario[fecha])
    
    promedio = sum(temperaturas) / len(temperaturas)
    print("El promedio de temperaturas de la ultima semana es: ", promedio)
    fichero.close()
    

registrarTemperaturas(registro)
promedioUltimaSemana()