# exercicio 1                                          Tema: Dicionários

# pessoa = {
#     "nome": "Giovani",
#     "idade": 17,
#     "cidade": "Mogi Guaçu"
# }

# pessoa["idade"] = 18

# print(pessoa)


######################################################

# Exercício 2 - Somar os valores do dicionario 

# precos = {
#     "banana": 3.50,
#     "maça": 2.80,
#     "uva": 4.00
# }

# soma = sum(precos.values()) # o metodo sum() faz a soma, o metodo .values() pega o valor do dicionario

# print(f"A soma dos valores é de: {soma: .2f}") # o .2f usa 2 casas dps da virgula

############################################################################################################################

# Exercício 3 - 

# frase = " O rato roeu a roupa do rei de Roma e a Rainha de raiva roeu o resto"
# print(frase)
# minuscula = frase.lower()
# palavras = minuscula.split() # o .split() ele separa a string em varias partes por palavra

# print(palavras)
# contador = {} # criei um contador vazio

# for palavra in palavras:         # para cada palavra dentro da lista de palavras, ele faz algo
#     if palavra in contador:      # se palavra tiver dentro do contador ;
#         contador[palavra] += 1   #  aumenta + 1
#     else:                        # se a palavra não esta no contador ;
#         contador[palavra] = 1    # Cria a chave com o valor 1

# print(contador)

########################################################################################################################
# Exercício 4

agenda = {
    "Giovani":["19-999295741" , "19-999295742"],
    "Simone": ["19-997873739" , "19-997873749"]
}

print(f"Os números dos contatos são: {agenda}")

for nome, telefone in agenda.items():
    print(f"\n Contato: {nome}")
    for telefone in telefone:
        print(f" - Telefone: {telefone}")

#########################################################################################################################