class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        self.nombre=nombre

    def get_edad(self):
        return self.edad

    def set_edad(self,edad):
        self.edad=edad
    
persona1=Persona("Juanma",17)
persona2=Persona("Lucas",18)

persona1.presentarse()
persona2.presentarse()

