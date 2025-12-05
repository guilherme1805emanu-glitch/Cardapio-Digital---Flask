
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        return self.listar()

    def listar(self):
        titulos = []
        for livro in self.livros:
            titulos.append(livro.titulo)
        return titulos
