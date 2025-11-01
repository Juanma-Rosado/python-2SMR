# Pide una palabra y muestra cuántas letras tiene y cuántas son vocales.

palabra=input("Introduce una palabra: ").lower()
letras=len(palabra)
vocales=0


for letra in palabra:
    if letra in "aeiou":
        vocales+=1

print(f"La palabra {palabra} tiene {letras} letras y {vocales} de ellas son vocales")


