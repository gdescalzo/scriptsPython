# Hora de jugar: Una calculadora tiene cuatro operaciones básicas (a saber: sumar, restar,
# multiplicar, dividir). Desarrolle una función para realizar cada operación, que reciba como
# parámetros dos números ingresados por el usuario y devuelva el resultado de la operación.
# Resuelva la división por restas sucesivas (investigar cómo se resuelve).

def dividoRestando (mensaje):
    nro1=float(input("Ingrese un numero: "))
    nro2=float(input("Ingrese dividendo, o ingrese 0 para finalizar: "))
        
    cont=0
    result=0
    
    while nro1 !=0  and nro1>0 :
        nro1=nro1-nro2
        cont=cont+1
    
    result=cont
    print ('''El resultado de la division es: ''', result,'''
''')


