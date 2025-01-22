numero = int(input("Digita un numero"))

match numero:
    case 0:
        print("El numero es cero")
    case numero if numero % 2 == 0:
        print("El numero es par")
    case numero if numero % 2 != 0:
        print("El numero es impar")
    case _:
        print("Numero no reconocido")
