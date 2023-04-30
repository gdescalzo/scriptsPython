# Mostrar las tablas de multiplicar (entre 1 y 10) del número 4. ¿Cómo cambiaría el algoritmo
# para que el usuario pueda decidir la tabla de multiplicar a mostrar?

# Inicio | consulta al usuario
print("A continuacion se mostraran las tablas de multiplicar (entre 1 y 10) del número 4")
print("Desea elegir otra tabla de multiplicar ?")
print(" ")
print("IMPORTANTE: Si escribe cualquier otra cosa diferente a SI. Se mostrara por defecto la tabla del 4 ")
cond = str(input(" Ingrese \"SI\" si desea ver otra tabla : "))
print(" ")

# Posibles variantes de la variable del condicional
si=str("si")
Si=str("Si")
sI=str("sI")
SI=str("SI")

bucle = 1

# Decision del usuario
if cond == si or cond == Si or cond == sI or cond == SI:
    
    # Multiplica por N
    numN = int(input("ingrese un numero:"))
    
    while bucle <= 10:
        multiplicaN = numN * bucle
        print(multiplicaN)
        bucle = bucle +1    

else:
    
    # Multiplica por 4
    num4 = 4
    while bucle <= 10:
        multiplica = num4 * bucle
        print(multiplica)
        bucle = bucle +1