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

lista_animales = [
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
ejer2(1977)

#Ejercicio 3
