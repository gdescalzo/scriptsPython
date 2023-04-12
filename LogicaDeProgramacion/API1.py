import random

"""
Nos acaban de contratar de una empresa para desarrollar un juego de adivinanzas de números. El juego debe tener las siguientes particularidades:

- Al inicio del juego, se debe solicitar al usuario que ingrese el rango de números para el juego y la cantidad de intentos máximos.
- El programa debe generar un número aleatorio dentro del rango ingresado por el usuario.
- El programa debe permitir al usuario la posibilidad de adivinar el número generado en la cantidad de intentos especificada.
- El programa debe indicar si el número ingresado por el usuario es mayor o menor que el número generado.
- El programa debe indicar al usuario cuántos intentos lleva y cuántos intentos le quedan.
- El programa debe permitir al usuario ingresar varios números para intentar adivinar el número generado, y guardarlos en un array.
- El programa debe verificar si el número ingresado ya fue ingresado anteriormente.
- El programa debe ordenar los números ingresados por el usuario de manera ascendente.
- El programa debe indicar al usuario los números que ya fueron ingresados ordenados.
- El juego debe terminar cuando el usuario adivina el número o se quedan sin intentos.

Consigna: 

- Instalar el software Dev C++. Es posible acceder al link de descarga haciendo clic acá.
- El programa debe solicitar al usuario que ingrese un límite inferior y superior de números para el juego.
- El programa debe solicitar al usuario que ingrese la cantidad de intentos máximos.
- El programa debe generar un número aleatorio dentro del rango ingresado por el usuario.
- El programa debe solicitar al usuario que ingrese un número para intentar adivinar el número generado.

"""

print("Juego de adivinanzas de números.")
print("Ingrese el rango de números para el juego y la cantidad de intentos máximos.")
print()
print()

Limite_Inferior = int(input(" Ingrese un límite inferior de números: "))
Limite_Superior = int(input(" Ingrese un límite superior de números: "))
Cantidad_Intentos_Max = int(input(" Ingrese la cantidad de intentos maximos: "))
Intento = int(0)

Numero_Aleatorio = random.randint(Limite_Inferior, Limite_Superior)

if Intento != Cantidad_Intentos_Max or Adivinar_Numero == Numero_Aleatorio:

    Adivinar_Numero = int(input(" Ingrese un numero para intentar adivinar el numero aleatoreo: "))
      
    if Adivinar_Numero != Numero_Aleatorio:     
        Adivinar_Numero = int(input(" Ingrese un numero para intentar adivinar el numero aleatoreo: "))
    else:        
        print("Usted adivino el numero aleatoreo", Numero_Aleatorio)
    
    Intento = Intento + 1

else:

    print("Finalizo el programa")