# Pide números al usuario hasta que escriba 0, y muestra la media de los números introducidos.

suma=0
contador=0

try:
    while True:
        numero=int(input("Introduce un numero: "))
        if numero==0:
            break
        suma+=numero
        contador+=1

    print(f"La media de esos numeros es {int(suma/contador)}")

except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")   
    