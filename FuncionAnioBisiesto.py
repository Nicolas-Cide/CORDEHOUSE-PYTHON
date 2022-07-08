# 1) Se elabora la funcion anioBisiesto para luego ser utilizada
def anioBisiesto(x):
    if ((x % 400) == 0):
        print("Es Bisiesto")
    elif ((x % 4) == 0 and (x % 100) != 0):
        print("Es Bisiesto")
    else:
        print("No es Bisiesto")


# 2) Se le pide al usuario que ingrese un año y se controla si es un numero o no.
its = False
while not(its):
    anio = input("Ingrese un año: ")
    try:
        int(anio)
        its = True
    except ValueError:
        print("Ingrese un numero!")


# 3) Se invoca la funcion anioBisiesto para mostrarle al usuario si lo es o no

anioBisiesto(int(anio))

