from viagem_class import viagem_class

viagem_0 = viagem_class("Florida")
viagem_1 = viagem_class("Havai")
viagem_2 = viagem_class("Toquio")
viagem_3 = viagem_class("Egito")

print("------------------------------------------------------------------------")
print("Bem-Vindo ! viagens senai tem ofertas pra vc")

viajante = input("Digite seu nome para comerçarmos: ")

print(f"{viajante} Temos 4 destinos para voce: "
'''
      [0] Florida
      [1] havai
      [2] toquio
      [3] egito
'''
)
    


selecao = int(input("Selecione o numero da viagem desejada: "))
lista_viagem = [viagem_0, viagem_1, viagem_2, viagem_3]
opcao_selecionada = int(selecao)
for opcao in lista_viagem:
    if opcao_selecionada >= 4:
        print("Esta opção nao esta incluida!")
        break
    if opcao_selecionada <= 3:
        print(f"{viajante} sua viagem para {lista_viagem[opcao_selecionada].destino} está marcada.")
        print("Volte sempre!")
        break
