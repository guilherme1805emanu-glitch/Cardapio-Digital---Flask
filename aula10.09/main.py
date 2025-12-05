from bibliotecas import Biblioteca
from livro import Livro

biblioteca = Biblioteca()
livro1 = Livro("vingadores", "George Orwell", 1949, True)

print(biblioteca.adicionar_livro(livro1))