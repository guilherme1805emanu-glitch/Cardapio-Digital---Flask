1.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def sacar(self,valor=0):
        self.saldo -= valor
        if self.saldo < 0:
            raise ValueError("Saldo insuficiente para saque!")


    def depositar(self, valor):
        self.saldo += valor


    def exibir_saldo(self):
        return self.saldo

conta1 = ContaBancaria("João", 1000)
conta1.sacar(1200)
print(conta1.exibir_saldo())
conta1.depositar(500)
print(conta1.exibir_saldo())