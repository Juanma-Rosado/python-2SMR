import os
os.system("cls")

try:
    numero=int(input("Introduce un numero entero positivo: "))

    for n in range(0,numero+1):
        if n%2!=0:
            if n!=numero:
                print(n, end=", ")
            else:
                print(n)
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
finally:
    print("El programa ha finalizado.")