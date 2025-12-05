# 4. Crie um programa que define uma classe simples e instancia um objeto dessa classe. Solicite ao usuário um nome de atributo e tente acessar esse atributo no objeto. Use try e except para tratar o caso de o atributo não existir.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_infor(self):
        return f"Nome da pessoa: {self.nome}, Idade da pessoa: {self.idade}"

nome1=input("Digite o nome da pessoa: ")
idade1= int (input("Digite a idade da pessoa: "))

pessoa=Pessoa(nome1, idade1)
# print(pessoa.exibir_infor())
    
atributo = input("Digite o nome do atributo que voê deseja usar: ")

while True:
    try:
        valor_atributo = getattr(pessoa, atributo)
        print(f"O valor do atributo '{atributo}' é: {valor_atributo}")
        break

    except AttributeError:
        print(f"O atributo '{atributo}' não existe na classe Pessoa.")

        
