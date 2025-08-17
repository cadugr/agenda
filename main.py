import funcoes.agenda as agenda

agenda_contatos = []
contato = {}

while True:
    
    print("\nMenu do aplicativo Agenda:")
    print(" ____________________________________")
    print("|                                    |")
    print("| 1. Adicionar um contato            |")
    print("| 2. Visualizar contatos             |")
    print("| 3. Editar contato                  |")
    print("| 4. Marcar contato como favorito ♥  |")
    print("| 5. Desmarcar contato como favorito |")
    print("| 6. Visualizar contatos favoritos   |")
    print("| 7. Apagar contato                  |")
    print("| 8. Sair                            |")
    print("|____________________________________|")

    escolha = input("\nDigite a sua escolha: ")

    if escolha == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        contato = {'nome': nome, 'telefone': telefone, 'email': email, 'favorito': False}
        agenda.adicionar_contato(agenda_contatos, contato)
    elif escolha == '2':
        agenda.visualizar_contatos(agenda_contatos)
    elif escolha == '3':
         agenda.visualizar_contatos(agenda_contatos)
         indice = int(input("Digite o número do contato a ser editado: ")) - 1
         contatoSalvo = agenda.buscar_contato_por_indice(agenda_contatos, indice)
         if contatoSalvo is None:
             print("Contato não encontrado.")
             continue
         if input("Deseja alterar o nome do contato? (s/n): ").lower() == 's':
             contatoSalvo["nome"] = input("Digite o novo nome do contato: ") 
         if input("Deseja alterar o telefone do contato? (s/n): ").lower() == 's': 
            contatoSalvo["telefone"] = input("Digite o novo telefone do contato: ")
         if input("Deseja alterar o e-mail do contato? (s/n): ").lower() == 's': 
            contatoSalvo["email"] = input("Digite o novo e-mail do contato: ")
         agenda.editar_contato(agenda_contatos, indice, contatoSalvo)    
    elif escolha == '4':
         agenda.visualizar_contatos(agenda_contatos)
         indice = int(input("Digite o número do contato a ser marcado como favorito: ")) - 1
         agenda.marcar_contato_favorito(agenda_contatos, indice)
    elif escolha == '5':
         agenda.visualizar_contatos(agenda_contatos)
         indice = int(input("Digite o número do contato a ser desmarcado como favorito: ")) - 1
         agenda.desmarcar_contato_favorito(agenda_contatos, indice)
    elif escolha == '6':
        agenda.visualizar_contatos_favoritos(agenda_contatos)
    elif escolha == '7':
        agenda.visualizar_contatos(agenda_contatos)
        indice = int(input("Digite o número do contato a ser apagado: ")) - 1
        agenda.apagar_contato(agenda_contatos, indice)             
    elif escolha == '8':
       break
   
print("Programa finalizado.")    
