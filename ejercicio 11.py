"""Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
a. Si es número es par o impar.
b. Cuanto es la suma total de todos los números mostrados.
c. Cuanto es la suma total de todos los números pares mostrados.
d. Cuanto es la suma total de todos los números impares mostrados."""
num=1 #Contador
suma_numeros=0  #Acumulador de la suma de todos los números.
suma_pares=0 #Acumulador de la suma de los numeros pares.
suma_impares=0 #Acumulador de la suma de los numeros impares.
while num<=10:
    suma_numeros+=num
    if num%2==0: #Se calcula si el número es par si su resto es 0.
       print(num, "es par.")
       suma_pares+=num #Se suman los pares.
    else:
       print(num, "es impar.")
       suma_impares+=num #Se suman los impares.
    num+=1
print("La suma de los números es:", suma_numeros)
print("La suma de todos los números pares es:", suma_pares)
print("La suma de todos los numeros impares es:", suma_impares)
