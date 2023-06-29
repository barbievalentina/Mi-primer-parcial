"""Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto (bruto + bonif), considerando:
a. Si trabajo más de 120hs, la bonificación es de %18
b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
c. Si trabajo menos de 80 horas, la bonificación es de %13."""
horas= int(input("Ingrese cuantas horas trabajó en el mes: ")) #Se pide el n° de horas trabajadas.
bonificaciones15= (horas*1300)*0.15
bonificaciones18= (horas*1500)*0.18
bonificaciones13= (horas*1100)*0.13
if  horas>192:
    print("Error. No se puede trabajar tantas horas en un mes.") 
elif horas<120: #Según las horas trabajadas tendrá un sueldo bruto, una bonificación y un sueldo neto diferente.
    multiplicacion= horas * 1300
    print("Su sueldo bruto es de $", multiplicacion, "\n" "Más una bonificación de $", bonificaciones15,"\n" "Su sueldo neto es de $", multiplicacion+bonificaciones15)
elif horas>=80 and horas<=120:
    multiplicacion= horas * 1500
    print("A usted le corresponde $", multiplicacion, "\n" "Más una bonificación de $", bonificaciones18,"\n" "Su sueldo neto es de $", multiplicacion+bonificaciones18)
elif horas<80:
    multiplicacion= horas * 1100
    print("A usted le corresponde $", multiplicacion, "\n" "Más una bonificación de $", bonificaciones13,"\n" "Su sueldo neto es de $", multiplicacion+bonificaciones13)