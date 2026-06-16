from .auxilliary import ler_arquivo, salvar_arquivo, titulo, input_seguro

# Adiciona um To-Do na lista
def adicionar_todo() -> None:
    todo_lista = ler_arquivo('todo')

    nome = input("Nome: ")
    comeco = input("Começo (dd/mm): ")
    fim = input("Fim (dd/mm): ")

    novo_todo = {"Nome": nome, "Começo": comeco, "Fim": fim}

    todo_lista.append(novo_todo)
    salvar_arquivo('todo', todo_lista)

# Remove um To-Do da lista
def remover_todo() -> None:
    todo_lista = ler_arquivo('todo')

    while True:
        todo_para_remover = input("Nome para remover: ").strip()
        
        if todo_para_remover in todo_lista:
            todo_lista.remove(todo_para_remover)
            salvar_arquivo(todo_lista)
            break
        else:
            print("To-Do não encontrado. Tente Novamente.\n")

# Edita informações de um To-Do
def editar_todo() -> None:
    pass

# To-Do
def mostrar_todo() -> None:
    while True:
        todo_lista = ler_arquivo('todo')

        # Cria a descrição
        desc = ""
        i = 0
        for todo in todo_lista:
            delimiter = ""
            desc = delimiter.join(f"{todo["Nome"]} ({todo["Começo"]} - {todo["Fim"]})")
            i += 1

        # Título
        match titulo(
            "To-Do",
            desc,
            ("Adicionar", "Remover", "Editar")):
            case 1:
                adicionar_todo()
            case 2:
                remover_todo()
            case 3:
                editar_todo()
            case 0:
                break