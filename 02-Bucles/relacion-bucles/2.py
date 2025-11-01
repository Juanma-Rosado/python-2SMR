#Pide un número y muestra la suma de todos los números impares desde 1 hasta ese número.

numero=int(input("Introduce un numero: "))
suma=0

for num in range(1,numero+1,2):
    suma+=num
print(f"La suma de todos los numeros impares desde {1} hasta {numero} es {suma}")
    
    
    