class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
    
persona1=Persona("Juanma",17)
persona2=Persona("Lucas",18)
persona3=Persona("Anjana",17)

personas=[persona1,persona2,persona3]

for persona in personas:
    persona.presentarse()