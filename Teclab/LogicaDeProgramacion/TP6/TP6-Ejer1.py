# Diseñar una función que reciba dos parámetros numéricos enteros, calcule y devuelva el
# resultado de la multiplicación de ambos utilizando sólo sumas.
# Desarrollar un programa principal para crear la siguiente serie numérica de N términos,
# comienza en uno y cada siguiente término se obtiene multiplicando el anterior por la ubicación:
#
#              1              2              6              24              120
#                           * 2            *3              *4                 *5

''' Importo libreria de Configuracion de Directorio '''
import sys
sys.path.append("/mnt/Storage2/Documentos/Personal/Facultad/UADE/2021/2do_Cuatrimestre/1. Fundamentos_de_Informática/Guia TP/Funciones")

''' Importo libreria de Multiplicacion '''
import FuncionCalcularMultiplicacionSumando

''' Importo libreria de nros aleatoreos '''
import random

# ## PROGRAMA PRINCIPAL
 
''' Defino variables globales '''
cont = 1
result = 1
nTermino = random.randint(1,100)
 
''' Condicion de verdad '''
while cont!=nTermino:
    result=FuncionCalcularMultiplicacionSumando.calcMult(result,cont)
    cont=cont+1
    print(result,end=' ')