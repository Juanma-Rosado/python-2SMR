import os
os.system("cls")

try:
    numero=int(input("Introduce un numero: "))
    suma=0

    for n in range(0,numero):
        if n%2==0:
            suma+=n
    print(f"La suma de los pares hasta {numero} es {suma}.")
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
finally:
    print("El programa ha finalizado.")
