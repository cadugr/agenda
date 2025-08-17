def adicionar_contato(lista_contatos, contato):
    """Adiciona um contato à lista de contatos."""
    lista_contatos.append(contato)
    print(f"Contato {contato['nome']} adicionado com sucesso!")
    return

def visualizar_contatos(lista_contatos):
    """Exibe todos os contatos na lista."""
    if not lista_contatos:
        print("Nenhum contato cadastrado.")
    else:
        print("Lista de contatos:")
        for i, contato in enumerate(lista_contatos, start=1):
            favorito = " ♥" if contato['favorito'] else " "
            print(f"{i}. nome: {contato['nome']} - telefone: {contato['telefone']} - e-mail: {contato['email']}{favorito}")
    return        

def editar_contato(lista_contatos, indice, contato_alterado):
    """Edita um contato na lista."""
    if 0 <= indice < len(lista_contatos):
        lista_contatos[indice] = contato_alterado
        print(f"Contato {contato_alterado['nome']} editado com sucesso!")
    else:
        print("Índice inválido.") 
    return               

def marcar_contato_favorito(lista_contatos, indice):
    """Marca um contato como favorito."""
    if 0 <= indice < len(lista_contatos):
        lista_contatos[indice]['favorito'] = True
        print(f"Contato {lista_contatos[indice]['nome']} marcado como favorito.")
    else:
        print("Índice inválido.")
    return    

def desmarcar_contato_favorito(lista_contatos, indice):
    """Desmarca um contato como favorito."""
    if 0 <= indice < len(lista_contatos):
        lista_contatos[indice]['favorito'] = False
        print(f"Contato {lista_contatos[indice]['nome']} desmarcado como favorito.")
    else:
        print("Índice inválido.")
    return    

def visualizar_contatos_favoritos(lista_contatos):
    """Exibe todos os contatos favoritos na lista."""
    favoritos = [contato for contato in lista_contatos if contato['favorito']]
    if not favoritos:
        print("Nenhum contato favorito.")
    else:
        print("Lista de contatos favoritos:")
        for i, contato in enumerate(lista_contatos, start=1):
            if contato['favorito']:
                favorito = " ♥" if contato['favorito'] else " "
                print(f"{i}. nome: {contato['nome']} - telefone: {contato['telefone']} - e-mail: {contato['email']} {favorito}")
    return            

def apagar_contato(lista_contatos, indice):
    """Apaga um contato da lista."""
    if 0 <= indice < len(lista_contatos):
        contato_removido = lista_contatos.pop(indice)
        print(f"Contato {contato_removido['nome']} apagado com sucesso!")
    else:
        print("Índice inválido.")
    return    

def buscar_contato_por_indice(lista_contatos, indice):
    """Busca um contato pelo índice."""
    if 0 <= indice < len(lista_contatos):
        return lista_contatos[indice]
    else:
        return None