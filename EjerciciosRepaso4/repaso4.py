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

dictAgua = {"Fuego":2,"Electrico":1,"Planta":0.5}
dictFuego = {"Planta":2,"Electrico":1,"Agua":0.5}
dictPlanta = {"Agua":2,"Electrico":1,"Fuego":0.5}
dictElectrico = {"Agua":2,"Fuego":1,"Planta":0.5}

def combatePokemon(atacante, defensor, ataque, defensa):
    debilidad = 0
    if atacante == "Agua":
        debilidad = dictAgua[defensor]
    elif atacante == "Fuego":
        debilidad = dictFuego[defensor]
    elif atacante == "Planta":
        debilidad = dictPlanta[defensor]
    elif atacante == "Electrico":
        debilidad = dictElectrico[defensor]
    dañoHecho = 50 * (ataque/defensa) * debilidad
    print("Has hecho ",dañoHecho," puntos de daño")

def main():
    atacante = input("Dime el tipo del atacante: ")
    defensor = input("Dime el tipo del defensor: ")
    ataque = int(input("Dime los puntos de ataque: "))
    defensa = int(input("Dime los puntos de defensa: "))

    combatePokemon(atacante,defensor,ataque,defensa)
main()