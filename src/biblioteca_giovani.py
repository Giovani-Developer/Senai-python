from biblioteca import biblioteca

e0 = biblioteca("Seja um programador inteligente!")
e1 = biblioteca("POO")
e2 = biblioteca("Manual da programação")

print("------------------------------------------------------------")
print("Bem-Vindo à Biblioteca de Freitas, Giovani")

solicitante = input("Digite seu nome: ")

print(f"{solicitante} temos esses livros disponiveis para o emprestimo"
'''
    [0] Seja um programador inteligente!
    [1] POO
    [2] Manuel da programação
'''
)

selecao = int(input("Selecione o livro desejado: "))
lista_livros = [e0, e1, e2]
opcao_selecionada = int(selecao)
for opcao in lista_livros:
    if opcao_selecionada >= 4:
        print("Este livro nao esta disponivel")
    if opcao_selecionada <= 3:
        print(f"{solicitante} Seu livro {lista_livros[opcao_selecionada].estante} é seu durante o emprestimo!!")
        print("Te espero no dia da devolução!")
        break

