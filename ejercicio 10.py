"""Escribe un programa que calcule el promedio general de una clase."""
num_alum=int(input("Ingrese cantidad de alumnos en la clase: ")) #Se guarda el n° de alumnos de la clase.
nota= 0 #Contador
acum=0 #Acumulador
while nota < num_alum:
    alumno=int(input("Ingrese las notas de los alumnos, una a una: "))
    nota+=1
    acum=acum + alumno #Se van guardando las notas de los alumnos.
    prom=acum/num_alum #Se saca el promedio de la clase en base a las notas guardadas en la variable "acum"
print("El promedio general de los alumnos es de: ", prom)
