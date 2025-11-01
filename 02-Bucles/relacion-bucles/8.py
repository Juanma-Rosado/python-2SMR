# Pide dos números y muestra todos los números comprendidos entre ellos.

numero1=int(input("Introduce un numero: "))
numero2=int(input("Introduce otro numero: "))

inicio=min(numero1, numero2)
final=max(numero1, numero2)

for num in range(inicio+1,final):
    print(num)



