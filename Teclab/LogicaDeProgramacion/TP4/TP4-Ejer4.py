# Leer 10 números enteros e imprimir el promedio, el mayor y en qué orden fue ingresado el
# mayor valor, si se ingresó más de una vez debe informar el primer ingreso.

# Leer 10 números enteros 
num1=int(input("ingrese N°1: "))
num2=int(input("ingrese N°2: "))
num3=int(input("ingrese N°3: "))
num4=int(input("ingrese N°4: "))
num5=int(input("ingrese N°5: "))
num6=int(input("ingrese N°6: "))
num7=int(input("ingrese N°7: "))
num8=int(input("ingrese N°8: "))
num9=int(input("ingrese N°9: "))
num10=int(input("ingrese N°10: "))

# el promedio
suma=num1+num2+num3+num4+num5+num6+num7+num8+num9+num10
prom=suma/2

# el mayor

if num1>num2 and num1>num3 and num1>num4 and num1>num5 and num1>num6 and num1>num7 and num1>num8 and num1>num9 and num1>num10:
    mayor=num1
    orden = 1
    print("promedio es igual a: ", prom)
    print("el mayor numero ingresado es: ", "\"",mayor,"\"", "y se ingreso en el orden: ""\"",orden,"\"")
    
elif num2>num1 and num2>num3 and num2>num4 and num2>num5 and num2>num6 and num2>num7 and num2>num8 and num2>num9 and num2>num10:
    mayor=num2
    orden = 2
    print("promedio es igual a: ", prom)
    print("el mayor numero ingresado es: ", "\"",mayor,"\"", "y se ingreso en el orden: ""\"",orden,"\"")

elif num3>num1 and num3>num2 and num3>num4 and num3>num5 and num3>num6 and num3>num7 and num3>num8 and num3>num9 and num3>num10:
    mayor=num3
    orden = 3
    print("promedio es igual a: ", prom)
    print("el mayor numero ingresado es: ", "\"",mayor,"\"", "y se ingreso en el orden: ""\"",orden,"\"")

elif num4>num1 and num4>num2 and num4>num3 and num4>num5 and num4>num6 and num4>num7 and num4>num8 and num4>num9 and num4>num10:
    mayor=num4
    orden = 4
    print("promedio es igual a: ", prom)
    print("el mayor numero ingresado es: ", "\"",mayor,"\"", "y se ingreso en el orden: ""\"",orden,"\"")

elif num5>num1 and num5>num2 and num5>num3 and num5>num4 and num5>num6 and num5>num7 and num5>num8 and num5>num9 and num5>num10:
    mayor=num5
    orden = 5
    print("promedio es igual a: ", prom)
    print("el mayor numero ingresado es: ", "\"",mayor,"\"", "y se ingreso en el orden: ""\"",orden,"\"")

elif num6>num1 and num6>num2 and num6>num3 and num6>num4 and num6>num5 and num6>num7 and num6>num8 and num6>num9 and num6>num10:
    mayor=num6
    orden = 6
    print("promedio es igual a: ", prom)
    print("el mayor numero ingresado es: ", "\"",mayor,"\"", "y se ingreso en el orden: ""\"",orden,"\"")

elif num7>num1 and num7>num2 and num7>num3 and num7>num4 and num7>num5 and num7>num6 and num7>num8 and num7>num9 and num7>num10:
    mayor=num7
    orden = 7
    print("promedio es igual a: ", prom)
    print("el mayor numero ingresado es: ", "\"",mayor,"\"", "y se ingreso en el orden: ""\"",orden,"\"")

elif num8>num1 and num8>num2 and num8>num3 and num8>num4 and num8>num5 and num8>num6 and num8>num7 and num8>num9 and num8>num10:
    mayor=num8
    orden = 8
    print("promedio es igual a: ", prom)
    print("el mayor numero ingresado es: ", "\"",mayor,"\"", "y se ingreso en el orden: ""\"",orden,"\"")    

elif num9>num1 and num9>num2 and num9>num3 and num9>num4 and num9>num5 and num9>num6 and num9>num7 and num9>num8 and num9>num10:
    mayor=num9
    orden = 9
    print("promedio es igual a: ", prom)
    print("el mayor numero ingresado es: ", "\"",mayor,"\"", "y se ingreso en el orden: ""\"",orden,"\"")
    
elif num10>num1 and num10>num2 and num10>num3 and num10>num4 and num10>num5 and num10>num6 and num10>num7 and num10>num8 and num10>num9:
    mayor=num10
    orden = 10
    print("promedio es igual a: ", prom)
    print("el mayor numero ingresado es: ", "\"",mayor,"\"", "y se ingreso en el orden: ""\"",orden,"\"")
