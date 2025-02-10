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
#Ejercicio 3