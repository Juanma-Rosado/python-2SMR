# Pide un número y muestra todos sus divisores positivos.

numero=int(input("Introduce un numero: "))
contador=0

while contador<numero:
    contador+=1
    if numero==contador:
        print(contador)
    elif numero%contador==0:
        print(contador, end=", ")

