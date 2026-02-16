class Contacto:
    def __init__(self,nombre,telefono):
        self.nombre=nombre
        self.telefono=telefono
        
    def llamar(self):
        print(f"Llamando a {self.nombre} al número {self.telefono}")

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,nombre):
        self.nombre=nombre
        
    def get_telefono(self):
        return self.telefono
    
    def set_telefono(self,telefono):
        self.telefono=telefono
    
    
contacto1=Contacto("Juanma",123456789)
contacto2=Contacto("Lucas",987654321)
contacto3=Contacto("Erika",1357981484)
contacto4=Contacto("Anjana",34877559)


diccionario={
    contacto1.nombre:contacto1,
    contacto2.nombre:contacto2,
    contacto3.nombre:contacto3,
    contacto4.nombre:contacto4
}


nombre=input("Introduce un nombre: ")

if nombre in diccionario:
    diccionario[nombre].llamar()
else:
    print("Contacto no encontrado")
