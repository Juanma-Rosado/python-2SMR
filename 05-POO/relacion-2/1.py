class Cuenta:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
        
    def ingresar(self,cantidad):
        self.saldo+=cantidad
    
    def retirar(self,cantidad):
        if self.saldo-cantidad>=0:
            self.saldo-=cantidad
        else:
            print("Saldo insuficiente")
            
    def get_titular(self):
        print(self.titular)
    
    def set_titular(self,titular):
        self.titular=titular
    
    def get_saldo(self):
        print(self.saldo)
    
    def set_saldo(self,saldo):
        self.saldo=saldo
    
cuenta=Cuenta("Juanma",1000)

cuenta.ingresar(1000)
cuenta.get_saldo()
cuenta.retirar(3000)
cuenta.get_saldo()