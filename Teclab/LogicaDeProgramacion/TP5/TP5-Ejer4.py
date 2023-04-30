# Una empresa factura a sus clientes el último día de cada mes. Si el cliente paga su factura
# dentro de los primeros 10 días del mes siguiente, tiene un descuento de $120 o del 2% de la
# factura, lo que resulte más conveniente para el cliente. Si paga en los siguientes 10 días del
# mes deberá pagar el importe original de la factura, mientras que si paga después del día 20
# deberá abonar una multa de $150 o del 10% de su factura, lo que resulte mayor. Escriba un
# algoritmo que lea el número del cliente y el total de la factura, y emita un informe donde conste
# el número del cliente y los tres importes que podrá abonar según la fecha de pago.


nroCliente=int(input("Ingrese el numero de cliente: "))
totalFactura=float(input("Total de la factura: "))
print ()

primeros10 = totalFactura*(2/100)
siguientes10 = totalFactura
despues20= totalFactura*(10/100)
descuento=120
multa=150

if primeros10 >= descuento:
    print ("Al cliente le conviene utilizar el descuento del 2% del total de su facutura: \t\t\t",primeros10)
else:
    print ("Al cliente le conviene utilizar el descuento de : \t\t\t",descuento)

print ("Pago del 1 al 10, deberá pagar el importe original de la factura: \t",siguientes10)

if despues20 <= multa:
    print ("Al cliente le conviene pagar la multa del 2% del valor total de la factura: ",despues20)
else:
    print("Al cliente le conviene pagar la multa: \t\t\t\t\t",multa)