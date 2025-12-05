alunos = [
    "Guilherme",
    "Victor",
    "Antonio",
    "Pamplona",
    "Mardonio"
]

while True:
    try:
        num = input("Digite um número: ")
        num = int(num)
        aluno_selecionado = alunos[num]
        print(aluno_selecionado)
        break
    except ValueError:
        print("O valor digitado é inválido. Digite apenas números")
    except IndexError:
        print("Aluno não encotrado.")
    except Exception:
        print("Algo aconteceu, não sabemos o que foi")
