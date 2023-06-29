"""Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas."""
contador_edades=0 #Contador
acumulador_edades=0 #Acumulador
condicion=1 #Condicion booleana.
while condicion==1:
    edades=int(input("Ingrese las edades, una a una: "))
    contador_edades=+1 
    acumulador_edades= acumulador_edades+edades #Acumula las edades ingresadas.
    condicion= int(input("¿Desea seguir ingresando edades? Si=1 No=0 ")) 
    promedio_edades= acumulador_edades/(contador_edades+1) #Calcula el promedio de las edades ingresadas.
    if condicion==0: #Condicion para que el usuario decida si seguir ingresando edades o no.
        print ("El promedio de las edades ingresadas es de", promedio_edades, "\n" "El total de edades que ingresó es:", contador_edades+1)
    elif condicion>1:
        print ("El valor ingresado es incorrecto.")