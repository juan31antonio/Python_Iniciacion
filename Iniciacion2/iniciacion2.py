#Ejercicio 1:
def ejer1():
    for var in range(100,199):
        print(var)


#Ejercicio 2:
def ejer2():
    for var in range(5,20,3):
        print(var)


#Ejercicio 3:
def ejer3():
    suma = 0
    for var in range(0,101):
        suma += var
    print(suma)  

#Ejercicio 4:
def ejer4():
    num1,num2 = 0,1
    for var in range(0,10):
        fibonacci = num1 + num2
        num1 = num2
        num2 = fibonacci
        print(fibonacci)

#Ejercicio 5:

def ejer5():
    num1,num2 = 0,1
    for var in range(0,10):
        fibonacci = num1 + num2
        num1 = num2
        num2 = fibonacci
        print(fibonacci)


#Ejercicio 6:
def ejer6():
    numero = 0
    bucle = True
    numeros = ""
    while bucle:
        try:
            numero = int(input("Dime un numero entero positivo"))
            if numero > 0:
                bucle = False
            else:
                print("El numero debe de ser positivo")
        except ValueError:
            print("Debe ser un numero entero")
    for var in range(0,numero):
        if(var%2 != 0):
            numeros += str(var)+", "
    print(numeros[:-2])


#Ejercicio 7:

def ejer7():
    numero = 0
    bucle = True
    numeros = ""
    while bucle:
        try:
            numero = int(input("Dime un numero entero positivo"))
            if numero > 0:
                bucle = False
            else:
                print("El numero debe de ser positivo")
        except ValueError:
            print("Debe ser un numero entero")
    numbers = ""
    for var in range(numero,0,-1):
        numbers += str(var) + ", "
    print(numbers[:-2])

#Ejercicio 8:

def ejer8():
    palabra = input("Dime una palabra ")
    for var in palabra[::-1]:
        print(var)

#Ejercicio 9:

def ejer9():
    frase = input("Dime una frase ")
    letra = input("Dime una letra ")
    print(frase.count(letra))

#Ejercicio 10:

def ejer10():
    numero = 0
    bucle = True
    while bucle:
        try:
            numero = int(input("Dime un numero entero positivo "))
            if numero > 0:
                bucle = False
            else:
                print("El numero debe de ser positivo")
        except ValueError:
            print("Debe ser un numero entero")
    for var in range(1,numero+1):
        print("*"*var)

#Ejercicio 11:

def ejer11():
    contraseña = "contraseña"
    bucle = True
    while bucle:
        intento = input("Prueba una contraseña ")
        if intento == contraseña:
            print("Correcto la has acertado")
            bucle = False
        else:
            print("Esa no era la contraseña, prueba de nuevo")

#Ejercicio 12:

def ejer12():
    numero = 0
    bucle = True
    while bucle:
        try:
            numero = int(input("Dime un numero entero positivo "))
            if numero > 0:
                bucle = False
            else:
                print("El numero debe de ser positivo")
        except ValueError:
            print("Debe ser un numero entero")
    isPrimo = True
    for var in range(2,numero):
        if numero%var == 0:
            isPrimo = False
    if isPrimo:
        print("El numero es primo")
    else:
        print("No es primo")
#Ejercicio 13:

def ejer13():
    año1 = int(input("Dime un año: "))
    año2 = int(input("Dime otro año: "))
    for anio in range(año1, año2 + 1):
        es_bisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
        if es_bisiesto and anio % 10 == 0:
            print(anio)

#Ejercicio 14:

def ejer14():
    lista = []
    for var in range(0,5):
        numero = int(input("Dime un numero "))
        lista.append(numero)
    lista.sort()
    print(lista[len(lista)-1])

#Ejercicio 15:

def ejer15():
    num1 = int(input("Dime un numero "))
    num2 = int(input("Dime otro numero "))
    operacion = input("Dime una operacion matematica ")
    if operacion == "+":
        print(num1+num2)
    elif operacion == "-":
        print(num1-num2)
    elif operacion == "*":
        print(num1*num2)
    else:
        print(num1/num2)

#Ejercicio 16:

def ejer16():
    lista = []
    for var in range(0,4):
        palabras = input("Dime una palabra ")
        lista.append(palabras)
    lista.sort()
    print(lista)

#Ejercicio 17:

def ejer17():
    numeroAAdivinar = 15
    contador = 0
    bucle = True
    while bucle:
        numero = int(input("Dime un numero "))
        if numero == numeroAAdivinar:
            if contador < 7:
                print("Has acertado el numero en menos de 7 intentos")
                bucle = False
            else:
                print("Has perdido, lo adivinaste en mas de 7 intentos") 
                bucle = False
        else:
            if numero > numeroAAdivinar:
                print("El numero que debes adivinar es menor, intenta de nuevo")
                contador += 1
            else:
                print("El numero que debes adivinar es mayor, intenta de nuevo")
                contador += 1
#Ejercicio 18:

def ejer18():
    total = 0
    numero = input("Dime un numero de al menos 4 cifras ")
    for digito in numero:
        total += int(digito)
    print(total)
#Ejercicio 19:

def ejer19():
    isPalindromo = False
    palabra = input("Dime una palabra ").lower()
    if palabra == palabra[::-1]:
        isPalindromo = True
    if isPalindromo:
        print("La palabra es un palindromo")
    else:
        print("La palabra no es un palindromo")

#Ejercicio 20:

def ejer20():
    bucle = True
    numeros = []
    while bucle:
        numero = int(input("Dime un numero "))
        if numero == -1:
            bucle = False
        else:
            numeros.append(numero)
    print(sum(numeros) / len(numeros))
ejer20()
