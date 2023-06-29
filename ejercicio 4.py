"""Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales, indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6).""" 
nota1=float(input("Ingrese la nota del 1° parcial")) #Se piden las notas de los 3 parciales.
nota2=float(input("Ingrese la nota del 2° parcial"))
nota3=float(input("Ingrese la nota del 3° parcial"))
prom= (nota1+nota2+nota3)/3 #Se calcula el promedio de la materia.
if prom>6:
    print ("Su promedio es de ", prom, ". Usted aprobó la materia.")
else:
    print("Su promedio es de ", prom, ". Usted desaprobó la materia, debe recursarla.")