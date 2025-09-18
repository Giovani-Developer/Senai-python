# numeros = [1, 2, 2, 3, 4, 4, 5, 1]

# unicos = []

# for i in numeros:
#     if i not in unicos:
#         unicos.append(i)

# print(unicos)


###################################################

# 2 Forma

# numeros = [1, 2, 2, 3, 4, 4, 5, 1]
# unicos = list(set(numeros))
# print(unicos)

#####################################################

# 2 exercicio

# lista1 = ["ana", "giovani", "gisele"]
# lista2 = ["billy", "theo", "gisele"]

# repeats = set(lista1)
# repeats2 = set(lista2)

# ordenada = repeats & repeats2

# intersecao_lista = list(ordenada)

# print(f"O nome repetido é {intersecao_lista}")


#########################################################################
# exercicio 3

# lista1 = ["ana", "giovani", "gisele"]
# lista2 = ["billy", "theo", "gisele"]

# conjunto1 = set(lista1)
# conjunto2 = set(lista2)


# diferenca = conjunto1 - conjunto2

# print(diferenca)

################################################################################

# exercicio 4

# user = input("Digite sua frase: ")

# frase = user.split()

# unicas = []

# for palavra in frase:
#     if palavra not in unicas: # se a palavra nao estiver no array unicas.
#         unicas.append(palavra)  # ele adiciona ao array unicas pelo .append()

# print("\nPalavras unicas:")
# for palavra in unicas: # o for percorre a frase e verifica se palavra esta dentro de unicas
#     print(palavra)

####################################################################################

# exercicio 5

# pergunta = input("Digite uma palavra: ") # cria uma variavel para a pergunta ao usuario

# if len(set(pergunta)) == len(pergunta): # o set transforma a pergunta em um conjunto / a função len me retorna numero de itens num objeto
#     print("Todos os caracteres são diferentes")
# else:
#     print("A palavra tem caracteres iguais")

 ##############################################################################################################

