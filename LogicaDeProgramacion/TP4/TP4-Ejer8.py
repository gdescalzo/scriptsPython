# Se desea analizar cuántos autos circulan con patente que tiene numeración par y cuántos con
# numeración impar en un día. Le solicitan escribir un algoritmo que permita ingresar la
# terminación de la patente (entre 0 y 9) hasta ingresar -1 e informar cuántas se ingresaron con
# numeración par y cuántas con numeración impar.

# Vars
contPar=0
contInpar=0
terPatente=0

while terPatente!=-1:
    
    # Terminación patente
    terPatente=int(input("Ingrese el numero de terminacion de la patente: "))                          # Entrada
    print(" ")
    
    # Compruebo si es impar
    if terPatente == 0 or terPatente == 2 or terPatente == 4 or terPatente == 6 or terPatente == 8 and terPatente < 10:
        print("La patente ingresada es par", terPatente)
        print(" ")
        
        contPar=contPar+1
        
    # Compruebo si es impar
    elif terPatente == 1 or terPatente == 3 or terPatente == 5 or terPatente == 7 or terPatente == 9 and terPatente < 10:
        print("La patente ingresada es inpar", terPatente)
        print(" ")
        
        contInpar=contInpar+1
    
    # Compruebo si es -1
    elif terPatente == -1:
        
        # -1 finaliza el programa
        print("Usted finalizo el programa con -1")
        print(" ")
    
    # Compruebo si es de dos digitos
    elif terPatente > 10:
        print("Ingrese numeros del 0 al 9")
        print(" ")
       
# Salidas (cuántos autos circulan)
print("La cantidad de autos con patente de numeración par circulan es: ", contPar)                         # patente numeración par
print("La cantidad de autos con patente de numeración inpar circulan es: ", contInpar)                     # patente numeración impar

