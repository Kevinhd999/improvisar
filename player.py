numero = int(input("Digite un numero "))

match numero:
    case 0:
        print("El numero es 0")
    case numero if numero < 10:
        print("El numero es menor que 10")
    case numero if numero >= 10:
        print("El numero es mayor o igual que 10")
    case _:
        print("Numero no reconocido")