# Ejercicio 19
# Definir una función que, al recibir una cadena de texto,
# cuente cuántas palabras hay y devuelva dicho valor.
# Dada la cadena, imprimir La cantidad de palabras en el texto es:.

def palabras(texto):
    texto = texto.split()
    return len(texto)

x = "Estoy haciendo un curso de Python"
print("La cantidad de palabras en el texto es:", palabras(x))


