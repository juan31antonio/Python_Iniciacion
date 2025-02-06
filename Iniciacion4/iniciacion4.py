# Ejercicio 1:
"""class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def saludar(self):
        print("Hola mi nombre es ",self.nombre," y tengo ",self.edad," anios")

    def informacion(self):
        print("Mi altura es ", self.altura, " metros")

persona1 = Persona("Juan", 30, 1.75)
persona1.saludar()
persona1.informacion()
"""





# Ejercicio 2:
"""class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,cantidad):
        self.saldo += cantidad
        print("Saldo agregado correctamente")

    def retirar(self,cantidad):
        self.saldo -= cantidad
        print("Saldo retirado correctamente")

    def consultar(self):
        print("Tu saldo actual es ",self.saldo)

persona1 = CuentaBancaria("Juan", 50)
persona1.consultar()
persona1.depositar(100)
persona1.consultar()
persona1.retirar(50)
persona1.consultar()
"""

# Ejercicio 3:

"""class Vehiculo:
    cantidad_total = 0

    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        Vehiculo.cantidad_total += 1

    def mostrar_info(self):
        return "Vehiculo: ", self.marca, " Modelo: ",self.modelo, "Anio: ", self.anio

vehiculo1 = Vehiculo("Toyota", "Corolla", 2021)
vehiculo2 = Vehiculo("Ford", "Mustang", 2022)
vehiculo3 = Vehiculo("Tesla", "Model 3", 2023)

print(vehiculo1.mostrar_info())
print(vehiculo2.mostrar_info())
print(vehiculo3.mostrar_info())
print("Cantidad total de vehiculos creados: ", Vehiculo.cantidad_total)"""





# Ejercicio 4:

"""class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

estudiante1 = Estudiante("Ana", [10, 5, 7, 9, 8])

promedio = estudiante1.calcular_promedio()
print("Nombre: ", estudiante1.nombre)
print("Promedio de calificaciones: ", promedio)"""





# Ejercicio 5:
"""class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def agregarExistencias(self, cantidad):
        self.cantidad += cantidad
        print("Se han agregado ", cantidad, " existencias de este producto")

    def quitarExistencias(self, cantidad):
        self.cantidad -= cantidad
        print("Se han agregado ", cantidad, " existencias de este producto")

    def mostrarInformacionProducto(self):
        print("Producto: ",self.nombre," Precio: ", self.precio," Cantidad: ",self.cantidad)
        

producto1 = Producto("Goma de borrar", 2.50, 10)
producto1.mostrarInformacionProducto()
producto1.agregarExistencias(20)
producto1.mostrarInformacionProducto()
producto1.quitarExistencias(5)
producto1.mostrarInformacionProducto()"""



# Ejercicio 6:
"""class Animal:
    def hacer_sonido(self):
        print("No soy ningun animal en concreto")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

perro = Perro()
gato = Gato()

perro.hacer_sonido()
gato.hacer_sonido()"""




# Ejercicio 7:
"""class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        return self.ancho * self.alto

rectangulo = Rectangulo(5,10)

print("El area del rectangulo es: ", rectangulo.area)"""

# Ejercicio 8:
"""class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        print("Marca: ",self.marca, "Modelo: ",self.modelo)

class Coche(Vehiculo):
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo)
        self.numero_puertas = numero_puertas

    def mostrar_informacion_coche(self):
        self.mostrar_informacion()
        print("Numero de puertas: ",self.numero_puertas)

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo_moto):
        super().__init__(marca, modelo)
        self.tipo_moto = tipo_moto

    def mostrar_informacion_moto(self):
        self.mostrar_informacion()
        print("Tipo de moto: ",self.tipo_moto)


coche = Coche("Toyota", "Corolla", 4)
moto = Moto("Yamaha", "MT-07", "Naked")

print("Información del coche: ")
coche.mostrar_informacion_coche()

print("Información de la moto: ")
moto.mostrar_informacion_moto()"""

# Ejercicio 9:
"""class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return "Título: "+ self.titulo+ " Autor: "+ self.autor

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print("Libro agregado: ", libro.titulo, " por ", libro.autor)

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print("Libro eliminado: ", titulo)
                return
        print("Libro no encontrado: ", titulo)

    def mostrar_libros(self):
        if self.libros:
            print("Listado de libros en la biblioteca:")
            for libro in self.libros:
                print(libro)
        else:
            print("La biblioteca esta vacia")

biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
libro3 = Libro("La sombra del viento", "Carlos Ruiz Zafón")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)


biblioteca.mostrar_libros()
biblioteca.eliminar_libro("Don Quijote de la Mancha")
biblioteca.mostrar_libros()
"""