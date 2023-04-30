# Escribir un algoritmo que lea números enteros hasta que se ingrese un 0, y muestre el máximo,
# el mínimo (sin considerar el 0) y la media (promedio) de todos ellos. Piense cómo debe
# inicializar las variables.

# lea números enteros hasta que se ingrese un 0

nro=int(input("Ingrese un numero: "))
cont=1
suma=0

while nro != 0:
    compara=nro
    
    if cont == 1:
        mayor=compara
        menor=compara
    elif compara>mayor:
        mayor=compara
    elif compara<menor:
        menor=compara
    
    nro=int(input("Ingrese un numero: "))
    suma=suma+compara
    cont=cont+1
    
prom=suma/(cont-1)

print(" ")
print(" ")
print("El mayor numero es",mayor)
print("El menor numero es",menor)
print("la suma es",suma)
print("El promedio es",prom)
    
        

            
                
        
    
    
