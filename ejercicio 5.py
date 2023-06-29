"""Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y muestre por pantalla el resultado, considerando lo siguiente:
a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
c. Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100."""
horas= int(input("Ingrese cuantas horas trabajó en el mes: ")) #Se pide el n° de horas trabajadas.
if horas>192:
    print ("Error. No se puede trabajar tantas horas en un mes.")
elif horas>120: #Según el n° de horas trabajadas cobrará diferente.
    multiplicacion= horas * 1500
elif horas>=80 and horas<=120:
    multiplicacion= horas * 1300
elif horas<80: 
    multiplicacion = horas*1100
print("De acuerdo a tus horas trabajadas, tu sueldo es de: ", multiplicacion)