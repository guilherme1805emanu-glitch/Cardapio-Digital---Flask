
class Circculo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
       from math import pi
       return pi * (self.raio ** 2)
    
    def perimetro(self):
        from math import pi
        return 2 * pi * self.raio
    
circulo1 = Circculo(5)
print(circulo1.area())
print(circulo1.perimetro())
