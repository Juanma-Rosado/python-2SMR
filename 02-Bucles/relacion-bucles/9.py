#Pide un número y calcula su factorial.

numero=int(input("Introduce un numero: "))
factorial=1

for i in range(1,numero+1):
    factorial*=i
print(f"El factorial del numero {numero} es {factorial}")



