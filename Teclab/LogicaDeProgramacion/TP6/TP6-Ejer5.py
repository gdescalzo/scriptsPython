# Desarrollar dos funciones:
# 1) Diseñar una función que solicite por teclado un número y lo retorne solo si el número
#      ingresado es natural, caso contrario la función deberá seguir solicitando el número.
# 2) Función para sumar los primeros N números naturales de un valor. Retorna la suma.
#
# Desarrollar un programa principal para ingresar una cantidad de valores naturales (la cantidad
# se solicita al usuario). Para cada valor informar la suma de los primeros N valores naturales.
# Al finalizar informar cuántos valores se ingresaron y cuál es el mayor valor ingresado.

import sys
sys.path.append("/mnt/Storage2/Documentos/Personal/Facultad/UADE/2021/2do_Cuatrimestre/1. Fundamentos_de_Informática/Guia TP/Funciones")

import FuncionMostrarMensaje
import FuncionNaturalOno
import FuncionValidadQseaPositivo
import FuncionSumarDigitosDunNro

# PROGRAMA PRINCIPAL
FuncionMostrarMensaje.mostrarMensaje("Ejercicio 5")
cantValores=FuncionValidadQseaPositivo.ingresarPositivo("Ingrese la cantidad de valores:  ")
sumar=0
cont=0
sumador=0
mayorValor=0

for i in range(cantValores):
    valor=FuncionNaturalOno.esNatural("Ingrese un valor: ")
    sumar=FuncionSumarDigitosDunNro.sumarDigitos(valor)
    print("El valor:",valor,"la suma de los primeros valores naturales, es:",sumar)
    cont=cont+1
    
    if sumador < valor :
        mayorValor=valor
    
    sumador=valor

print()
print("La cantidad de valores ingresados es:" ,cont,"el mayor valor es:",mayorValor)