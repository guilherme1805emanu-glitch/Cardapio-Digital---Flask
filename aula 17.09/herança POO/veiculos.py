
class Veiculo:
    def __init__(self,marca,modelo,fabricacao,preco):
        self._marca=marca
        self._modelo=modelo
        self._fabricacao=fabricacao
        self._preco=preco
        
    def exibirInfo(self):
        return f"""A marca do veículo é:{self._marca}
        seu modelo é:{self._modelo}
        o ano de sua fabricação é:{self._fabricacao}
        e o preço desse veículo é:{self._preco} reais."""
        
        
class Carro (Veiculo):
    def __init__(self, marca, modelo, fabricacao, preco,tipo_de_gasolina,quantidade_de_portas):
        super().__init__(marca, modelo, fabricacao, preco)
        self._tipo_de_gasolina=tipo_de_gasolina
        self._quantidade_de_portas=quantidade_de_portas
        
    def exibirInfo(self):
        return f"""A marca do veículo é:{self._marca}
        seu modelo é:{self._modelo}
        o ano de sua fabricação é:{self._fabricacao}
        o preço desse veículo é:{self._preco} reais.
        O tipo de gasolina que ele usa é:{self._tipo_de_gasolina}
        e a quantidade de portas que ele possui é:{self._quantidade_de_portas}."""
        
class Moto (Veiculo):
    def __init__(self, marca, modelo, fabricacao, preco,cilindradas,tipo_de_partida):
        super().__init__(marca, modelo, fabricacao, preco)
        self._cilindradas=cilindradas
        self._tipo_de_partida=tipo_de_partida
    
    def exibirInfo(self):
        return f"""A marca do veículo é:{self._marca}
        seu modelo é:{self._modelo}
        o ano de sua fabricação é:{self._fabricacao}
        o preço desse veículo é:{self._preco} reais.
        A quantidade de cilindradas que ela possui é:{self._cilindradas}
        e o tipo de partida que ela possui é:{self._tipo_de_partida}."""
        
class concessionaria:
    def __init__(self,nome,veiculos=[]):
        self._nome=nome
        self._veiculos=veiculos
        
    def adicionarVeiculo(self,veiculo):
        self._veiculos.append(veiculo)
        
    def listarVeiculos(self):
        for veiculo in self._veiculos:
            print(veiculo.exibirInfo())
            print("-------------------")
            
