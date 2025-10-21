######################################################################################################

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
    
#     def apresentar(self):
#         print(f"O meu nome é {self.nome} e eu tenho {self.idade} anos")

#     def fazer_aniversario(self):
#         self.idade += 1
        

    
# pessoa1 = Pessoa("Giovani", 17)
# pessoa2 = Pessoa("Ana", 17)

# pessoa1.apresentar()
# pessoa2.apresentar()

# pessoa1.fazer_aniversario()

# pessoa1.apresentar()

##################################################################################################################################

# class conta_bancaria:
#     def __init__(self, titular):
#         self.titular = titular
#         self.saldo = 0
        
#     def depositar(self, valor):
#         self.saldo += valor
#         print(f"Depósito de R${valor: .2f} realizado! Saldo atual: R${self.saldo: .2f}")
    
#     def sacar(self, valor):
#         if valor <= self.saldo:
#             self.saldo -+ valor
#             print(f"Saque de R${valor: .2f} realizado! Saldo atual: R${self.saldo: .2f}")
#         else:
#             print("ERRO: Saldo insuficiente na conta.")
    
#     def mostrar_saldo(self):
#         print(f"Saldo final de{self.titular}: R${self.saldo: .2f}")
    
# conta = conta_bancaria("Giovani")
# conta.depositar(500)
# conta.sacar(200)
# conta.sacar(400)
# conta.mostrar_saldo()


# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.__titular = titular
#         self.__saldo = saldo

#      # GETTER
#     def get_saldo(self):
#             return self.__saldo
#     # SETTER    
#     def depositar(self, valor):
#             self.__saldo += valor

# conta = ContaBancaria("Giovani", 1000)
# print(f"Seu valor em caixa: R$ {conta.get_saldo()}")
# conta.depositar(777)
# print(f"Seu valor em caixa após o depósito: R$ {conta.get_saldo()}")        


# Herança ->
# class Animal:
#     def __init__(self, nome):
#         self.nome = nome

#         def emitir_som(self):
#             print("som estranho")

# class Cachorro(Animal):
#     def emitir_som(self): # Sobrescreve o método.
#         print("Au au au")

# class Gato(Animal):
#     def emitir_som(self):
#         print("Miauuuuu")

# dog = Cachorro("yuri")
# cat = Gato("Remy")

# dog.emitir_som()
# cat.emitir_som()
##################################################################################### 
# class Funcionario:
#     def __init__(self, nome, salario):
#         self.nome = nome
#         self.__salario = salario

#     def get_salario(self):
#         return self.__salario

#     def setar_salario(self, salario):
#         self.__salario = salario


# class Gerente(Funcionario):
#     def __init__(self, nome, salario, departamento):
#         Funcionario.__init__(self, nome, salario)
#         self.departamento = departamento

#     def mostrar_departamento(self):
#         print(f"O gerente {self.nome} é reponse pelo departamento de {self.departamento}")



# f1 = Funcionario("Giovani", 4000)
# print(f"Seu salário é de: R$ {f1.get_salario()}")
# f1.setar_salario(7000)
# print(f"Seu novo salário é de: R$ {f1.get_salario()}")

# # Instanciando um Gerente
# gerente = Gerente("Amanda", 9000, "Recursos Humanos")
# print(f"Salário da gerente: R$ {gerente.get_salario()}")
# print(gerente.mostrar_departamento())

########################################################################################################################################
# class Produto:
#     def __init__(self, nome, preco):
#         self.__nome = nome
#         self.__preco = preco

#     def get_preco(self):
#         return self.__preco

#     def setar_preco(self, preco):
#         self.__preco = preco  

# p1 = Produto("Agua", 10)
# p2 = Produto("pão", 12)


# preco_com_desconto = p1.get_preco() * 0.9
# preco_com_desconto2 = p2.get_preco() * 0.9
# p1.setar_preco(preco_com_desconto)
# p2.setar_preco(preco_com_desconto2)

# print(f"O valor da agua com 10% de desconto é de: R$ {p1.get_preco():.2f}")
# print(f"O valor do pao com 10% de desconto é de: R$ {p2.get_preco():.2f}")

######################################################################################################################

# class Veiculo:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

#     def __str__(self):
#         return f"{self.marca} {self.modelo} ({self.ano})"
    
# class Carro(Veiculo):
#     def mostrar_tipo(self):
#         print("")

