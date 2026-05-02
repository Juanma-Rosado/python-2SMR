class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")
        print(f"Saldo actual: {self.saldo}")


cuenta1 = CuentaBancaria("Juanma", 100)
cuenta1.depositar(50)
cuenta1.retirar(200)
cuenta1.retirar(40)
