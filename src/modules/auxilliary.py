from pyfiglet import figlet_format
from os import system
import json

# Lê um arquivo json, retornando ele em dicionário
def ler_arquivo(arquivo: str) -> dict:
    with open(f"data/{arquivo}.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

# Salva um arquivo json
def salvar_arquivo(arquivo: str, dados: list) -> None:
    with open(f"data/{arquivo}.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def input_seguro(prompt: str) -> str:
    return input(prompt).lower().strip()

# Cria uma arte ascii com base no texto
def criar_arte_ascii(texto: str) -> None:
    system("clear")
    print(figlet_format(texto, "small"), end="")

# Cria um título, com descrições e opcoes
def titulo(cabecalho: str, descricao: str = "", opcoes: list=[], voltar: bool = True) -> int:
    while True:
        criar_arte_ascii(cabecalho)

        # Descrição
        if descricao:
            for linha in descricao.splitlines():
                print(f"  {linha}")
            print()

        # Opções
        i = 1
        for opcao in opcoes:
            print(f"{i} -> {opcao}")
            i += 1

        if voltar:
            print("\n0 -> Voltar")

        # Input (se houver opções)
        if opcoes:
            try:
                uinput = int(input(">> "))
            except ValueError:
                continue

            print()

            # Validação
            if uinput >= 1 and uinput <= i-1 or uinput == 0 and voltar:
                return uinput
