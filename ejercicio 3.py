"""Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar)."""
dolar=float(input("Ingrese cuantos dólares quiere convertir: ")) #Se pide ingresar los dólares que quiere convertir.
tipodolar=float(input("Ingrese el precio del tipo de cambio del dólar: ")) #Se ingresa el precio del tipo de dolar al que se quiere convertir.
pesosarg= dolar*tipodolar
print("Usted tiene ", pesosarg, " pesos argentinos.")