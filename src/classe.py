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
        

class conta_bancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor: .2f} realizado! Saldo atual: R${self.saldo: .2f}")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -+ valor
            print(f"Saque de R${valor: .2f} realizado! Saldo atual: R${self.saldo: .2f}")
        else:
            print("ERRO: Saldo insuficiente na conta.")
    
    def mostrar_saldo(self):
        print(f"Saldo final de{self.titular}: R${self.saldo: .2f}")
    
conta = conta_bancaria("Giovani")
conta.depositar(500)
conta.sacar(200)
conta.sacar(400)
conta.mostrar_saldo()
