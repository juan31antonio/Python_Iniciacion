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

def main():
    fichero = open("datos.csv","r")
    lineas = fichero.readlines()
    lista = [lineas.split(",")]
    for line in lineas:
        lista += line.split(",")
    print(lista)
    """diccionario = dict()
    for encabezado in lista[0]:
        dict[encabezado] = []
    for fila in lista[1:]:
        for index in range"""
main()
# Ejercicio 6
# Ejercicio 7
# Ejercicio 8
# Ejercicio 9
# Ejercicio 10
# Ejercicio 11