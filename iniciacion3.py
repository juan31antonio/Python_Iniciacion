# Ejercicio 1:

def calcularArea(base, altura):
    area = base * altura
    return area

def calcularPerimetro(base, altura):
    perimetro = (base*2) + (altura*2)
    return perimetro

def main():
    base = int(input("Dime la base de un rectangulo "))
    altura = int(input("Dime la altura de un rectangulo "))
    area = calcularArea(base, altura)
    perimetro = calcularPerimetro(base, altura)
    print("El area es: ",area," y el perimetro es: ",perimetro)


# Ejercicio 2:
count = 0
def calcAñosBisiestos(año1, año2):
    global count
    # Al crear una lista con los años y ordenarla,
    # ya no nos afectaria el orden con el que el usuario meta los años
    listaAños = [año1, año2] 
    listaAños.sort()
    listaAñosBisiestos = []
    for anio in range(listaAños[0], listaAños[1] + 1):
        esBisiesto = (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
        if esBisiesto:
            count += 1
            listaAñosBisiestos.append(anio)
    return listaAñosBisiestos


def main():
    primerAño = int(input("Dime un año "))
    segundoAño = int(input("Dime otro año "))
    listaAñosBisiestos = calcAñosBisiestos(primerAño, segundoAño)

    print("Hay entre esos dos años: ",count, " años bisiestos y son: ",listaAñosBisiestos)

# Ejercicio 3:
def ordenadorDePalabras(listaPalabras):
    listaOrdenada = sorted(listaPalabras)
    return listaOrdenada

def main():
    bucle = True
    listaPalabras = []
    while bucle:
        palabra = input("Dime una palabra ")
        if palabra == "FIN":
            bucle = False
        else:
            listaPalabras.append(palabra)
    listaOrdenada = ordenadorDePalabras(listaPalabras)
    print(listaOrdenada)


# Ejercicio 4:

def ordenadorDePalabras(listaPalabras):
    listaOrdenada = sorted(listaPalabras)
    return listaOrdenada

def main():
    bucle = True
    listaPalabras = []
    while bucle:
        palabra = input("Dime una palabra ")
        indice = listaPalabras.index(palabra)
        if indice:
            print("Esa palabra ya esta en la lista")
        else:
            if palabra == "FIN":
                bucle = False
            else:
                listaPalabras.append(palabra)
    listaOrdenada = ordenadorDePalabras(listaPalabras)
    print(listaOrdenada)

# Ejercicio 5:
def sueldoBruto(horas, eurosLaHora):
    bruto = horas * eurosLaHora
    return bruto

def sueldoNeto(sueldoBruto, impuestos):
    neto = sueldoBruto * (1 - impuestos / 100)
    return neto

def impuestosAPagar(sueldoBruto, sueldoNeto):
    impuestosPagados = sueldoBruto - sueldoNeto
    return impuestosPagados

def main():
    horas = int(input("Dime una cantidad de horas: "))
    eurosALaHora = int(input("Dime los euros a la hora: "))
    impuestos = int(input("Dime un porcentaje de impuestos: "))

    sueldoBrutoResultado = sueldoBruto(horas, eurosALaHora)
    sueldoNetoResultado = sueldoNeto(sueldoBrutoResultado, impuestos)
    impuestosPagados = impuestosAPagar(sueldoBrutoResultado, sueldoNetoResultado)

    print("El sueldo bruto es: ",sueldoBrutoResultado," , el neto es: ",sueldoNetoResultado, " y los impuestos pagados son: ",impuestosPagados)

# Ejercicio 6:
def pedirNumeros():
    bucle = True
    listaNumeros = []
    while bucle:
        try:
            num = int(input("Dime un numero "))
            if num == -1:
                bucle = False
            else:
                listaNumeros.append(num)
        except ValueError:
            print("No has introducido un numero")
    return listaNumeros
        

def calcPromedio(listaNumeros):
    promedio = sum(listaNumeros) / len(listaNumeros)
    return print("El promedio es: ",promedio)

def calcMaximo(listaNumeros):
    listaNumeros.sort(reverse= True)
    return print("El maximo es: ",listaNumeros[0])

def calcMinimo(listaNumeros):
    listaNumeros.sort()
    return print("El minimo es: ",listaNumeros[0])

def main():
    listaNumeros = pedirNumeros()
    calcMaximo(listaNumeros)
    calcPromedio(listaNumeros)
    calcMinimo(listaNumeros)

# Ejercicio 7:
def comprobadorTamanio(contraseña):
    if len(contraseña) > 8:
        return True
    else:
        return False

def comprobadorMayusculas(contraseña):
    mayusculas = any(letra.isupper() for letra in contraseña)
    minusculas = any(letra.islower() for letra in contraseña)

    if mayusculas and minusculas:
        return True
    else:
        return False


def comprobadorNumero(contraseña):
    numero = any(caracter.isnumeric() for caracter in contraseña)
    if numero:
        return True
    else:
        return False

def comprobadorCaracter(contraseña):
    char = any(not caracter.isalnum() for caracter in contraseña)
    if char:
        return True
    else:
        return False

def main():
    contraseña = input("Dime un contraseña: ")
    tamanioComprobacion = comprobadorTamanio(contraseña)
    mayusculasComprobacion = comprobadorMayusculas(contraseña)
    numeroComprobacion = comprobadorNumero(contraseña)
    caracteresComprobacion = comprobadorCaracter(contraseña)

    if tamanioComprobacion and mayusculasComprobacion and numeroComprobacion and caracteresComprobacion:
        print("Esta contraseña es segura")
    else:
        if not tamanioComprobacion:
            print("La contraseña no es segura, debe de tenar mas de 8 caracteres")
        if not mayusculasComprobacion:
            print("La contraseña no es segura, no tiene mayusculas o minusculas")
        if not numeroComprobacion:
            print("La contraseña no es segura, agrega algun numero")
        if not caracteresComprobacion:
            print("La contraseña no es segura, agrega algun caracter especial")

# Ejercicio 8:
def calcPromedio(estudiantes):
    notas = []
    # La _, para que el for ignore le primer valor de el par de la tupla
    for _, nota in estudiantes:
        notas.append(nota)
    
    return sum(notas) / len(notas)

def calcMax(estudiantes):
    notas = []
    # La _, para que el for ignore le primer valor de el par de la tupla
    for _, nota in estudiantes:
        notas.append(nota)
    notaMaxima = max(notas)
    for estudiante, nota in estudiantes:
        if nota == notaMaxima:
            return estudiante

def calcMin(estudiantes):
    notas = []
    # La _, para que el for ignore le primer valor de el par de la tupla
    for _, nota in estudiantes:
        notas.append(nota)
    notaMaxima = min(notas)
    for estudiante, nota in estudiantes:
        if nota == notaMaxima:
            return estudiante

def main():
    estudiantes = []
    bucle = True
    while bucle:
        entrada = input("Introduce el nombre y calificacion: ")
        if entrada == "FIN":
            break
        try:
            nombre, calificacion = entrada.split()
            calificacion = float(calificacion)
            if (nombre, calificacion) in estudiantes:
                print("Ese estudiante y calificacion ya estan en la lista")
            else:
                estudiantes.append((nombre, calificacion))
        except ValueError:
            print("Error: Debes introducir el nombre seguido de la calificación, separados por un espacio.")
    promedio = calcPromedio(estudiantes)
    max = calcMax(estudiantes)
    min = calcMin(estudiantes)
    print("El promedio es: ",promedio," la maxima nota es: ",max," y la minima nota es: ",min)

# Ejercicio 9:
def main():

# Ejercicio 10:
