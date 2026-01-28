class Contacto:
    def __init__(self,nombre,telefono):
        self.nombre=nombre
        self.telefono=telefono

    def llamar(self):
        print(f"Llamando a {self.nombre} al número {self.telefono}")


contacto1=Contacto("Juanma",123456789)
contacto2=Contacto("Lucas", 987654321)
contacto3=Contacto("Anjana",444444444)


diccionario={
    contacto1.nombre:contacto1,
    contacto2.nombre:contacto2,
    contacto3.nombre:contacto3
}


nombre=input("Introduce el nombre del contacto: ")


if nombre in diccionario:
    diccionario[nombre].llamar()
else:
    print("El contacto no existe")