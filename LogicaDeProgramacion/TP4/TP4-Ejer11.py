# Cada cliente que va al banco Express, indica su número de documento y aguarda a ser atendido,
# cuando finaliza la atención del día se ingresa -1 para indicar que no hay más clientes para ser
# atendidos. El banco desea saber quién fue el primer cliente atendido y quién fue el último.

# Vars
dniCli=1
primerCliente=0
ultimoCliente=0
cont=0

# Inicio del Bucle (compruebo que el DNI no se 0 ni -1)
while dniCli !=0 and dniCli !=-1 and dniCli>0:
    
    # Solicito un numero
    dniCli=int(input("Ingrese su numero de DNI (solo numeros) :"))                               # Entrada
    
    if dniCli !=0 and dniCli !=-1 and dniCli>0:
        # Guardo el ultimo DNI
        ultiDniCli=dniCli
    
    # Compruebo que sea negativo
    while dniCli <0 and dniCli !=-1:
        print("Usted ingreso un numero negativo, por favor ingrese un DNI valido (positivo)")
        dniCli=int(input("Ingrese su numero de DNI (solo numeros) :"))                           # Entrada
        
        if dniCli !=0 and dniCli !=-1 and dniCli>0:
            # Guardo el ultimo DNI
            ultiDniCli=dniCli

    # Compruebo que sea negativo o "0"
    while dniCli ==0 or dniCli<0 and dniCli !=-1:
        print("Usted ingreso un numero negativo, o 0, por favor ingrese un DNI valido (positivo)")
        dniCli=int(input("Ingrese su numero de DNI (solo numeros) :"))                           # Entrada
        
        if dniCli !=0 and dniCli !=-1 and dniCli>0:
            # Guardo el ultimo DNI
            ultiDniCli=dniCli
    
    # Cuento los clientes
    cont=cont+1
    
    # Filtro entre el primer cliente y el ultimo
    if cont==1:
        primerCliente=dniCli
    elif dniCli == -1:
        ultimoCliente=ultiDniCli

cont=cont-1

print(" ")
print("La cantidad de clientes atendidos es: ", cont)                                             # Salida
print("El primer cliente atiendo fue: ",primerCliente)                                            # Salida
print("El utilmo cliente atiendo fue: ",ultimoCliente)                                            # Salida
    