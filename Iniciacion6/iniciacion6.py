import json

#Ejercicio 1

"""def main():
    fichero = open("datos.json","r")
    dict = json.load(fichero)
    print(dict["nombre"])
    fichero.close()
main()"""
#Ejercicio 2

"""def main():
    diccionario = {
    "manzana": {"precio": 1.2, "stock": 50, "categoria": "fruta"},
    "banana": {"precio": 0.8, "stock": 40, "categoria": "fruta"},
    "leche": {"precio": 1.5, "stock": 30, "categoria": "lácteos"}}
    fichero = open("productos.json","w")
    json.dump(diccionario,fichero)
    fichero.close()
main()"""
#Ejercicio 3

"""def main():
    fichero = open("estudiantes.json","r")
    diccionario = json.load(fichero)
    notaMaxima = diccionario[0]["calificacion"]
    notaMinima = diccionario[0]["calificacion"]
    nombreMax = ""
    nombreMin = ""
    sumaNotas = 0
    for dict in diccionario:
        if dict["calificacion"] > notaMaxima:
            notaMaxima = dict["calificacion"]
            nombreMax = dict["nombre"]
        if dict["calificacion"] < notaMinima:
            notaMinima = dict["calificacion"]
            nombreMin = dict["nombre"]
        sumaNotas += dict["calificacion"]
    fichero.close()
    print("El alumno con la nota maxima es: ",nombreMax," con una nota de: ",notaMaxima)
    print("El alumno con la nota minima es: ",nombreMin," con una nota de: ",notaMinima)
    print("La media es: ",sumaNotas/len(diccionario))
main()"""
#Ejercicio 4

"""def main():
    fichero = open("Ejercicio3.json","r")
    diccionario = json.load(fichero)
    diccionario["ciudad"] = "Barcelona"
    fichero.close()
    fichero = open("Ejercicio3.json","w")
    json.dump(diccionario,fichero)
    fichero.close()
main()"""
#Ejercicio 5

"""def main():
    fichero = open("Ejercicio3.json","r")
    diccionario = json.load(fichero)
    fichero2 = open("Ejercicio4.json","r")
    diccionario2 = json.load(fichero2)
    fichero.close()
    fichero2.close()
    ficheroCombinado = open("Ejercicio5.json","w")
    json.dump([diccionario,diccionario2],ficheroCombinado)
    ficheroCombinado.close()
main()"""
#Ejercicio 6

"""def main():
    try:
        fichero = open("prueba.txt","r")
        diccionario = json.load(fichero)
        print("Json cargado correctamente: ",diccionario)
        fichero.close()
    except json.JSONDecodeError:
        print("Error al cargar Json")
main()"""
#Ejercicio 7

def main():
    fichero = open("empleados.json", "r")
    diccionario = json.load(fichero)
    empleados = {}
    for dict in diccionario:
        departamento = dict["departamento"]
        salario = dict["salario"]
        if departamento in empleados:
            empleados[departamento]["salarioTotal"] += salario
            empleados[departamento]["numeroEmpleados"] += 1
        else:
            empleados[departamento] = {"salarioTotal": salario, "numeroEmpleados": 1}
    medias = {}
    for departamento in empleados:
        media = empleados[departamento]["salarioTotal"] / empleados[departamento]["numeroEmpleados"]
        medias[departamento] = {"media": media}
    fichero.close()
    fichero = open("resumen_departamentos.json", "w")
    json.dump(medias, fichero)
    fichero.close()
main()
