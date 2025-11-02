# Dibuja un cuadrado de asteriscos del tamaño que indique el usuario.

tamaño=int(input("Introduce el tamaño del cuadrado: "))
contador=0

while tamaño>contador:
    print(tamaño*"*")
    contador+=1