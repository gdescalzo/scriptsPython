# Leer números que representan edades de un grupo de personas, finalizando la lectura cuando
# se ingrese el número 999. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o
# más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad
# válida. (Se considera válido una edad entre 0 y 100).

# Vars
nro=0
contMas18=0
contMenos18=0
sumaMayores=0
sumaMenores=0

# Mensaje a usuario
print("A continuacion se leeran los numeros que se ingresan por teclado y se calcularan el promedio de mayores de 18 y menores de 18 ")
print("Para finalizar ingrese 999")
print(" ")

# Inicio del Bucle
# Compruebo que sea positivo ; que no sea 999 y que sea menor o = a 100
while nro!=999 and nro>=0: #and nro<100:
    
    # Leer números de edades
    nro=int(input("Ingrese un numero de edad, (positivo, entre 0 y 100): "))

    # Verifico que la edad no sea mayor a 100 años y no sea un numero negativo
    if nro > 100 and nro!=999 or nro <0 and nro!=999:
        
        # Verifico que la edad no sea mayor a 100 años.
        while nro > 100 and nro!=999:
            print(" ")
            print("Usted ingreso una edad mayor a 100, por favor ingrese un edad entre 0 y 99")
            nro=int(input("Ingrese un numero de edad, (positivo, entre 0 y 100): "))
            
            # Verifico que sea Menor a 18
            if nro < 18 and nro!=999 and nro>=0 and nro<=100:
                print("es menor a 18")
                
                # cuento las veces y las posiciones de ingreso.
                contMenos18=contMenos18+1
                
                # sumo los menores de 18 años
                sumaMenores=nro+sumaMenores
 
            # Verifico que sea Mayor a 18
            elif nro > 18 and nro!=999 and nro>=0 and nro<100:
                print("es mayor a 18")
                
                # cuento las veces y las posiciones de ingreso.
                contMas18=contMas18+1
                
                # sumo los menores de 18 años
                sumaMayores=nro+sumaMayores
 
        # Verifico que la edad no sea un numero negativo.    
        while nro < 0 and nro!=999:
            print(" ")
            print("Usted ingreso numero negativo, por favor ingrese un edad entre 0 y 99")
            nro=int(input("Ingrese un numero de edad, (positivo, entre 0 y 100): "))

            # Verifico que sea Menor a 18
            if nro < 18 and nro!=999 and nro>=0 and nro<=100:
                print("es mayor a 18")
                
                # cuento las veces y las posiciones de ingreso.
                contMenos18=contMenos18+1
                
                # sumo los menores de 18 años
                sumaMenores=nro+sumaMenores
 
            # Verifico que sea Mayor a 18
            elif nro > 18 and nro!=999 and nro>=0 and nro<100:
                print("es menor a 18")
                
                # cuento las veces y las posiciones de ingreso.
                contMas18=contMas18+1
                
                # sumo los menores de 18 años
                sumaMayores=nro+sumaMayores
    
    # Si es correcto el ingreso de usuario (osea si no es negativo, si no es mayor a 100)
    elif nro > 0  and nro!=999:
        
        if nro > 0 and nro!=999:
            
            # Verifico que sea Menor a 18
            if nro < 18 and nro!=999 and nro>=0: #and nro<=100:
                print("es Menor a 18")
                
                # cuento las veces y las posiciones de ingreso de los menores.
                contMenos18=contMenos18+1
                
                # sumo los menores de 18 años
                sumaMenores=nro+sumaMenores
 
            # Verifico que sea Mayor a 18
            elif nro > 18 and nro!=999 and nro>=0 and nro<100:
                print("es Mayor a 18")
                
                # cuento las veces y las posiciones de ingreso de los mayores.
                contMas18=contMas18+1
                
                # sumo los mayores de 18 años
                sumaMayores=nro+sumaMayores
                
    # Finaliza programa
    elif nro == 999:
        print("Usted ingreso una edad mayor a 999 para finalizar")
        
        if contMenos18 !=0:
            # Calculo el promedio de las edades menores a 18 años
            promMenores=sumaMenores/contMenos18
            print("el promedio de edad de las personas con menos de 18 años es: ",promMenores)        # Salida
            
            # Imprimo cuántos son menores de 18 años
            print("Los menores a 18 años, son: ", contMas18)                                          # Salida
            
        if contMas18 !=0:
            # Calculo el promedio de las edades mayores a 18 años
            promMayores=sumaMayores/contMas18
            print("el promedio de edad de las personas con mas de 18 años es: ",promMayores)          # Salida
            
            # Imprimo cuántos son mayores de 18 años
            print("Los mayores a 18 años, son: ", contMenos18)                                        # Salida
    