# Paso 1: Crear una lista de números
numeros = [10, 20, 30, 40, 50]

# Paso 2: Inicializar la variable suma en 0
suma = 0

# Paso 3: Utilizar un ciclo for para sumar los números en la lista
for numero in numeros:
    suma += numero

# Paso 4: Calcular el promedio dividiendo la suma entre la cantidad de números
promedio = suma / len(numeros)

# Paso 5: Imprimir el resultado
print("El promedio de los números en la lista es:", promedio)

