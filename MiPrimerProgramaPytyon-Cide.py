print("---- Se da inicio al programa que calcula la nota final del alumno en base a 2 notas ----")

Nota1 = int(input("Ingresar Nota 1: "))
Nota2 = int(input("Ingresar Nota 2: "))
PorcNota1 = 40
PorcNota2 = 60

ResNota1 = (PorcNota1*Nota1)/100
ResNota2 = (PorcNota2*Nota2)/100
NotaFinal = ResNota1 + ResNota2

print("La nota final del alumno es: " + str(float(NotaFinal)))