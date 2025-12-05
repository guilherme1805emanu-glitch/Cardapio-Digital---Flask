class Calculadora:

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida!")
        return a / b
    
calc1 = Calculadora()
print(calc1.somar(10, 5))
print(calc1.subtrair(10, 5))
print(calc1.multiplicar(10, 5))
print(calc1.dividir(10, 2))