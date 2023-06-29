"""Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el
año de nacimiento"""
ano= int(input("Ingrese el año en que nació: ")) #Se pide el año en que nació para restarle al año actual.
ano1= int(input("Ingrese el año actual: ")) #Se pide el año actual para restarle el año en que nació.
edad= ano1-ano #Se le resta el año de nacimiento al año actual para saber la edad que va a cumplir.
print("Usted tiene o va a cumplir", edad, "años.") #Se imprime por pantalla la edad que cumplió ó cumplirá el usuario.
