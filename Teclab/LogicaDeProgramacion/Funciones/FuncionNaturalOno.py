# 1) Diseñar una función que solicite por teclado un número y lo retorne solo si el número
#      ingresado es natural, caso contrario la función deberá seguir solicitando el número.

def esNatural (mensaje):
    nro=float(input("Ingrese un numero: "))
    result=nro%1
    
    while result!= 0:
        nro=float(input("Ingrese un numero: "))
        result=nro%1
        
    nro=int(nro)
    return (nro)
    #print (nro,"es natural")