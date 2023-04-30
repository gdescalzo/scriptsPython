# 1) Función para sumar los dígitos de un número. Recibe un número y retorna la suma de los dígitos. (NO utilizar cadenas de caracteres str, para lograr el objetivo)

def sumarDigitos (nro):
    #nro=input(mensaje)
    sumaNro=0
    
    while nro>10:
        descomponeNro1= nro%10
        nro=nro//10
        sumaNro=sumaNro+descomponeNro1
        
    sumaNro=sumaNro+nro
    return sumaNro
    