import random
def sumar_dados(a, b):
    return a + b
def tirar_dados():
    a=random.randint(1,6)
    b=random.randint(1,6)
    resultado = sumar_dados(a, b)
    return a ,b, resultado

total=0
quiere = input ("¿Quieres jugar?")

while quiere[0:2] == "si" or quiere[0:2]=="Si" or quiere[0:2]=="SI":
    a, b, c=tirar_dados()
    print ("Primer dado: ", a,"\n","Segundo Dado: ", b,"\n","La suma total es: ", c)
    quiere = input ("¿Desea volver a jugar?")
    total += c

print("Gracias por jugar su total de puntos es: ",total)
