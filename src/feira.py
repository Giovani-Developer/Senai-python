from feira_livre import feira_livre

f1 = feira_livre("Maça")
f2 = feira_livre("Pera")
f3 = feira_livre("Banana")
f4 = feira_livre("Kiwi")

print("-----------------------------------------------------------------------")
print("Bem vindo a feira de seu Tião")

comprador = input("Digite seu nome: ")

print(f"{comprador} temos essas frutas:"
'''
    [0]Maça
    [1]Pera
    [2]Banana
    [3]Kiwi
'''
)

selecao = int(input("Digite qual fruta voce quer: "))
lista_frutas = [f1, f2, f3, f4]
opcao_seleciona = int(selecao)

for opcao in lista_frutas:
    if opcao_seleciona >= 5:
        print("essa fruta nao esta disponivel")
    if opcao_seleciona <=4:
        print(f"{comprador} a fruta {lista_frutas[opcao_seleciona].estante} é sua!")
        print("Volte sempre!")
        break