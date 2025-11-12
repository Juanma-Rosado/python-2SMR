import os
os.system("cls")

numero_valido = False  # bandera para controlar si el dato es correcto

while not numero_valido:
    try:
        numero = int(input("Introduce un número positivo: "))
        if numero < 0:
            print("Debe ser un número positivo.")
        else:
            numero_valido = True  # solo salimos si el número es válido
    except ValueError:
        print("Error: debes introducir un número entero válido.")

try:
    for fila in range(0, numero + 1):
        for columna in range(numero - fila):
            print("*", end="")
        print()
except Exception as ex:
    print(f"Ha ocurrido un error inesperado: {ex}")
finally:
    print("El programa ha finalizado.")
