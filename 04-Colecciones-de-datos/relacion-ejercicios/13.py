# Ejercicio 13
# Utilizando bucles while, imprimir el siguiente dibujo:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


cnt = 1
while cnt <= 5:
    print("*" * cnt)
    cnt += 1

cnt = 4
while cnt >= 1:
    print("*" * cnt)
    cnt -= 1


