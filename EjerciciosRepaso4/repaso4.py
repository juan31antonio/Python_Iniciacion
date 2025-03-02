import json

#Ejercicio 1
"""def ejer1(lista1, lista2, bool):
    lista = []
    if bool:
        for elemento in lista1:
            if elemento in lista2:
                lista.append(elemento)
    else:
        for elemento in lista1:
            if elemento not in lista2:
                lista.append(elemento)
        for elemento in lista2:
            if elemento not in lista1:
                lista.append(elemento)
    return lista


def main():
    lista_resultado = ejer1([1,2,3,4,5],[1,6,7,8,9],True)
    print(lista_resultado)
main()"""

#Ejercicio 2

"""lista_animales = [
    "Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente", 
    "Caballo", "Oveja", "Mono", "Gallo", "Perro", "Jabali"
]

lista_elementos = [
    "Madera","Madera", "Fuego","Fuego", "Tierra",
    "Tierra", "Metal","Metal", "Agua", "Agua"
]

def ejer2(anio):
    comprobar = anio-1924
    modulo_indice = comprobar % 60

    print(lista_animales[modulo_indice%12])
    print(lista_elementos[modulo_indice%10])
ejer2(1977)"""

#Ejercicio 3
"""tipos = {"Fuego":{"Planta":2,"Electrico":1,"Agua":0.5}, "Electrico":{"Agua":2,"Fuego":1,"Planta":0.5},
 "Agua":{"Fuego":2,"Electrico":1,"Planta":0.5}, "Planta":{"Agua":2,"Electrico":1,"Fuego":0.5}}

def combatePokemon(atacante, defensor, ataque, defensa):
    debilidad = tipos[atacante][defensor]
    dañoHecho = 50 * (ataque/defensa) * debilidad
    print("Has hecho ",dañoHecho," puntos de daño")

def main():
    atacante = input("Dime el tipo del atacante: ")
    defensor = input("Dime el tipo del defensor: ")
    ataque = int(input("Dime los puntos de ataque: "))
    defensa = int(input("Dime los puntos de defensa: "))

    combatePokemon(atacante,defensor,ataque,defensa)
main()"""


#Ejercicio 4

"""class Contacto():
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    def modificar(self, nuevoNombre, nuevoTelefono, nuevoEmail):
        self.nombre = nuevoNombre
        self.telefono = nuevoTelefono
        self.email = nuevoEmail
    def mostrarDatos(self):
        print("Nombre: ",self.nombre," Telefono: ",self.telefono," Email: ",self.email)

def main():
    bucle = True
    agenda = {}
    while bucle:
        respuesta = input("1 --> Añadir Contacto\n2 --> Lista de Contactos\n3 --> Buscar Contacto\n4 --> Editar Contacto\n5 --> Salir Agenda\nPulsa una opcion: ")
        if respuesta == "1":
            nombre = input("Dime el nombre del contacto: ")
            telefono = input("Dime el telefono del contacto: ")
            email = input("Dime el email del contacto: ")
            contacto = Contacto(nombre,telefono,email)
            agenda[nombre] = contacto
        elif respuesta == "2":
            for nombre in agenda:
                agenda[nombre].mostrarDatos()
        elif respuesta == "3":
            nombre = input("Dime el nombre del contacto que quieres buscar: ")
            if nombre in agenda:
                agenda[nombre].mostrarDatos()
            else:
                input("Ese contacto no existe en la agenda: ")
        elif respuesta == "4":
            nombre = input("Dime el nombre del contacto que quieres modificar: ")
            nuevoNombre = input("Dime el nuevo nombre: ")
            nuevoTelefono = input("Dime el nuevo telefono: ")
            nuevoEmail = input("Dime el nuevo email: ")
            agenda[nombre].modificar(nuevoNombre, nuevoTelefono, nuevoEmail)
        elif respuesta == "5":
            print("Saliendo....")
            bucle = False
        else:
            print("Opcion incorrecta")
main()"""


#Ejercicio 5

class JuegoDeMesa():
    def __init__(self, nombre, editorial, mecanica, dificultad):
        self.nombre = nombre
        self.editorial = editorial
        self.mecanica = mecanica
        self.dificultad = dificultad
    def diccionario(self):
        return {
            "nombre": self.nombre,
            "editorial": self.editorial,
            "mecanica": self.mecanica,
            "dificultad": self.dificultad
        }
    
def main():
    bucle = True
    listaJuegos = []
    while bucle:
        respuesta = input("1 --> Agregar Juego\n2 --> Guardar JSON\n3 --> Salir\nPulsa una opcion: ")
        if respuesta == "1":
            nombre = input("Dime el nombre del juego: ")
            editorial = input("Dime la editorial del juego: ")
            mecanica = input("Dime la mecanica del juego: ")
            dificultad = input("Dime la dificultad del juego: ")
            juego = JuegoDeMesa(nombre,editorial,mecanica, dificultad)
            listaJuegos.append(juego)
            print("Juego agregado correctamente")
        elif respuesta == "2":
            fichero = open("JuegosDeMesa.json","w")
            json.dump([juego.diccionario() for juego in listaJuegos],fichero)
            fichero.close()
        elif respuesta == "3":
            print("Saliendo....")
            bucle = False
        else:
            print("Opcion incorrecta")
main()