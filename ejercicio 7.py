"""Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades de horas, escribe un programa que calcule el descuento anual a realizarse, considerando:
a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1.
d. El programa debe mostrar elsalario anual bruto, el monto anual de bonificaciones, el monto anual
a descontarse y las horas trabajadas en todo el año."""
horas= int(input("Ingrese cuantas horas trabajó en el mes: ")) #Se pide el n° de horas trabajadas.
if  horas>192:
    print("Error. No se puede trabajar tantas horas en un mes.") 
elif horas>=80 and horas<=120:
    multiplicacion= (horas * 1500)*12 #Se calculan las horas trabajadas por año.
    horas=horas*12
    if multiplicacion>2000000:
       bonificaciones=((horas*1500)*0.18)*12 #La variable "bonificaciones" calcula las bonificaciones que se darán dependiendo del n° de horas trabajadas.
       desc= 0.05*multiplicacion #La variable "desc" calcula el descuento anual.
       print("Su salario anual bruto es de $", multiplicacion, "\n" "Más una bonificación anual de $", bonificaciones,"\n" "Su sueldo neto anual es de $", multiplicacion+bonificaciones, "\n" "Su monto anual a descontarse es de $", desc, "\n" "Sus horas trabajadas al año son:", horas )
    elif multiplicacion>=100000 and multiplicacion<2000000:
       bonificaciones=((horas*1500)*0.18)*12
       desc= 0.03*multiplicacion
       print("Su salario anual bruto es de $", multiplicacion, "\n" "Más una bonificación anual de $", bonificaciones,"\n" "Su sueldo neto anual es de $", multiplicacion+bonificaciones, "\n" "Su monto anual a descontarse es de $", desc, "\n" "Sus horas trabajadas al año son:", horas )
    elif multiplicacion<1000000:
        bonificaciones=((horas*1500)*0.18)*12
        desc= 0.01*multiplicacion
        print("Su salario anual bruto es de $", multiplicacion, "\n" "Más una bonificación anual de $", bonificaciones,"\n" "Su sueldo neto anual es de $", multiplicacion+bonificaciones, "\n" "Su monto anual a descontarse es de $", desc, "\n" "Sus horas trabajadas al año son:", horas )
elif horas>120: #Según las horas trabajadas tendrá un sueldo bruto, una bonificación, un sueldo neto diferente y trabajará al año un número de horas diferente.
    multiplicacion= (horas * 1300)*12 #Se calculan las horas trabajadas por año.
    horas=horas*12
    if multiplicacion>2000000:
       bonificaciones= ((horas*1300)*0.15)*12
       desc= 0.05*multiplicacion 
       print("Su salario anual bruto es de $", multiplicacion, "\n" "Más una bonificación anual de $", bonificaciones,"\n" "Su sueldo neto anual es de $", multiplicacion+bonificaciones, "\n" "Su monto anual a descontarse es de $", desc, "\n" "Sus horas trabajadas al año son:", horas)
    elif multiplicacion>=100000 and multiplicacion<2000000:
       bonificaciones= ((horas*1300)*0.15)*12
       desc= 0.03*multiplicacion
       print("Su salario anual bruto es de $", multiplicacion, "\n" "Más una bonificación anual de $", bonificaciones,"\n" "Su sueldo neto anual es de $", multiplicacion+bonificaciones, "\n" "Su monto anual a descontarse es de $", desc, "\n" "Sus horas trabajadas al año son:", horas)
    elif multiplicacion<1000000:
        bonificaciones= ((horas*1300)*0.15)*12
        desc= 0.01*multiplicacion
        print("Su salario anual bruto es de $", multiplicacion, "\n" "Más una bonificación anual de $", bonificaciones,"\n" "Su sueldo neto anual es de $", multiplicacion+bonificaciones, "\n" "Su monto anual a descontarse es de $", desc, "\n" "Sus horas trabajadas al año son:", horas)
elif horas<80:
    multiplicacion= (horas * 1100) #Se calculan las horas trabajadas por año.
    horas=horas*12
    if multiplicacion>2000000:
       bonificaciones=((horas*1500)*0.13)*12
       desc= 0.05*multiplicacion
       print("Su salario anual bruto es de $", multiplicacion, "\n" "Más una bonificación anual de $", bonificaciones,"\n" "Su sueldo neto anual es de $", multiplicacion+bonificaciones, "\n" "Su monto anual a descontarse es de $", desc, "\n" "Sus horas trabajadas al año son:", horas )
    elif multiplicacion>=100000 and multiplicacion<2000000:
       bonificaciones=((horas*1500)*0.13)*12
       desc= 0.03*multiplicacion
       print("Su salario anual bruto es de $", multiplicacion, "\n" "Más una bonificación anual de $", bonificaciones,"\n" "Su sueldo neto anual es de $", multiplicacion+bonificaciones, "\n" "Su monto anual a descontarse es de $", desc, "\n" "Sus horas trabajadas al año son:", horas )
    elif multiplicacion<1000000:
        bonificaciones=((horas*1500)*0.13)*12
        desc= 0.01*multiplicacion
        print("Su salario anual bruto es de $", multiplicacion, "\n" "Más una bonificación anual de $", bonificaciones,"\n" "Su sueldo neto anual es de $", multiplicacion+bonificaciones, "\n" "Su monto anual a descontarse es de $", desc, "\n" "Sus horas trabajadas al año son:", horas )
