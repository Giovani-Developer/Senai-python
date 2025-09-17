lista_compras = []

while True:
    item = input("digite um item para adicionar a lista ou ('sair' ) para finalizar:  ")

    if item.lower() == "sair": # transforma todo o conteudo em minuscula
        break

    lista_compras.append(item) # .append adiciona um valor no array

print("\nSua lista de compras:")

lista_ordenada = sorted(lista_compras)
for i, produto in enumerate(lista_compras):
  
    print(f"{i}. {produto}")



