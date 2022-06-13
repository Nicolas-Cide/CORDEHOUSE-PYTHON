print("---- Se da inicio al programa que calcula la nota final del alumno en base a 2 notas ----")

Nota1 = int(input("Ingresar Nota 1: "))
Nota2 = int(input("Ingresar Nota 2: "))
PorcNota1 = int(input("Ingrese porcentaje de Nota 1: "))
PorcNota2 = int(input("Ingrese porcentaje de Nota 2: "))

PorcNota1 = PorcNota1/100
PorcNota2 = PorcNota2/100

NotaFinal = ((PorcNota1*Nota1)+(PorcNota2*Nota2))

print("La nota final del alumno es: " + str(float(NotaFinal)))