# Diseñar una función que reciba dos números enteros como parámetros enteros A y B, y permita
# obtener AB mediante multiplicaciones sucesivas.
# Desarrollar un programa principal para generar N veces dos valores al azar en un rango desde-hasta
# ingresado por teclado y calcular AalaB, mostrar por pantalla los valores creados y el resultado de la operación.

''' Importo libreria de configuracion de directorio '''
import sys
sys.path.append("/mnt/Storage2/Documentos/Personal/Facultad/UADE/2021/2do_Cuatrimestre/1. Fundamentos_de_Informática/Guia TP/Funciones")

''' Importo libreria para calcular el exponente multiplicando'''
import FuncionCalcularExponenteMultiplicando

''' Importo libreria para crear numeros aleatoreos '''
import random

'''Importo libreria para validar que el nro sea positivo'''
import FuncionValidadQseaPositivo

## PROGRAMA PRINCIPAL

''' Variables Globales '''
nVeces = random.randint(1,99)

''' Ingresos por teclado '''
valorDsd = FuncionValidadQseaPositivo.ingresarPositivo("Ingrese desde que numero: ")
valorHasta = FuncionValidadQseaPositivo.ingresarPositivo("Ingrese hasta que numero: ")

for i in range(valorDsd,valorHasta):
    valor1 = random.randint(1,99)
    valor2 = random.randint(1,99)
    
    result=FuncionCalcularExponenteMultiplicando.calcExpon(valor1,valor2)
    
    print("El nro",valor1,"elevado a",valor2,"es igual a:",result)
    
    
    


