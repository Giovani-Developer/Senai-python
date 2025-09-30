# nome = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")

# with open("Usuarios.txt", "a") as nomes:
#     nomes.write(f"{nome} : {idade}")

# with open("nomes.txt", "a") as nomes:
#     nomes.write("Giovani ")
#     nomes.write("Ana")

# with open("nomes.txt", "r") as nomes:
#     for nome in nomes:
#         print(nome.strip())

# with open("nomes.txt", "r") as nome:
#     nomes = nome.readlines()

# nomes_formatados = []
# for n in nomes:
#     n = n.strip().lower() + "\n"
#     nomes_formatados.append(n)

# with open("nomes.txt", "w") as arq:
#     arq.writelines(nomes_formatados)

# with open("nomes.txt", "r") as nome:
#     for nome in nomes:
#         print(nome)

# with open("Usuarios.txt", "r") as arq:
#     linhas = arq.readlines()

# linhas_formatadas = []
# for linha in linhas:
#     nome, idade = linha.strip().split(";")
#     linhas_formatadas.append(f"{nome.upper()};{idade}\n")


# with open("Usuarios.txt", "w") as arq:
#     arq.writelines(linhas_formatadas)

try:
    with open("log.txt", "x")as arq:
        arq.write("Arquivo criado com sucesso! \n")
except FileExistsError:
    print("O arquivo log.txt já existe.")
