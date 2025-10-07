class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"



class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self.matricula = matricula

    def __str__(self):
        return f"Aluno: {self.nome} | Matrícula: {self.matricula}"



class Professor(Pessoa):
    def __init__(self, nome, cpf, disciplina):
        super().__init__(nome, cpf)
        self.disciplina = disciplina

    def __str__(self):
        return f"Professor: {self.nome} | Disciplina: {self.disciplina}"



class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = set()       
        self.professores = set()  

    def adicionar_aluno(self, aluno):
        self.alunos.add(aluno)
        print(f" Aluno '{aluno.nome}' adicionado ao curso {self.nome}.")

    def adicionar_professor(self, professor):
        self.professores.add(professor)
        print(f" Professor '{professor.nome}' adicionado ao curso {self.nome}.")

    def exibir_dados(self):
        print(f"\n Curso: {self.nome}")
        print(" Professores:")
        if self.professores:
            for prof in self.professores:
                print(" -", prof)
        else:
            print(" (nenhum professor cadastrado)")

        print(" Alunos:")
        if self.alunos:
            for aluno in self.alunos:
                print(" -", aluno)
        else:
            print(" (nenhum aluno matriculado)")



def menu():
    cursos = {}

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Criar curso")
        print("2 - Cadastrar aluno em curso")
        print("3 - Cadastrar professor em curso")
        print("4 - Exibir dados do curso")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do curso: ")
            if nome not in cursos:
                cursos[nome] = Curso(nome)
                print(f" Curso '{nome}' criado com sucesso!")
            else:
                print(" Esse curso já existe.")

        elif opcao == "2":
            nome_curso = input("Digite o nome do curso: ")
            if nome_curso in cursos:
                nome = input("Nome do aluno: ")
                cpf = input("CPF: ")
                matricula = input("Matrícula: ")
                aluno = Aluno(nome, cpf, matricula)
                cursos[nome_curso].adicionar_aluno(aluno)
            else:
                print(" Curso não encontrado.")

        elif opcao == "3":
            nome_curso = input("Digite o nome do curso: ")
            if nome_curso in cursos:
                nome = input("Nome do professor: ")
                cpf = input("CPF: ")
                disciplina = input("Disciplina: ")
                professor = Professor(nome, cpf, disciplina)
                cursos[nome_curso].adicionar_professor(professor)
            else:
                print(" Curso não encontrado.")

        elif opcao == "4":
            nome_curso = input("Digite o nome do curso: ")
            if nome_curso in cursos:
                cursos[nome_curso].exibir_dados()
            else:
                print(" Curso não encontrado.")

        elif opcao == "5":
            print("\n Saindo do sistema. Até logo!")
            break

        else:
            print(" Opção inválida, tente novamente.")



menu()