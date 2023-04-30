# El factorial de un número entero N mayor que cero se define como el producto de todos los
# enteros X tales que 0 < X <= N. Desarrollar un programa para calcular el factorial de un número
# dado hasta ingresar -1. Deberán rechazarse las entradas inválidas (menores que 0). Al finalizar
# informar cuantas veces se calculó el factorial.

# Variable de entrada
nro=1

while nro!=0 and nro!=-1:
    
    # Variables Globales
    contMulti=1
    factorNro=1
    
    # Entrada
    nro=int(input("Ingrese un numero para realizar su factorial: "))
    
    # Verificamos que no sea negativo.
    while nro < 0 and nro !=-1:
        print("Usted ingreso un numero negativo, por favor")
        nro=int(input("Ingrese un numero para realizar su factorial: "))
    
    # Finaliza el programa con -1    
    if nro == -1:
        
        print("Usted ingreso -1 para finalizar el programa")
    
    # Realizamos su factorial
    else:
        
        for nroX in range (1,nro):

            contMulti=contMulti+1
            nroXb=contMulti
            factorNro=factorNro*nroXb
            
        print("su factorial: ",factorNro)