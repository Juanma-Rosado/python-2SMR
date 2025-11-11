import os
os.system("cls")

try:
    contraseña_real="python123"
    contraseña_introducida=input("Introduce la contraseña: ")
    intento=1


    while contraseña_real!=contraseña_introducida:
        if intento==3:
            print("Acceso denegado")
            break
        else:
            print("Contraseña incorrecta")
            intento+=1
            contraseña_introducida=input("Introduce la contraseña: ")
    else:
        print("Acceso permitido")
except Exception as ex:
    print(f"Ha ocurrido un error, {ex}")
finally:
    print("El programa ha finalizado.")