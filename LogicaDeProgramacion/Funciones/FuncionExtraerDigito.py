# 2) Extraer un dígito de un número. La función recibe como parámetros dos números enteros, uno será del que se extraiga el dígito y el otro indica qué cifra se
#     desea obtener. La cifra de la derecha se considera la número 0. Retornar el valor -1 si no existe el dígito solicitado. Tener en cuenta que el número puede
#     ser positivo o negativo. Ejemplo:
#                                                                 extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8) devuelve -1.
#extracDig=int(input("Ingrese numero:"))
#cifraObtener=int(input("Indicar qué cifra se  desea obtener: "))

def extraerDigito (extracDig,cifraObtener):
    devuelve=-1
    
    for i in range (cifraObtener):
        extracDig=extracDig//10
        
    if extracDig == 0:
        #print(devuelve)
        return devuelve
    else:
        #print(extracDig)
        return extracDig

