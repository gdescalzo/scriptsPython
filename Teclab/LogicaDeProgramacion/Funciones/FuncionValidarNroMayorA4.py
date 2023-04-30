
''' Verifica que el nro ingresado no sea mayor a 4 '''


def mayor_acuatro(a):
    while a > 4:
        print("El numero ingresado es mayor a 4")
        a = int(input("Ingrese un nro, menor a 4: "))
    return a
