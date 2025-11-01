# Pide una palabra y un número, y muestra esa palabra repetida tantas veces como el número indique.

palabra=input("Introduce una palabra: ")
numero=int(input("Introduce un numero: "))

for _ in range(numero):
    print(palabra)