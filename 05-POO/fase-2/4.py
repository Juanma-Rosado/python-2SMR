class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def mostrar_pago(self):
        print(f"{self.nombre} cobra {self.sueldo_base}")


class Vendedor(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self.comision = comision

    def mostrar_pago(self):
        pago_total = self.sueldo_base + self.comision
        print(f"{self.nombre} (Vendedor) cobra {pago_total} (incluye comisión)")


emp = Empleado("Ana", 1000)
vend = Vendedor("Luis", 1000, 500)

emp.mostrar_pago()
vend.mostrar_pago()
