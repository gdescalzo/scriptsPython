# 1) Función para sumar los dígitos de un número. Recibe un número y retorna la suma de los dígitos. (NO utilizar cadenas de caracteres str, para lograr el objetivo)
#
# 2) Extraer un dígito de un número. La función recibe como parámetros dos números enteros, uno será del que se extraiga el dígito y el otro indica qué cifra se
#     desea obtener. La cifra de la derecha se considera la número 0. Retornar el valor -1 si no existe el dígito solicitado. Tener en cuenta que el número puede
#     ser positivo o negativo. Ejemplo:
#                                                                 extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8) devuelve -1.
# Desarrollar un programa para generar valores al azar de 5 dígitos hasta que el dígito central
# sea cero. Mostrar por pantalla este número y la suma de sus dígitos utilizando ambas funciones
# creadas y no olvidar mostrar un título al inicio utilizando la función del ejercicio 3

''' Cargo la carpeta raiz con todas las funciones '''
import sys
sys.path.append("/mnt/Storage2/Documentos/Personal/Facultad/UADE/2021/2do_Cuatrimestre/1. Fundamentos_de_Informática/Guia TP/Funciones")

import FuncionSumarDigitosDunNro
import FuncionExtraerDigito
import FuncionMostrarMensaje
import random

# PROGRAMA PRINCIPAL
pSuma=1

FuncionMostrarMensaje.mostrarMensaje("Ejercicio 4")   

while pSuma != 0:
    valAzar=random.randint(10000,99999)
    pSuma=FuncionExtraerDigito.extraerDigito(valAzar,2)%10
    print("El numero al azar es:",valAzar,"tiene un",pSuma,"en su quinta cifra")

suma=FuncionSumarDigitosDunNro.sumarDigitos(valAzar)
print()
print("El numero al azar es:",valAzar,"tiene un",pSuma,"en su quinta cifra, y la suma de sus numeros es:",suma)

