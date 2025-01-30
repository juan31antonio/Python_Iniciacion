# Ejercicio 1
"""def main():
    archivo = open("datos.txt","r")
    count = 0
    while True:
        linea = archivo.readline() 
        if not linea:
            break 
        print(linea)
        count += 1
    archivo.close()
    print("El numero de lineas es: ", count)
main()"""

# Ejercicio 2

"""def main():
    userInput = input("Dime algo que quieras escribir en el fichero: ")
    fichero = open("salida.txt","w")
    fichero.write(userInput + '\n')
    fichero.close()
main()"""
# Ejercicio 3

"""def main():
    fichero = open("datos.txt","r")
    lista = fichero.readlines()
    palabras = 0
    for line in lista:
        palabras += len(line.split(" "))
    print("El numero de palabras es: ",palabras)
main()"""

# Ejercicio 4

"""def main():
    palabraABuscar = input("Dime la palabra a buscar en el texto: ")
    palabraSustituir = input("Dime la palabra por la que vas a modificar: ")
    fichero = open("texto.txt","r")
    ficheroModificado = open("modificado.txt","w")
    texto = fichero.read()
    texto = texto.replace(palabraABuscar,palabraSustituir)
    ficheroModificado.write(texto)
    fichero.close()
    ficheroModificado.close()
main()"""

# Ejercicio 5

"""def main():
    fichero = open("datos.csv","r")
    list = []
    while line := fichero.readline():
        list += [line.split(",")]
    print(list)
    diccionario = dict()
    for item in list[0]:
        diccionario[item] = []
    for item in list[1::]:
        for index in range(len(item)):
            diccionario[list[0][index]].append(item[index])
    print(diccionario)
main()"""
# Ejercicio 6

"""def main():
    count = 0
    fichero = open("numeros.txt","r")
    numeros = []
    lista = fichero.readlines()
    numMin = int(lista[0])
    numMax = int(lista[0])
    for line in lista:
        num = int(line)
        count += 1
        numeros.append(num)
        if num < numMin:
            numMin = num
        if num > numMax:
            numMax = num
    print("El numero mayor es: ",numMax," el numero menor es: ",numMin," la suma es:", sum(numeros), " y la media es: ",sum(numeros)/ count)
main()"""

# Ejercicio 7

"""def main():
    fichero = open("grande.txt", "r")
    lista = fichero.readlines()
    lineasNum = len(lista)
    for i in range(0, lineasNum, 10):
        ficheroGuardar = open("grande_" + str(i) + ".txt", "w")
        ficheroGuardar.writelines(lista[i:i+10])
main()"""

# Ejercicio 8

"""def main():
    fichero1 = open("archivo1.txt", "r")
    fichero2 = open("archivo2.txt", "r")
    combinado = open("combinado.txt","w")
    lista1 = fichero1.readlines()
    lista2 = fichero2.readlines()
    max_len = max(len(lista1), len(lista2))
    for i in range(max_len):
        if i < len(lista1):
            combinado.write(lista1[i])
        if i < len(lista2):
            combinado.write(lista2[i])
main()"""

# Ejercicio 9

"""def main():
    fichero = open("log.txt", "r")
    ficheroLimpio = open("limpio.txt","w")
    lista = fichero.readlines()
    listaLimpia = []

    for linea in lista:
        if linea not in listaLimpia:
            listaLimpia.append(linea)
    for lineaLimpia in listaLimpia:
        ficheroLimpio.write(lineaLimpia)
main()"""
# Ejercicio 10

"""def main():
    fichero = open("servidor.log", "r")
    ficheroError = open("errores.log", "w")
    ips = []
    errores = []
    diccionario = {}
    lista = fichero.readlines()
    for linea in lista:
        ips.append(linea[20:31])
        if linea.__contains__("Error"):
            errores.append(linea)
    for lineaError in errores:
        ficheroError.write(lineaError)
    for ip in ips:
        if ip in diccionario:
            diccionario[ip] += 1
        else:
            diccionario[ip] = 1
    print(diccionario)
main()"""
# Ejercicio 11

def main():
    bucle = True
    while bucle:
        print("Bloc de Notas")
        print("1--> Agregar nueva nota")
        print("2--> Leer todas las notas")
        print("3--> Buscar notas por palabra clave")
        print("4--> Borrar una nota especifica")
        print("5--> Salir")
        
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            fichero = open("notas.txt", "a")
            nota = input("Dime la nota que quieres agregar: ")
            fichero.write(nota+"\n")
            fichero.close()

        elif opcion == "2": 
            fichero = open("notas.txt", "r")
            lista = fichero.readlines()
            for linea in lista:
                print(linea) 
            fichero.close()  

        elif opcion == "3":
            fichero = open("notas.txt", "r")
            palabraClave = input("Dime la palabra clave por la que quieres buscar: ")
            lista = fichero.readlines()
            for linea in lista:
                if palabraClave in linea:
                    print(linea)   
            fichero.close()

        elif opcion == "4":
            fichero = open("notas.txt", "r")
            lista = fichero.readlines()
            for i in range(0,len(lista)):
                print(str(i)+"--> "+lista[i])  
            borrarNota = input("Dime que nota quieres que borre: ")
            lista.pop(int(borrarNota))
            fichero = open("notas.txt", "w")
            for nota in lista:
                fichero.write(nota)
            fichero.close()

        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Introducido opcion no valida")
main()