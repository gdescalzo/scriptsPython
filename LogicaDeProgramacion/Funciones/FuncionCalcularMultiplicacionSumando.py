# Diseñar una función que reciba dos parámetros numéricos enteros, calcule y devuelva el
# resultado de la multiplicación de ambos utilizando sólo sumas.

def calcMult (a,b):
    suma=0
    for i in range(b):
        suma=a+suma
        
    return suma