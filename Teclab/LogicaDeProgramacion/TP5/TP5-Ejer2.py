# Escribir un algoritmo que permita ingresar los números de legajo de los alumnos de un curso
# y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo.

# Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota
# mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga
# de datos, informar:
# •  Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
# •  Cantidad de alumnos que desaprobaron el examen. Nota menor a 4.
# •  Porcentaje de alumnos que están aplazados (tienen 1 en el examen).

# Mensaje a usuario
print("A continuacion se leeran los numeros de legajo (que se ingresan por teclado) de los alumnos de un curso")
print("Para finalizar ingrese -1")
print(" ")

legajo=0                                                                                              # Entrada
nota=0                                                                                                # Entrada
aplazo=0
promAplazo=0

# Vars
contAprueba=0
contDesaprueba=0
contAplazo=0

while legajo>=0 and nota>=0 and nota<=10:

    legajo=int(input("Ingresar número de legajo: "))                                                   # Entrada
    nota=int(input("Ingresar nota de examen final: "))                                                 # Entrada
    
    # Verifico: que la nota no sea sea -1 y el legajo no sea -1                                            ## Proceso
    if legajo>=0 and legajo!=-1 and nota!=-1:
        
        if nota > 4 and nota <= 10:
            print(legajo,"aprobo con",nota,"ya que es mayor a 4")
            print(" ")
            
            contAprueba=contAprueba+1
        
        elif nota > 1 and nota < 4:
            print(legajo,"desaprobo con",nota,"ya que es menor a 4")
            print(" ")
            
            contDesaprueba=contDesaprueba+1
        
        elif nota == 1:
            print(legajo,"desaprobo con",nota," y tiene aplazo")
            print(" ")
            
            contAplazo=contAplazo+1
            aplazo=nota+aplazo
        
    while nota<0 and legajo<0 and nota!=-1 and legajo!=-1:
        print("usted ingreso un numero negativo, por favor ingrese numeros positivos")
        print(" ")

if contAplazo !=0:
    promAplazo = aplazo/contAplazo

# Se finaliza el programa
if legajo==-1 or nota==-1:
    print("Ingreso un -1 (fin de la carga)")
    print(" ")
    print("La cantidad de alumnos que aprobaron con nota mayor o igual a 4: ",contAprueba)               ## Salida
    print("La cantidad de alumnos que desaprobaron el examen. Nota menor a 4: ",contDesaprueba)          ## Salida
    print("La cantidad de alumnos que están aplazados (tienen 1 en el examen): ",promAplazo)             ## Salida