# Ejercicio 17
# Utilizando bucles, imprimir de una lista de números todos aquellos que no sean pares.
# Utiliza la variable numeros = [4,6,7,8,23,21,999,10,13,65,72].

numeros = [4,6,7,8,23,21,999,10,13,65,72]

for num in numeros:
    if num%2!=0:
        print(num)