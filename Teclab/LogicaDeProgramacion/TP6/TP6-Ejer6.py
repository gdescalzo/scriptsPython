# Hora de jugar: Una calculadora tiene cuatro operaciones básicas (a saber: sumar, restar,
# multiplicar, dividir). Desarrolle una función para realizar cada operación, que reciba como
# parámetros dos números ingresados por el usuario y devuelva el resultado de la operación.
# Resuelva la división por restas sucesivas (investigar cómo se resuelve).
# Desarrollar un programa principal con un menú que permita realizar una operación y posea
# una opción para Salir. Luego de cada operación realizada se debe volver a presentar el menú.

import sys,os                                                       # Importo el modulo para definir path de las funciones
#sys.path.append("../../Funciones")                                 # Recomendada para cualquier ide menos vscode 
#sys.path.insert(0, "/home/goku/Documents/GitHub/uade/Funciones")   # Solo para que funcione en vscode, comentar si no se usa vscode
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Funciones')))

import FuncionSuma
import FuncionResta
import FuncionMultiplica
import FuncionDivisionRestando
import FuncionMostrarMensaje
import FuncionValidadQseaPositivo
import FuncionMostrarMensajeCalculadora
import FuncionValidarNroMayorA4

#PROGRAMA PRINCIPAL

''' Cargo funcion mensaje '''
FuncionMostrarMensaje.mostrarMensaje("TP 6 - Calculadora Python")

''' Variables globales '''
opt=1

''' Inicio del Menu '''
while opt !=0:
    
    ''' Funcion enunciado '''
    FuncionMostrarMensajeCalculadora.mostrarMensaje()
    
    ''' Valido variable de entrada '''
    opt=FuncionValidadQseaPositivo.ingresarPositivo("Ingrese un numero del 1 al 4: ")
    opt=FuncionValidarNroMayorA4.mayor_acuatro(opt)
    
    ''' Menu '''
    if opt == 1:
        FuncionSuma.operacionSumar("Operacion Suma")
    elif opt == 2:
        FuncionResta.operacionResta("Operacion Resta")
    elif opt == 3:
        FuncionMultiplica.operacionMultiplica("Operacion Multiplicacion")
    elif opt == 4:
        FuncionDivisionRestando.dividoRestando("Operacion Division entera")
