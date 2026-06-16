from modules.auxilliary import titulo
from modules.options import mostrar_opcoes 
from modules.todo import mostrar_todo
from modules.routine import mostrar_rotina

# Main
def main() -> None:
    while True:
        match titulo(
            "DoPy",
            "Credits to bcsarah@github.com",
            ("To-Do", "Routine", "Opções")):
            case 1:
                mostrar_todo()
            case 2:
                mostrar_rotina()
            case 3:
                mostrar_opcoes()
            case 0:
                break

main()