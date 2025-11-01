# Pide una serie de números hasta que el usuario escriba un número negativo,
# y muestra el mayor número introducido.

"""
numeros=[]

while True:
    numero=int(input("Introduce un numero: "))
    if numero<0:
        break
    numeros.append(numero)

print(f"El numero mayor es {max(numeros)}")
"""

try:
    numero=int(input("Introduce un numero: "))
    numeros=[]

    while numero>=0:
        numeros.append(numero)
        numero=int(input("Introduce un numero: "))

    print(f"El numero mayor es {max(numeros)}")
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")