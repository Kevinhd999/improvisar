suma = 0

numero = int(input("Digite un numero (o negativo para acabar la suma)"))

while numero >= 0:
    suma += numero
    numero = int(input("Digite un numero (o negativo para acabar la suma)"))

print("La suma es:", suma)