# Pide números al usuario hasta que escriba uno mayor que 100,
# y muestra la suma total de los números introducidos.

numero=int(input("Introduce un numero: "))
suma=0

while numero<100:
    suma+=numero
    numero=int(input("Introduce un numero: "))

print(f"La suma de los numeros introducidos es {suma}")