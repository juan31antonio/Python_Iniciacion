#Ejercicio 1

"""tablero = [["*","*","*"],["*","*","*"],["*","*","*"]]

def juego():
    print("Va a empezar el juego, empieza O")
    juegoEmpezado = True
    turno1 = True
    print("    0    1     2\n0",tablero[0],"\n1",tablero[1],"\n2",tablero[2])
    while juegoEmpezado:
        try:
            respuesta = input("Dime la fila y la columna de la siguiente forma 'columna:fila' : ")
            posicion = respuesta.split(":")
            if turno1:
                if tablero[int(posicion[1])][int(posicion[0])] != "*":
                    print("El jugador 1 ha intentado hacer trampas, juagdor 2 gana")
                    break
                else:
                    tablero[int(posicion[1])][int(posicion[0])] = "O"
                    turno1 = False
            else:
                if tablero[int(posicion[1])][int(posicion[0])] != "*":
                    print("El jugador 2 ha intentado hacer trampas, juagdor 2 gana")
                    break
                else:
                    tablero[int(posicion[1])][int(posicion[0])] = "X"
                    turno1 = True

            print("    0    1     2\n0",tablero[0],"\n1",tablero[1],"\n2",tablero[2])
            
            for i in range(0,3):
                if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0]!= "*":
                    usuario = tablero[i][0]
                    if usuario == "X":
                        usuario = "2"
                    else: usuario = "1"
                    print("El usuario: ",usuario," ha ganado")
                    juegoEmpezado = False
                    break
                if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i]!= "*":
                    usuario = tablero[i][0]
                    if usuario == "X":
                        usuario = "2"
                    else: usuario = "1"
                    print("El usuario: ",usuario," ha ganado")
                    juegoEmpezado = False
                    break
                if (tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[1][1]!= "*") or (tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[1][1]!= "*"):
                    usuario = tablero[1][1]
                    if usuario == "X":
                        usuario = "2"
                    else: usuario = "1"
                    print("El usuario: ",usuario," ha ganado")
                    juegoEmpezado = False
                    break

            if not any('*' in fila for fila in tablero):
                if juegoEmpezado:
                    print("El juego ha acabado en empate")
                    break
                else:
                    print("El juego ha acabado")
                    break
        except:
            if turno1:
                print("El jugador 1 ha intentado hacer trampas, el jugador 2 gana")
                break
            else:
                print("El jugador 2 ha intentado hacer trampas, el jugador 1 gana")
                break
juego()"""

"""Tiempo estimado 30-40 mins"""
#Ejercicio 2
"""dHexadecimal = {
  "A": 10,
  "B": 11,
  "C": 12,
  "D": 13,
  "E": 14,
  "F": 15
}

hexaBinario = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

hexadecimal = ["1A", "2F", "B4", "FF", "00", "5D"]



tupla = ()

def hexaADecimal(hexadecimalLista):
    maximoValor = 0
    numMaximo = ""
    for num in hexadecimalLista:
        total = 0
        numInvertido = num[::-1]
        for i in range(len(numInvertido)):
            digito = numInvertido[i]
            if digito.isdigit():
                total += int(digito) * 16 ** i
            else:
                total += dHexadecimal[digito] * 16 ** i
        if total > maximoValor:
            maximoValor = total
            numMaximo = num
    tupla = (maximoValor, numMaximo)
    print(tupla)
hexaADecimal(hexadecimal)

def hexadecimalABinario(numero):
    binario = ""
    for num in numero: 
        binario += hexaBinario[num]  
    print(binario)
hexadecimalABinario("4F")

def binarioADecimal(binario):
    total = 0
    binario = binario[::-1] 
    for numero in range(len(binario)):
        if binario[numero] == '1':
            total += 2 ** numero
    print(total)
binarioADecimal("10100001")"""
"""Tiempo estimado 30 mins"""
#Ejercicio 3
cine = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]

def gestionCine():
    reserva = True
    while reserva:
        print("\n",cine[0],"\n",cine[1],"\n",cine[2],"\n",cine[3],"\n",cine[4])
        reservar = input("Dime que silla quieres reservar columna:fila  o salir para terminar la reserva: ")
        if reservar.lower() == "salir":
            reserva = False
            break
        try:
            posicion = reservar.split(":")
            fila = int(posicion[0])
            columna = int(posicion[1])
            
            if fila < 0 or fila >= len(cine) or columna < 0 or columna >= len(cine[0]):
                print("Fila o columna no validas. Introduce valores dentro del rango")
            elif cine[fila][columna] == "O":
                print("Esa butaca ya esta reservada")
            else:
                cine[fila][columna] = "O"
                print("\n",cine[0],"\n",cine[1],"\n",cine[2],"\n",cine[3],"\n",cine[4])
                respuesta = input("Quieres hacer otra reserva? s/n: ")
                if respuesta.lower() == "n":
                    reserva = False

        except (ValueError, IndexError):
            print("Entrada no valida")
    print("Cerrado reserva de entradas")
gestionCine()