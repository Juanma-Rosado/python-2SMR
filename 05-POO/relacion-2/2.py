class Rectangulo():
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        return self.base*self.altura
    
    def perimetro(self):
        return 2*(self.base+self.altura)
    
rectangulo1=Rectangulo(6,4)

print(f"El área es {rectangulo1.area()} y el perímetro es {rectangulo1.perimetro()}")
