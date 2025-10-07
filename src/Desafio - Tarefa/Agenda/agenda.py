from contato import Contato, Agenda

def menu():
    agenda = Agenda()

    while True:
        print("\n----- AGENDA -----")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Editar contato")
        print("4. Deletar contato")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email:")
            contato = Contato(nome, telefone, email)
            agenda.adicionar_contato(contato)
        
        elif escolha == "2":
            agenda.listar_contatos()

        elif escolha == "3":
            agenda.listar_contatos()
            try:
                indice = int(input("Numero do contato para editar: ")) -1
                nome = input("Novo nome:")
                telefone = input("Novo telefone: ")
                email = input("Novo email: ")
                agenda.editar_contato(indice, nome, telefone, email)
            except ValueError:
                print("Entrada invalida!")

        elif escolha == "4":
            agenda.listar_contatos()
            try:
                indice = int(input("Numero do contato para deletar: "))
                agenda.deletar_contato(indice)
            except ValueError:
                print("Entrada invalida!")
                
        elif escolha == "5":
            print("Saindo da agenda...")
            break
        else:
            print("Opção invalida.")

if __name__ == "__main__":
    menu()