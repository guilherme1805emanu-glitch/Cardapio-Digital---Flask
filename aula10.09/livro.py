class Livro:
    def __init__(self,titulo,autor,ano_de_publicacao,disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
        else:
            raise ValueError("Livro indisponível para empréstimo!")
    def devolver(self):
        self.disponivel = True
    def exibir_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_de_publicacao}, Disponível: {self.disponivel}"
    
livro1 = Livro("1984", "George Orwell", 1949)
print(livro1.exibir_info())
livro1.emprestar()