
from abc import ABC, abstractmethod
from enum import Enum




class Pessoa(ABC):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @abstractmethod
    def apresentar(self):
        pass


class Cliente(Pessoa):
    def __init__(self, nome, email, endereco):
        super().__init__(nome, email)
        self.endereco = endereco

    def apresentar(self):
        return f"Sou cliente {self.nome}, moro em {self.endereco}."



class Funcionario(Pessoa):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

    def apresentar(self):
        return f"Sou funcionário {self.nome}, trabalho como {self.cargo}."




class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"


class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f" Produto '{produto.nome}' adicionado ao carrinho.")

    def calcular_total(self):
        return sum(p.preco for p in self.produtos)

    def listar_produtos(self):
        if not self.produtos:
            print(" O carrinho está vazio.")
        else:
            print("\n Produtos no carrinho:")
            for p in self.produtos:
                print(f" - {p}")




class StatusPedido(Enum):
    PENDENTE = "Pendente"
    PAGO = "Pago"
    ENVIADO = "Enviado"
    ENTREGUE = "Entregue"


class Pedido:
    def __init__(self, cliente, carrinho):
        self.cliente = cliente
        self.produtos = carrinho.produtos
        self.valor_total = carrinho.calcular_total()
        self.status = StatusPedido.PENDENTE

    def alterar_status(self, novo_status):
        self.status = novo_status
        print(f" Status do pedido alterado para: {self.status.value}")

    def resumo_pedido(self):
        print("\n===== RESUMO DO PEDIDO =====")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Email: {self.cliente.email}")
        print(f"Endereço: {self.cliente.endereco}")
        print("\nItens do pedido:")
        for produto in self.produtos:
            print(f" - {produto}")
        print(f"\n Valor total: R${self.valor_total:.2f}")
        print(f" Status: {self.status.value}")
        print("=============================")





cliente1 = Cliente("Giovani Freitas", "giovani123@gmail.com", "Rua das Flores, 123")
funcionario1 = Funcionario("João Silva", "joao@empresa.com", "Atendente")


notebook = Produto("Notebook", 3500.00)
mouse = Produto("Mouse sem fio", 150.00)
teclado = Produto("Teclado mecânico", 250.00)


carrinho_cliente = Carrinho()
carrinho_cliente.adicionar_produto(notebook)
carrinho_cliente.adicionar_produto(mouse)
carrinho_cliente.adicionar_produto(teclado)

carrinho_cliente.listar_produtos()


pedido1 = Pedido(cliente1, carrinho_cliente)


pedido1.resumo_pedido()


pedido1.alterar_status(StatusPedido.PAGO)


pedido1.resumo_pedido()


print("\n--- Apresentações ---")
print(cliente1.apresentar())

print(funcionario1.apresentar())
from abc import ABC, abstractmethod
from enum import Enum




class Pessoa(ABC):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @abstractmethod
    def apresentar(self):
        pass



class Cliente(Pessoa):
    def __init__(self, nome, email, endereco):
        super().__init__(nome, email)
        self.endereco = endereco

    def apresentar(self):
        return f"Sou cliente {self.nome}, moro em {self.endereco}."



class Funcionario(Pessoa):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.cargo = cargo

    def apresentar(self):
        return f"Sou funcionário {self.nome}, trabalho como {self.cargo}."




class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"


class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f" Produto '{produto.nome}' adicionado ao carrinho.")

    def calcular_total(self):
        return sum(p.preco for p in self.produtos)

    def listar_produtos(self):
        if not self.produtos:
            print(" O carrinho está vazio.")
        else:
            print("\n Produtos no carrinho:")
            for p in self.produtos:
                print(f" - {p}")




class StatusPedido(Enum):
    PENDENTE = "Pendente"
    PAGO = "Pago"
    ENVIADO = "Enviado"
    ENTREGUE = "Entregue"


class Pedido:
    def __init__(self, cliente, carrinho):
        self.cliente = cliente
        self.produtos = carrinho.produtos
        self.valor_total = carrinho.calcular_total()
        self.status = StatusPedido.PENDENTE

    def alterar_status(self, novo_status):
        self.status = novo_status
        print(f" Status do pedido alterado para: {self.status.value}")

    def resumo_pedido(self):
        print("\n===== RESUMO DO PEDIDO =====")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Email: {self.cliente.email}")
        print(f"Endereço: {self.cliente.endereco}")
        print("\nItens do pedido:")
        for produto in self.produtos:
            print(f" - {produto}")
        print(f"\n Valor total: R${self.valor_total:.2f}")
        print(f" Status: {self.status.value}")
        print("=============================")





cliente1 = Cliente("Giovani Freitas", "giovani123@gmail.com", "Rua das Flores, 123")
funcionario1 = Funcionario("João Silva", "joao@empresa.com", "Atendente")


notebook = Produto("Notebook", 3500.00)
mouse = Produto("Mouse sem fio", 150.00)
teclado = Produto("Teclado mecânico", 250.00)


carrinho_cliente = Carrinho()
carrinho_cliente.adicionar_produto(notebook)
carrinho_cliente.adicionar_produto(mouse)
carrinho_cliente.adicionar_produto(teclado)

carrinho_cliente.listar_produtos()


pedido1 = Pedido(cliente1, carrinho_cliente)


pedido1.resumo_pedido()


pedido1.alterar_status(StatusPedido.PAGO)


pedido1.resumo_pedido()


print("\n--- Apresentações ---")
print(cliente1.apresentar())

print(funcionario1.apresentar())
