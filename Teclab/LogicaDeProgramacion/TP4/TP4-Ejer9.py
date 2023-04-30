# Leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e
# imprimir el resultado. Ejemplo: 4*3 = 4 + 4 + 4 (4 sumado 3 veces).

# Entradas (Leer dos números)
nroA=int(input("Ingrese el Numero A (Por favor ingrese un numero positivo): "))  # Número A
nroB=int(input("Ingrese el Numero B (Por favor ingrese un numero positivo): "))  # Número B

# Vars
contA=0
contB=1
suma=0
sumando=()

# Inicio del bucle (comprobacion
while nroA < 0 or nroB < 0:
    
    # Compruebo si nroA es negativo
    while nroA < 0:
        print("El",nroA, "es negativo, por favor")
        nroA=int(input("Ingrese el Numero A (Por favor ingrese un numero positivo): "))
        
    # Compruebo si nroB es negativo
    while nroB < 0:
        print("El",nroA, "es negativo, por favor")
        nroB=int(input("Ingrese el Numero B (Por favor ingrese un numero positivo): "))
        
if nroB > 0:
        
    while contB <= nroB:
        suma = (suma + nroA)
        contB=contB+1
        sumando=sumando,nroA
        print
        
        
# Salida
print("El resultado es: ",nroA,"*",nroB,"=",suma)
print("El resultado es: ",nroA,"*",nroB,"=",sumando)