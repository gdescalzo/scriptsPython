# Esta funcion no tiene parametro, por q se encarga de pedir dato por teclado.
# Ingresar del teclado unnumero y validar que sea positivo.

def ingresarPositivo(mensaje):
    ''' Ingresar del teclado un numero y validar que sea positivo.'''
    num = int(input(mensaje))

    ''' Ciclo de validacion positivo '''
    while num < 0:
        print("Debe ser positivo")
        num = int(input(mensaje))

    ''' Cuando termina el ciclo estoy seguro que el valor de num es positivo '''
    return num
