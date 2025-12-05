#1.Crie um programa que solicite ao usuário dois números e calcule a soma deles.
#Use try e except para tratar quaisquer erros que possam ocorrer 
#(como entradas não numéricas)

# while True:
#     try:
#         num1 = input("Digite o primeiro número:")
#         conversion1 = int(num1)

#         num2 = input("Digite o segundo número:")
#         conversion2 = int(num2)

#         somaDosNumeros = conversion1 + conversion2
#         print(somaDosNumeros) 
#         break

#     except ValueError:
#         print("Você pde digitar apenas números!!")
        
# _______________________________________________________________________________

#2.Crie um programa que solicite ao usuário um índice e tente acessar um elemento em uma lista. Use try e except para tratar quaisquer erros que possam ocorrer (como o índice estar fora do intervalo ou não ser um número).

# carros=[
#     "BMW",
#     "FERRARI",
#     "LAMBORGUINI",
# ]

# while True:
#     try:
#         num = input("Digite um número: ")
#         num = int(num)
#         carro_selecionado = carros[num]
#         print(carro_selecionado)
#         break
#     except ValueError:
#         print("O valor digitado é inválido. Digite apenas números")
#     except IndexError:
#         print("Carro não encotrado.")

