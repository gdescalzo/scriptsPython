# Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
# •  Aplica el precio base a la primera docena de unidades.
# •  Aplica un 10% de descuento a todas las unidades entre 13 y 100.
# •  Aplica un 25% de descuento a todas las unidades por encima de las 100.
# Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El
# cálculo resultante sería:
#     
# 100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04
# 
# Escribir un algoritmo que lea la cantidad solicitada de un producto y su precio base, y muestre
# el valor total de la venta y el precio promedio por unidad. El fin de carga se determina
# ingresando -1 como cantidad solicitada.
# 
# Al finalizar informar:
# a) Cantidad de ventas realizadas total.
# b) Cantidad de ventas que se aplicaron un 10% de descuento.
# c) Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos.


precioBase=int(100) # Precio base
precioDes10=0
precioDes25=0

# Leer cant solicitada de producto
cantProd=int(input("Ingrese la cantidad solicitada de producto: "))
precioProd=int(input("Ingrese el precio base de producto: "))

if cantProd !=0 and cantProd!=-1:
    
    if cantProd <=12:
        # Aplica el precio base a la primera docena de unidades.
        for cont in range(1,13):
            print("Los productos",cont,"tiene precio base",precioBase)
        
    elif cantProd >12 and cantProd <=100:

        # Aplica el precio base a la primera docena de unidades.
        for cont in range(1,13):
            print("Los productos",cont,"tiene precio base",precioBase)

        # Aplica un 10% de descuento a todas las unidades entre 13 y 100.
        for cont in range(13,cantProd+1):
            precioDes10=precioProd*10/100
            print("Los productos",cont,"tiene precio con %10 de descuento",precioDes10)
    
    elif cantProd >100:
        
        # Aplica el precio base a la primera docena de unidades.
        for cont in range(1,13):
            print("Los productos",cont,"tiene precio base",precioBase)
            
        # Aplica un 10% de descuento a todas las unidades entre 13 y 100.
        for cont in range(13,101):
            precioDes10=precioProd*10/100
            print("Los productos",cont,"tiene precio con %10 de descuento",precioDes10)
            
        # Aplica un 25% de descuento a todas las unidades por encima de las 100.
        for cont in range(101,cantProd+1):
            precioDes25=precioProd*25/100
            print(cont,"tiene precio con %25 de descuento",precioDes25)

if cantProd == -1:
    print("usted ingreso -1 para finalizar")


