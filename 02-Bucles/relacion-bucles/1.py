#Pide un número al usuario y muestra todos los números desde 0 hasta ese número, de dos en dos.

numero=int(input("Introduce un numero: "))

for num in range(0,numero+1,2):
    print(num)
    
    
