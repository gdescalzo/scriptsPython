# Ingresar un número n, validar que sea positivo. Luego:
# a) Mostrar los primeros n números impares hasta el número ingresado.
#    Ejemplo:
#            •  Si se ingresa 5, se debe mostrar 1 3 5
#            •  Si se ingresa 8, se debe mostrar 1 3 5 7
#            •  Si se ingresa -5, se debe pedir otro número.
# b) Informar la suma de esos números impares.

# Vars
contPar=0
contImpar=0
nro=1
sumaImpar=0
resultImpares=0

# Compruebo el ingreso
if nro!=0:
    nro=int(input("Ingrese un numero positivo e impar a validar: "))                                                      # Entrada
    print(" ")
    
    # Verifico que el numero no sea negativo
    while nro<0:
        print("Usted ingreso un numero negativo, por favor ingrese valores positivos")
        nro=int(input("Ingrese un numero positivo e impar a validar: "))                                                  # Entrada
        print(" ")
    
    # Verifico que el numero no sea 0
    while nro == 0:
        print("Usted ingreso un 0, por favor ingrese valores positivos")
        nro=int(input("Ingrese un numero positivo e impar a validar: "))                                                  # Entrada
        print(" ")
        
    result=nro%2
     
    while result == 0:
       print(nro," es par, para continuar por favor ingrese un numero Impar")
       nro=int(input("Ingrese un numero positivo e impar a validar: "))                                                    # Entrada
       print(" ")
       result=nro%2

if result !=0:
    print(nro," es impar")
    while contImpar < (nro-1):       
        
        if contImpar !=0:
            resultImpar=contImpar%2
            if resultImpar !=0:
                #print(contImpar, end=' ')
                resultImpares=contImpar
                
        contImpar=contImpar+1
        
        if contImpar !=0:
            resultImpares=contImpar%2
            if resultImpares!=0:
                print(contImpar, end=' ')
                sumaImpar=contImpar+sumaImpar
        
    
    print("La suma de los numeros impares es: ", sumaImpar)