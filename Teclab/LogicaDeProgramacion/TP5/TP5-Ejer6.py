# Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y un número
# entero N que representa una cantidad de días. Realizar un programa que imprima la nueva
# fecha que resulta de sumar N días a la fecha dada. Tener en cuenta los años bisiestos tal como
# se detalla en el ejercicio 9 de la práctica 3.

nroD=int(input("Ingrese Nro de dia: "))
# # Verificamos que el usuario ingrese numeros entre 1 y 31 para los dias 
# while nroD < 1 or nroD >31:
#     print("Usted ingreso un Nro de dia fuera del rango de los meses '(31)', por favor")
#     nroD=int(input("Ingrese Nro de dia: "))

nroM=int(input("Ingrese Nro de mes: "))
# # Verificamos que el usuario ingrese numeros entre 1 y 12 para el mes
# while nroM < 1 or nroM >12:
#     print("Usted ingreso un Nro de mes fuera del rango de los años '(12)', por favor")
#     nroD=int(input("Ingrese Nro de mes: "))

nroA=int(input("Ingrese Nro de año: "))
# # Verificamos que el usuario ingrese numeros mayores a 1
# while nroA < 1:
#     print("Usted ingreso un Nro de año invalido '(negativo o menor a 0)', por favor")
#     nroD=int(input("Ingrese Nro de año: "))

# print() # Espaciador
print("Usted ingreso la fecha:",nroD,"/",nroM,"/",nroA)
print() # Espaciador

nroN=int(input("Ingrese Nro de dias a sumar: "))
# # Verificamos que el usuario ingrese numeros mayores a 1
# while nroN < 1:
#     print("Usted ingreso un Nro de dias a sumar '(negativo o menor a 0)', por favor")
#     nroN=int(input("Ingrese Nro de dias a sumar: "))

suma=0
sumaDias=0

for nDias in range(nroD,32):
    
    suma=nDias+1
    
    if suma >= 31:
        nroN=nroN-31
        for nDias1 in range(sumaDias,nroN):
            
            if nroM == 1 or nroM == 3 or nroM == 5 or nroM == 7 or nroM == 10 or nroM == 12:
                #print("El Nro de mes ingresado",nroM,"es de 31 dias")
                
                if suma == 31:
                    nroM=nroM+1
                    print("El numero de mes es: ", nroM)
                    
            elif nroM == 4 or nroM == 6 or nroM == 9 or nroM == 11:
                #print("El Nro de mes ingresado",nroM,"es de 30 dias")
                
                if suma == 30:
                    nroM=nroM+1
                    print("El numero de mes es: ", nroM)           
            
        
    
    print(suma)








# Comprobamos si el mes es de 31 dias
#if nroM == 1 or nroM == 3 or nroM == 5 or nroM == 7 or nroM == 10 or nroM == 12:
#    print("El Nro de mes ingresado",nroM,"es de 31 dias")
# 
# # Comprobamos si el mes es de 30 dias
# elif nroM == 4 or nroM == 6 or nroM == 9 or nroM == 11:
#     print("El Nro de mes ingresado",nroM,"es de 30 dias")
# 
# # Comprobamos si el mes es de 28 dias
# elif nroM == 2:
#     print("El Nro de mes ingresado",nroM,"es de 28 dias")
#     
# else:
#     print("El Nro de mes ingresado",nroM,"no es valido")
    

