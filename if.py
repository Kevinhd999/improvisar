nota1 = float(input("Digite la nota 1 "))

nota2 = float(input("Digite la nota 2 "))

nota3 = float(input("Digite la nota 3 "))

promedio = (nota1 + nota2 + nota3) / 3


print("El promedio de las notas es:", promedio)

if promedio > 10:
    print("Estan mal digitadas las notas")
elif promedio == 10:
    print("El alumno aprobó con una calificación perfecta.")
elif promedio >= 9:
    print("El alumno aprobó con una calificación sobresaliente.")
elif promedio >= 7:
    print("El alumno aprobó satisfactoriamente.")
elif promedio >= 6:
    print("El alumno necesita mejorar un poco.")
else :
    print("El alumno reprobó.")

