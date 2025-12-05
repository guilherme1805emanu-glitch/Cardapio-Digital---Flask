class Produto:
    def __init__(self, nome, preco,codigo,validade,marca,laticinio,tipo,tipos_disponiveis = ['alimento','bebida']):
        self.nome = nome
        self.preco = preco
        self.codigo = codigo
        self.validade = validade
        self.marca = marca
        self.laticinio = laticinio
        self.tipo = tipo
        self.tipos_disponiveis = tipos_disponiveis
        
        if tipo not in tipos_disponiveis:
            raise ValueError(f"Tipo inválido: {tipo} os tipos disponíveis são: {', '.join(tipos_disponiveis)}")
        

class Alimento(Produto):       
    lista=["Fresco","Congelado","Hortifruti","Enlatado,Salgado","Doce","Integral","Orgânico","Estantânio"]

    def __init__(self, nome, preco,codigo,validade,marca,laticinio,tipo,peso):
        super().__init__(nome, preco,codigo,validade,marca,laticinio,tipo,self.lista)
        self.peso = peso
        
class Bebida(Produto):        
    lista=["Água","Refrigerante","Suco","Alcool","Chá","Café","Energético","Isotônico"]
    def __init__(self, nome, preco,codigo,validade,marca,laticinio,tipo,volume):
        super().__init__(nome, preco,codigo,validade,marca,laticinio,tipo,self.lista)
        self.volume = volume


class Estoque:
    def __init__(self):
        self.__lista = []
    def adicionar_produto(self,produto,quantity=0):
        for estoque in self.__lista:
            if estoque["produto"]._codigo ==produto.codigo:
                estoque["quantidade"] += quantity
                return
        self.__lista.append({
            "produto":produto,
            "quantidade":quantity
        })
        
        
    def remover_produto(self,produto,quantity=0):
        for estoque in self.__lista:
            if estoque["produto"].codigo == produto.codigo:
                if estoque["quantidade"] < quantity:
                    raise ValueError("Quantidade insuficiente em estoque para remoção!")
                estoque["quantidade"] -= quantity
                return
        raise ValueError("Produto não encontrado no estoque!")
    
    def listar_produtos(self):
        return self.__lista
    
    
    
alimento1 = Alimento("maçã",5.00,1234,"12/12/2024","danoni",False,"Fresco",5)
estoque1 = Estoque()
# estoque1.adicionar_produto(alimento1,10)
# print(estoque1.listar_produtos())
# estoque1.remover_produto(alimento1,5)
# print(estoque1.listar_produtos())