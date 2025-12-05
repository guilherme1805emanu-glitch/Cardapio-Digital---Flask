
class Pessoa:
    def __init__(self,nome,sobrenome):
        self._nome = nome
        self._sobrenome = sobrenome
        
    def falar (self):
        return f"Olá, meu nome é {self._nome} {self._sobrenome}"
        
pessoaTeste = Pessoa("Fulano","da Silva")
print(pessoaTeste.falar())


class Professor(Pessoa):
    def __init__(self,nome,sobrenome,curso):
        super().__init__(nome,sobrenome)
        self._curso = curso
        
    def ensinar(self):
        return f"Vamos aprender sobre {self._curso}"
    
professorTeste = Professor("Beltrano","de Souza","JavaScript")
print(professorTeste.falar())
print(professorTeste.ensinar())

#-----------------------------------------------------------------------------------------------------------------------------------------------------
