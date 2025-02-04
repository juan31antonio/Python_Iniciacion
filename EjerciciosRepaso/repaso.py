import json

#Ejercicio 1:
"""try:
    def funcionRecibe(parrafo):
        lista = parrafo.split()
        diccionario = {}
        for palabra in lista:
            if palabra in diccionario:
                diccionario[palabra] += 1
            else:
                diccionario[palabra] = 1
        
        diccionarioOrdenado = {}
        valores = list(diccionario.values())

        for i in range(len(valores)):
            for j in range(i + 1, len(valores)):
                if valores[i] < valores[j]:
                    valores[i], valores[j] = valores[j], valores[i]
        
        for frecuencia in valores:
            for clave in diccionario:
                if diccionario[clave] == frecuencia and clave not in diccionarioOrdenado:
                    diccionarioOrdenado[clave] = diccionario[clave]
                    break
        
        return diccionarioOrdenado

except ValueError:
    print("Se ha introducido un valor incorrecto")
    

diccionario = funcionRecibe("Hola que tal estas, Hola que que")
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

"""def pedir_texto():
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
        lista.append(palabra.lower().strip(".,!?;:"))

    print(lista)

pedir_texto()"""



#Ejercicio 4:
#Ejercicio 5:
#Ejercicio 6:
#Ejercicio 7:
#Ejercicio 8:
#Ejercicio 9:
#Ejercicio 10: