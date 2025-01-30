#Ejercicio 1:
def ejer1():
    a = 20.21
    a = int(a)

    print(a, type(a))

    b = 21
    b = float(b)
    print(b, type(b))

#Ejercicio 2:
def ejer2():
    nombre = "pedro"
    print(nombre*3)


#Ejercicio 3:
def ejer3():
    cadena = "Sistemas de Gestión Empresarial"
    primerEspacio= cadena.index(" ")
    apartado1 = cadena[:primerEspacio]
    print(apartado1)
    segundoEspacio = cadena.index(" ",primerEspacio+1)
    apartado2 = cadena[primerEspacio+1:segundoEspacio]
    print(apartado2)
    apartado3 = cadena.upper()
    print(apartado3)
    apartado4 = cadena.replace(" ","")
    print(apartado4)
    apartado5 = str(len(apartado1))+" "+str(len(apartado2))+" "+str(len(apartado3))+" "+str(len(apartado4))
    print(apartado5)


#Ejercicio 4:
def ejer4():
    cadena = "S,G,E"
    lista = cadena.split(",")
    print(lista)


#Ejercicio 5:

def ejer5():
    cadena = "Juan Antonio Cordero Gonzalez"
    repeticiones = cadena.lower().count("a")
    print(repeticiones)


#Ejercicio 6:
def ejer6():
    cadena = "Juan Antonio Cordero Gonzalez"
    repeticiones = cadena.lower().find("a")
    print(repeticiones)


#Ejercicio 7:

def ejer7():
    cadena = "Juan Antonio Cordero Gonzalez"
    primerApellido = cadena.find("Cordero")
    print(cadena.index("a",primerApellido))

#Ejercicio 8:

def ejer8():
    lista = [1,2,3,4,5]
    lista.append(6)
    lista.remove(3)
    print(lista)

#Ejercicio 9:

def ejer9():
    lista = [1,2,3,4,5]
    lista.pop(3)
    print(lista)

#Ejercicio 10:

def ejer10():
    lista = [1,2,3,4,5,6,7,8,9,10]
    tresPrimeros = lista[:3]
    tresUltimos = lista[-3:]
    print(tresPrimeros+tresUltimos)

#Ejercicio 11:

def ejer11():
    lista = [23,1,5,93,67,10,32,7,54,912]
    lista.sort(reverse=True)
    print(lista)

#Ejercicio 12:

def ejer12():
    lista1 = [1,2,3,4,5]
    lista2 = [6,7,8,9,10]
    print(lista1+lista2)

#Ejercicio 13:

def ejer13():
    lista = [1,2,3,4,5]
    lista.append(3.1416)
    lista.sort()
    print(lista)

#Ejercicio 14:

def ejer14():
    lista = ["Juan","Maria","Carlos"]
    cadena = lista[0]+","+lista[1]+","+lista[2]
    print(cadena)

#Ejercicio 15:

def ejer15():
    tupla = (1,2,3)
    print(tupla*2)

#Ejercicio 16:

def ejer16():
    diccionario = {'Nombre': "Roberto", 'Edad': 15,'Ciudad': "Valencia"}
    print(diccionario["Nombre"],diccionario["Edad"],diccionario["Ciudad"])

#Ejercicio 17:

def ejer17():
    diccionario = {'Nombre': "Roberto", 'Edad': 15,'Ciudad': "Valencia"}
    diccionario['Nickname'] = "robertito"
    del(diccionario["Ciudad"])
    print(diccionario["Nombre"],diccionario["Edad"],diccionario["Nickname"])

#Ejercicio 18:

def ejer18():
    diccionario = {'numeros': [1,2,3,4,5]}
    diccionario['numeros'].append(7)
    diccionario['numeros'][0] = 0
    print(diccionario)

#Ejercicio 19:

def ejer19():
    tupla = (1,4,5)
    diccionario = {tupla[0]: tupla[1],tupla[2]:5}
    print(diccionario)

#Ejercicio 20:

def ejer20():
    diccionario = {'Juan Antonio':[(1,2,3),(7,6,5),(10,9,8)]}
    print(diccionario)
ejer20()

