class Coche:
    def __init__(self, marca, modelo, encendido=False):
        self.marca = marca
        self.modelo = modelo
        self.encendido = encendido

    def arrancar(self):
        self.encendido = True
        print(f"El coche {self.marca} ha arrancado")


coche1 = Coche("Ferrari", "Testarossa")
coche1.arrancar()
