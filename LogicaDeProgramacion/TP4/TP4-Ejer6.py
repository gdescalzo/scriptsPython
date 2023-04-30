# Ingresar números, hasta que la suma de los números pares supere 100. Mostrar Cuántos
# números en total se ingresaron.

suma = 0
cont=1

while suma <100:
    nro=int(input("Ingrese un numero: "))
    cont=cont+1 
    
    if nro>=100:
        nro=int(input("Ingrese un numero menor a 100: "))
        cont=cont+1 
        if nro!=100:
            suma=suma+nro 
    elif (nro % 2)==0:
        suma=suma+nro

cont=cont-1

print("se ingresaron en total", cont)
    




