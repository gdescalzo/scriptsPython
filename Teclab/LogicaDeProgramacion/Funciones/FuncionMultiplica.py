# Hora de jugar: Una calculadora tiene cuatro operaciones básicas (a saber: sumar, restar,
# multiplicar, dividir). Desarrolle una función para realizar cada operación, que reciba como
# parámetros dos números ingresados por el usuario y devuelva el resultado de la operación.
# Resuelva la división por restas sucesivas (investigar cómo se resuelve).

def operacionMultiplica (mensaje):
    mult=float(input("Ingrese el primer numero: "))
    nro2=float(input("Ingrese el siguiente numero, o ingrese 0 para finalizar: "))
    cont=0
    
    while nro2 !=0:
        if cont!=0:
            nro2=float(input("Ingrese el siguiente numero, o ingrese 0 para finalizar: "))
        
        if nro2 !=0:
            mult=mult*nro2
            cont=cont+1
        
        print(mult)