import os
os.system("cls")

try:
    numero=int(input("Introduce un numero: "))
    numeros=[]

    while numero not in numeros:
        numeros.append(numero)
        numero=int(input("Introduce un numero: "))

    print("Numero repetido.")
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
finally:
    print("Fin del programa.")