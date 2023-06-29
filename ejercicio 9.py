"""Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad de personas ingresada por el usuario."""
num= int(input("Ingrese la cantidad de veces que desea ingresar los datos: ")) #Variable "num" guarda el n° de veces que el usuario decida realizar la entrada de datos.
if num<1:
 print("Error. Número inválido.") 
persona=0 #Contador.
while persona < num:
    nom= input("Ingrese nombre: ")
    apellido= input("Ingrese Apellido: ")
    edad= int(input("Ingrese edad: "))
    #Se imprime por pantalla los datos de las personas.
    print(nom)
    print(apellido)
    print(edad)
    persona+=1