# class Moto(Veiculo):
#     def mostrar_tipo(self):
#         print("")


# golf = Carro("Volkswagen | ", "MK4 | ",  2007)
# cg = Moto("CG | ", "fan | ", 2001)

# golf.mostrar_tipo()
# cg.mostrar_tipo()
# print(f"{golf}")
# print(f"{cg}")
###################################################################################################################

# class Funcionario:
#     def trabalhar(self):
#         print("O funcionario esta trabalhando normalmente")

# class Estagiario(Funcionario):
#     def trabalhar(self):
#         print("O estagiario esta aprendendo")

# funcionario1 = Funcionario()
# estagiario1 = Estagiario()

# funcionario1.trabalhar()
# estagiario1.trabalhar()

###################################################################################################

# class ContaCorrente:
#     def __init__(self, saldo):
#         self.__saldo = saldo

#     def depositar(self, valor):
#         if valor > 0:
#             self.__saldo += valor
#             print(f"Depósito de R$ {valor} ralizado com sucesso")
#         else:
#             print("Valor inválido")

#     def sacar(self, valor):
#         if valor <= 0:
#             print("Valor invalido")
#         elif valor <= self.__saldo:
#             self.__saldo -= valor
#             print(f"seu saque foi concluido no valor de {valor:.2f}")
#         else:
#             print("saldo insuficiente!")

#     def consultar_saldo(self):
#         print(f"Saldo atual: R$ {self.__saldo}")

# valor1 = ContaCorrente(100)
# valor1.depositar(50)
# valor1.consultar_saldo()
# valor1.sacar(50)
# valor1.consultar_saldo()

######################################################################################################################

# class Aluno:
#     def __init__(self, nome, nota):
#         self.__nome = nome
#         self.__nota = nota
    
#     def get_nota(self):
#         return self.__nota
    
#     def set_nota(self):
#         if self.__nota > 0:
#             print("Sua nota foi aceita!")
#         else:
#             print("Sua nota não foi aceita!")

#     def nota_max(self):
#         if self.__nota == 10:
#             print("Parabéns você tirou nota máxima!!")

# nota1 = Aluno("Giovani", 9)
# nota1.get_nota()
# nota1.set_nota()
# nota1.nota_max()
        
################################################################################################################
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
    
# class Professor(Pessoa):
#     def __init__(self, nome, idade, materia):
#         super().__init__(nome, idade)
#         self.materia = materia

# pessoa1 = Pessoa()
# prof1 = Professor()

###############################################################################################################

# class Veiculo:
#     def __init__(self, nome):
#         self.nome = nome
    
#     def mover(self):
#         print("Carro parado")

# class Carro(Veiculo):
#     def mover(self):
#         print("Isso é um carro e estou dirigindo o carro!")

# class Bicicleta(Veiculo):
#     def mover(self):
#         print("Isso é uma bike e estou pedalando!")

# carro = Carro("Golf")
# bicicleta = Bicicleta("KSW")

# carro.mover()
# bicicleta.mover()

###################################################################################################################

# class Usuario:
#     def __init__(self, nome, senha):
#         self.nome = nome
#         self.__senha = senha
        

#     def alterar_senha(self, antiga, nova):
#         if antiga == self.__senha:
#             self.__senha = nova
#             print("A senha foi alterada!")

#         else:
#             print("A senha antiga esta incorreta ")

#     def login(self, senha):
#         if senha == self.__senha:
#             print(f"Aceso permitido. Bem vindo {self.nome}")
#         else:
#             print("Senha incorreta")

# user = Usuario("Giovani", "124")
# user.login("124")

#########################################################################################################################

# class Animal:
#     def mover(self):
#         print("o animal ta andando")

# class Mamifero(Animal):
#     def amamentar(self):
#         print("ta amamentando")

# class Cachorro(Mamifero):
#     def latir(self):
#         print("ta latindo")


# dog = Cachorro()

# dog.mover()
# dog.amamentar()
# dog.latir()

########################################################################################################

# from abc import ABC, abstractclassmethod

# class Instrumento(ABC):
#     @abstractclassmethod
#     def tocar(self):
#         pass

# class Violao(Instrumento):
#     def tocar(self):
#         print("o violao esta tocadando um som")

# class Bateria(Instrumento):
#     def tocar(self):
#         print("a bateria esta tocando")

# violao = Violao()
# bateria = Bateria()

