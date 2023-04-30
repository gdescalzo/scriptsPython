# Leer 10 números enteros e imprimir el promedio, el mayor y en qué orden fue ingresado el
# mayor valor, si se ingresó más de una vez debe informar el primer ingreso.

bucle=1
suma=0
mayor=0
orden=0

while bucle <= 10:
    # leer 10 números enteros
    print("Ingrese el numero", bucle)
    num=int(input(": ")) # Entradas
    print(" ")
    
    # mayor
    while num > mayor:
        mayor= num
        orden = bucle

    # los sumo
    suma = suma + num
    
    bucle = bucle + 1
    
# promedio
prom=suma/10

# Salida
print(" ")
print("La suma es: ", suma,"y su promedio es: ",prom)
print("El mayor es numero ingresado es: ", mayor, "y fue ingresado en el orden: ",orden )





    
    
    
    
    