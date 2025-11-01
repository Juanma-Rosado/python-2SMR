# Pide números hasta que se escriba un 0; al final, muestra cuántos eran pares y cuántos impares.

numero=int(input("Introduce un numero: "))
par=0
impar=0

while numero!=0:
    if numero%2==0:
        par+=1
    else:
        impar+=1
    numero=int(input("Introduce un numero: "))

print(f"{par} numeros eran pares y {impar} numeros eran impares")