# violao.tocar()
# bateria.tocar()

##############################################################################################

# from abc import ABC, abstractclassmethod

# class Funcionario(ABC):
#     @abstractclassmethod
#     def calcular_pagamento(self):
#         pass

# class Assalariado(Funcionario):
#     def __init__(self, salario):
#         self.salario = salario

#     def calcular_pagamento(self):
#         return self.salario
    
# class Horista(Funcionario):
#     def __init__(self, valor_hora, horas_trabalhadas):
#         self.valor_hora = valor_hora
#         self.horas_trabalhadas = horas_trabalhadas

#     def calcular_pagamento(self):
#         return self.valor_hora * self.horas_trabalhadas
    
# f1 = Assalariado(3000)
# f2 = Horista(50, 60)

# f1.calcular_pagamento()


###############################################################################################################################
# from viagem_class import viagem_class

# viagem_0 = viagem_class("Florida")
# viagem_1 = viagem_class("Havai")
# viagem_2 = viagem_class("Toquio")
# viagem_3 = viagem_class("Egito")

# print("------------------------------------------------------------------------")
# print("Bem-Vindo ! viagens senai tem ofertas pra vc")

# viajante = input("Digite seu nome para comerçarmos: ")

# print(f"{viajante} Temos 4 destinos para voce: "
# '''
#       [0] Florida
#       [1] havai
#       [2] toquio
#       [3] egito
# '''
# )
    


# selecao = int(input("Selecione o numero da viagem desejada: "))
# lista_viagem = [viagem_0, viagem_1, viagem_2, viagem_3]
# opcao_selecionada = int(selecao)
# for opcao in lista_viagem:
#     if opcao_selecionada >= 4:
#         print("Esta opção nao esta incluida!")
#         break
#     if opcao_selecionada <= 3:
#         print(f"{viajante} sua viagem para {lista_viagem[opcao_selecionada].destino} está marcada.")
#         print("Volte sempre!")
#         break


# from biblioteca import biblioteca

# e0 = biblioteca("Seja um programador inteligente!")
# e1 = biblioteca("POO")
# e2 = biblioteca("Manual da programação")

# print("------------------------------------------------------------")
# print("Bem-Vindo à Biblioteca de Freitas, Giovani")

# solicitante = input("Digite seu nome: ")

# print(f"{solicitante} temos esses livros disponiveis para o emprestimo"
# '''
#     [0] Seja um programador inteligente!
#     [1] POO
#     [2] Manuel da programação
# '''
# )

# selecao = int(input("Selecione o livro desejado: "))
# lista_livros = [e0, e1, e2]
# opcao_selecionada = int(selecao)
# for opcao in lista_livros:
#     if opcao_selecionada >= 4:
#         print("Este livro nao esta disponivel")
#     if opcao_selecionada <= 3:
#         print(f"{solicitante} Seu livro {lista_livros[opcao_selecionada].estante} é seu durante o emprestimo!!")
#         print("Te espero no dia da devolução!")
#         break



#####################################################################################################################################

# exemplo com o construtor Dataclass

# from dataclasses import dataclass

# @dataclass
# class Produto:
#     nome: str
#     preco: float
#     estoque: int = 0

# p1 = Produto("Caneta", 2.50, 10)
# p2 = Produto("Caneta", 2.50, 10)

# print(p1)
# print(p1 == p2)


############################################################################################################################
# import sqlite3

# conexao = sqlite3.connect('meubanco.db')

# cursor = conexao.cursor()


# cursor.execute('''
# CREATE TABLE IF NOT EXISTS usuarios (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     email TEXT UNIQUE NOT NULL
# )  
#  ''')

# cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', ("Giovani", 'giovanif@email.com'))

# conexao.commit()
# conexao.close()

# print("Banco criado e usuário inserido com sucesso!")

###################################################################################################################################
import sqlite3

conexao = sqlite3.connect('loja.db')

cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome  TEXT NOT NULL,
    preco INTEGER NOT NULL,
    estoque INTEGER NOT NULL
)
''')

produto = [
    ("Agua", 10, 10),
    ("pao", 10, 2),
    ("Bolo", 10, 5)

]

cursor.executemany('INSERT INTO produtos (nome, preco, estoque) VALUES (?,?,?)',produto )


conexao.commit()
conexao.close()

print("Banco criado com sucesso!")
print(produto)
