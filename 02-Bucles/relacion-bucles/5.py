# Pide números al usuario hasta que introduzca un número negativo,
# y muestra cuántos números positivos introdujo.

numero=int(input("Introduce un numero: "))
contador=0

while numero>0:
    numero=int(input("Introduce un numero: "))
    contador+=1

print(f"Has introducido {contador} numeros positivos")

