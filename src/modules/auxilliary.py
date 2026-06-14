from pyfiglet import figlet_format
from os import system

# Lê um arquivo json, retornando ele em dicionário
def ler_arquivo(arquivo:str) -> dict:
    with open(f"data/{arquivo}.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

# Salva um arquivo json
def salvar_arquivo(arquivo:str, dados: list) -> None:
    with open(f"data/{arquivo}.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# Cria uma arte ascii com base no texto
def criar_arte_ascii(texto: str) -> None:
    system("clear")
    print(figlet_format(texto, "small"), end="")

# Cria um título, com descrições e opcoes
def titulo(cabecalho: str, descricao: str = "", opcoes: dict = {}, voltar: bool = True) -> None:
    while True:
        criar_arte_ascii(cabecalho)

        # Descrição
        if descricao:
            for linha in descricao.splitlines():
                print(f"  {linha}")
            print()

        # Opções
        opcoes_lista = list(opcoes.items())

        for i, (opcao, funcao) in enumerate(opcoes_lista, start=1):
            print(f"{i} -> {opcao}")

        if voltar:
            print("\n0 -> Voltar")

        if opcoes:
            # Input
            try:
                uinput: int = int(input(">> "))
            except ValueError:
                continue

            # Validação
            if uinput == 0 and voltar:
                break
            if uinput >= 1 and uinput <= len(opcoes_lista):
                break

    if uinput == 0:
        pass
    else:
        _, func = opcoes_lista[uinput - 1]
        func()
