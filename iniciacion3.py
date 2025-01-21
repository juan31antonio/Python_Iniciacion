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
        
        if palabra in listaPalabras:
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

inventario = {}
def agregarProducto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    precio = float(input("Ingrese el precio del producto: "))
    inventario[nombre] = {'cantidad': cantidad, 'precio': precio}
    print("Producto agregado correctamente.")

def actualizarProducto():
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    if nombre in inventario:
        nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        inventario[nombre]['cantidad'] = nueva_cantidad
        print("Producto actualizado correctamente.")
    else:
        print("El producto no existe en el inventario.")

def valorProducto():
    nombre = input("Ingrese el nombre del producto: ")
    if nombre in inventario:
        valor = inventario[nombre]['cantidad'] * inventario[nombre]['precio']
        print("El valor del inventario del producto es:", valor)
    else:
        print("El producto no existe en el inventario.")

def valorTotalInventario():
    total = sum(inventario[producto]['cantidad'] * inventario[producto]['precio'] for producto in inventario)
    print("El valor total del inventario es:", total)

def mostrarInventario():
    if inventario:
        print("Inventario actual:")
        for producto, datos in inventario.items():
            print("Nombre:", producto, "Cantidad:", datos['cantidad'], "Precio:", datos['precio'])
    else:
        print("El inventario esta vacio.")

def main():
    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Ver valor de un producto")
        print("4. Ver valor total del inventario")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            agregarProducto()
        elif opcion == 2:
            actualizarProducto()
        elif opcion == 3:
            valorProducto()
        elif opcion == 4:
            valorTotalInventario()
        elif opcion == 5:
            mostrarInventario()
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


# Ejercicio 10:

tienda = {}
carrito = {}
clave_administrador = "admin123"

def es_administrador():
    clave = input("Ingrese la clave de administrador: ")
    return clave == clave_administrador 

def agregarProducto():
    if es_administrador():
        nombre = input("Ingrese el nombre del producto: ")
        stock = int(input("Ingrese el stock del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        tienda[nombre] = {'stock': stock, 'precio': precio}
        print("Producto agregado correctamente.")
    else:
        print("Clave incorrecta. No puede agregar productos.")

def actualizarProducto():
    if es_administrador():
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        if nombre in tienda:
            nuevo_stock = int(input("Ingrese el nuevo stock del producto: "))
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            tienda[nombre]['stock'] = nuevo_stock
            tienda[nombre]['precio'] = nuevo_precio
            print("Producto actualizado correctamente.")
        else:
            print("El producto no existe en la tienda.")
    else:
        print("Clave incorrecta. No puede actualizar productos.")

def mostrarProductos():
    if tienda:
        print("Productos disponibles en la tienda:")
        for producto, datos in tienda.items():
            print(f"Nombre: {producto}, Stock: {datos['stock']}, Precio: {datos['precio']}")
    else:
        print("La tienda esta vacia.")

def agregarAlCarrito():
    nombre = input("Ingrese el nombre del producto a agregar al carrito: ")
    if nombre in tienda and tienda[nombre]['stock'] > 0:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad <= tienda[nombre]['stock']:
            if nombre in carrito:
                carrito[nombre] += cantidad
            else:
                carrito[nombre] = cantidad
            tienda[nombre]['stock'] -= cantidad
            print("Producto agregado al carrito.")
        else:
            print("No hay suficiente stock disponible.")
    else:
        print("El producto no existe o no hay stock disponible.")

def retirarDelCarrito():
    nombre = input("Ingrese el nombre del producto a retirar del carrito: ")
    if nombre in carrito:
        cantidad = int(input("Ingrese la cantidad a retirar: "))
        if cantidad <= carrito[nombre]:
            carrito[nombre] -= cantidad
            tienda[nombre]['stock'] += cantidad
            if carrito[nombre] == 0:
                del carrito[nombre]
            print("Producto retirado del carrito.")
        else:
            print("No tienes esa cantidad en el carrito.")
    else:
        print("El producto no esta en el carrito.")

def mostrarCarrito():
    if carrito:
        print("Contenido del carrito:")
        for producto, cantidad in carrito.items():
            print(f"Nombre: {producto}, Cantidad: {cantidad}")
    else:
        print("El carrito esta vacio.")

def costoTotalCarrito():
    total = sum(carrito[producto] * tienda[producto]['precio'] for producto in carrito)
    print("El costo total del carrito es:", total)

def realizarCompra():
    if carrito:
        costoTotalCarrito()
        confirmar = input("¿Desea realizar la compra?: ")
        if confirmar.lower() == 'si':
            carrito.clear()
            print("Compra realizada con éxito.")
        else:
            print("Compra cancelada.")
    else:
        print("El carrito esta vacio.")

def main():
    while True:
        print("\nOpciones:")
        print("1. Agregar producto a la tienda")
        print("2. Actualizar producto en la tienda")
        print("3. Mostrar productos de la tienda")
        print("4. Agregar producto al carrito")
        print("5. Retirar producto del carrito")
        print("6. Mostrar contenido del carrito")
        print("7. Ver costo total del carrito")
        print("8. Realizar compra")
        print("9. Salir")
        opcion = int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            agregarProducto()
        elif opcion == 2:
            actualizarProducto()
        elif opcion == 3:
            mostrarProductos()
        elif opcion == 4:
            agregarAlCarrito()
        elif opcion == 5:
            retirarDelCarrito()
        elif opcion == 6:
            mostrarCarrito()
        elif opcion == 7:
            costoTotalCarrito()
        elif opcion == 8:
            realizarCompra()
        elif opcion == 9:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida")

main()