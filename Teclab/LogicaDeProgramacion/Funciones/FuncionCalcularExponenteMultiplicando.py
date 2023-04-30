# Diseñar una función que reciba dos números enteros como parámetros enteros A y B, y permita
# obtener AalaB mediante multiplicaciones sucesivas.

def  calcExpon(a,b):
    multiplica = 1
    for i in range(b):
        multiplica = a * multiplica
        
    return multiplica
    