# with open("alunos.txt", "w") as nomes:
#     nomes.write("Gabriel\n")
#     nomes.write("Giovani\n")

# with open("alunos.txt", "a") as nomes:
#     nomes.write("Essa mensagem foi adiciona com o append")



# with open("alunos.txt", "r") as nomes:
#     for nome in nomes:
#         print(nome.strip())


linhas = ["Joao\n", "Maria\n", "Pedro\n"]
with open("participantes.txt", "w") as nomes:
    nomes.writelines(linhas)