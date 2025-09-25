with open("alunos.txt", "w") as nomes:
    nomes.write("Giovani")
    nomes.write("Ana")
    nomes.write("jose")
    
with open("alunos.txt", "r") as nomes:
    for nome in nomes:
        print(nome.strip())