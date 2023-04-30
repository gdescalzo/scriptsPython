# Un negocio desea saber el importe total recaudado al fin del día, desea contar con un programa
# que pueda ingresar el importe de cada venta realizada. Para indicar que finalizó el día se ingresa
# -1. ¿Cuál fue el monto total vendido y cuántas ventas se realizaron? El importe de cada venta
# realizada debe ser un valor positivo.

# Vars:
cont=0
ventaRealizada=0
suma=0

# Inicio del Bucle
while ventaRealizada != -1:
    
    # Importe ventas realizadas (debe ser positivo)
    ventaRealizada=int(input("Ingrese monto (positivo) de venta se realizada: "))      # Entrada
    print(" ")
    
    # Verifica que sea positivo y distinto de -1
    if ventaRealizada < 0 and ventaRealizada != -1:
        print("Error - Usted ingreso un numero negativo, para el monto, por favor.")
        ventaRealizada=int(input("Ingrese monto (positivo) de venta se realizada: "))  # Entrada
        print(" ")

        if ventaRealizada != 0 and ventaRealizada != -1 and ventaRealizada > 0:
            suma = suma + ventaRealizada

    # Verifica que sea distinto de 0
    elif ventaRealizada == 0 and ventaRealizada != -1:
        
        print("Error - Usted ingreso es \"0\", para el monto, por favor.")
        ventaRealizada=int(input("Ingrese monto (positivo) de venta se realizada: "))  # Entrada
        print(" ")
        
        if ventaRealizada != 0 and ventaRealizada != -1 and ventaRealizada > 0:
            suma = suma + ventaRealizada

    # Verifica que sea positivo
    elif ventaRealizada > 0:
        
        # Sumo las ventas realizadas.
        suma = suma + ventaRealizada
        
    # Finaliza programa con -1
    elif ventaRealizada == -1:

        print("Usted finalizo el programa")
        print(" ")
    
    # Cuento cant de ventas realizadas
    if ventaRealizada != 0 and ventaRealizada != -1 and ventaRealizada > 0:
        cont=cont+1
        
# Muestro cant de ventas realizadas
print("La cantidad de ventas realizadas fueron: ", cont)                                  # Salida

# Muestro importe total
print("El monto total de ventas realizadas es: ", suma)                                   # Salida




