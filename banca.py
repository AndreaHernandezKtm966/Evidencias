import random
ganadas = 0
perdidas = 0
empate = 0

while True:
    banca = random.randint(1,13)
    jugador = int(input("ingrese un numero"))

    if banca > jugador:
        print("perdio")
        perdidas += 1
    elif jugador > banca:
        print("ganaste")
        ganadas += 1
    elif jugador == banca:
        print("empate")
        empate += 1

    if ganadas == 5:
        print(f"ganaste el juego 5 ganadas{ganadas} y empataste{empate}, perdiste {perdidas}")
        break
    elif perdidas == 3:
        print(f"perdiste el juego 3 perdidas{perdidas} y empataste{empate}, perdiste {ganadas}")
        break

    continua = input("quieres retirarse? si/no?: ")
    
    if continua == "si":
        print("gracias por jugar")
        break 