"""Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas."""
persona=0 #Contador.
while persona < 5:
    nom= input("Ingrese nombre: ") #Se pide los datos de las personas.
    apellido= input("Ingrese Apellido: ")
    edad= int(input("Ingrese edad: "))
    #Se imprime por pantalla los datos de las personas.
    print(nom)
    print(apellido)
    print(edad)
    persona+=1