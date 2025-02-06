import json,random
#Ejercicio 1

"""horario = {}

class Clase:
    def __init__(self, nombre, diaSemana, hora):
        self.nombre = nombre
        self.diaSemana = diaSemana
        self.hora = hora

def registrarClase():
    bucle = True
    while bucle:
        nombre = input("Dime el nombre de la clase o salir para terminar el horario: ")
        if nombre == "salir":
            bucle = False
            break
        diaSemana = input("Dime el dia de la semana: ")
        hora = input("Dime la hora de esa clase: ")
        clase = Clase(nombre,diaSemana,hora)
        if diaSemana in horario:
            horario[diaSemana].append(clase.__dict__)
        else:
            horario[diaSemana] = [clase.__dict__]
    fichero = open("horario.json","w")
    json.dump(horario,fichero)
    fichero.close()

def verDia():
    dia = input("Dime el dia del que quieres ver el horario: ")
    fichero = open("horario.json","r")
    diccionario = {}
    diccionario = json.load(fichero)
    if dia in diccionario:
        horarioDia = diccionario[dia]
    else:
        print("Ese dia no esta registrado")
    print("El horario de ese dia es: ",horarioDia)

registrarClase()
verDia()"""

#Ejercicio 2

"""banco = {}

def ingresarUser():
    bucle = True
    while bucle:
        try:
            nombre = input("Dime el nombre del usuario o salir: ")
            if nombre == "salir":
                bucle = False
                break
            saldo = int(input("Dime el saldo de ese usuario: "))
            banco[nombre] = saldo
        except ValueError:
            print("Debes introducir un numero como saldo")

def funciones():
    nombre = input("Dime quiene eres: ")
    salida = None
    while salida != 4:
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Consultar saldo")
        print("4. Salir")
        salida = int(input("Dime que quieres hacer: "))
        if salida == 1:
            try:
                cantidad = int(input("Dime la cantidad que quieres introducir en el banco: "))
                banco[nombre] += cantidad
                print("Has introducido: ",cantidad," ahora en tu banco hay: ",banco[nombre],"€")
            except ValueError:
                print("Debes introducir un numero entero")
        elif salida == 2:
            try:
                cantidad = int(input("Dime cuanto dinero vas a retirar: "))
                if cantidad > banco[nombre]:
                    print("No puedes retirar esa cantidad de dinero, saldo insuficiente")
                else:
                    banco[nombre] -= cantidad
                    print("Has retirado: ",cantidad," ahora en tu banco hay: ",banco[nombre],"€")
            except ValueError:
                print("Debes introducir un numero entero")
        elif salida == 3:
            print("Tu saldo actual es de : ",banco[nombre],"€")
        elif salida == 4:
            print("Saliendo...")
ingresarUser()
funciones()"""



#Ejercicio 3

"""coches = [
        ("mercedes",18),
        ("ferrari",22),
        ("porche",20)
    ]

recorrido = {"mercedes":0,"ferrari":0,"porche":0}
def carrera():
    while recorrido[coches[0][0]] < 100 and recorrido[coches[1][0]] < 100 and recorrido[coches[2][0]] < 100:
        for coche in coches:
            recorrido[coche[0]] += random.randint(1, coche[1])
            print("El coche: ",coche[0]," ha llegado hasta los: ",recorrido[coche[0]])
            if recorrido[coche[0]] >= 100:
                print(coche[0]," ha ganado la carrera")
                break
carrera()"""
#Ejercicio 4

class SerVivo():
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia

class Animal(SerVivo):
    def __init__(self, nombre, energia):
        super().__init__(self,nombre,energia)

    def mover(self):
        gasto = 0.1 * random.randint(1,200)
        self.energia -= gasto
        print(self.nombre," se movio y gasto ",gasto ," de energia.")

    def comer(self):
        energiaRecuperada= 2 * random.randint(2,10)
        self.energia += energiaRecuperada
        print(self.nombre,"comio y recupero ",energiaRecuperada ," de energia.")

class Plantas(SerVivo):
    def __init__(self, nombre, energia, crecimiento):
        super().__init__(self,nombre,energia)
        self.crecimiento = crecimiento

    def crecer(self):
        self.crecimiento += 0.5
        self.energia -= 3
        print("La planta ha crecido 0.5 centimetros y ha gastado 3 de energia")

    def fotosintesis(self):
        self.energia += 3
        print("La planta ha hecho la fotosintesis y ha recuperado 3 de energia")