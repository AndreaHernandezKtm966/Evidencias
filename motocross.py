total = 0

print("escoja una de las siguientes opciones")
print("1 hora ($ 40.000)")
print("2 hora ($60.000)")
print("3 hora ($80.000)")
print("0. fin de horas")

while True:
    opcion = int(input("digite algunas de las opciones"))

    match opcion:
        case 1:
            print("has seleccionado la primera opcion y su valor es: $40.000")
            total += 40.000

        case 2:
           print("has seleccionado la segunda opcion y su valor es: $60.000")
           total += 60.000
        case 3:
            print("has seleccionado la tercera opcion y su valor es: $80.000")
            total += 80.000
        case 0:
            print("su compra fue finalizada")
            print("el total apagar es ",total)
            break
        case _:
            print("la opcion que seleccionaste no existe")

 
            print(f"total a pagar",total)