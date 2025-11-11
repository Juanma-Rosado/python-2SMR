import os
os.system("cls")

try:
    numero=int(input("Introduce un numero: "))

    for i in range(numero+1):
        print(2**i)
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
finally:
    print("El programa ha terminado.")