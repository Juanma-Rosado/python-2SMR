# Pide una palabra y muestra cuántas veces aparece cada letra.

palabra=input("Introduce una palabra: ").lower()
frecuencia={}

for letra in palabra:
    if letra in frecuencia:
        frecuencia[letra]+=1
    else:
        frecuencia[letra]=1

for letra, cantidad in frecuencia.items():
    print(f"La letra {letra} aparece {cantidad} veces")


