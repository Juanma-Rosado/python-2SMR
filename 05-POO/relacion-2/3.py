class Empleado():
    def __init__(self,nombre,puesto,sueldo_mensual):
        self.nombre=nombre
        self.puesto=puesto
        self.sueldo_mensual=sueldo_mensual
    
    def sueldo_anual(self):
        sueldo_año=self.sueldo_mensual*12
        bono=sueldo_año*0.05
        return sueldo_año+bono
    
empleado1=Empleado("Juanma","Programador",2000)

print(f"Tu sueldo total anual es {empleado1.sueldo_anual()}€")
