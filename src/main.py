from modules.auxilliary import titulo
from modules.options import options
from modules.todo import todo
from modules.routine import routine

# Main
def main() -> None:
    main_titulo = titulo(
        "An CLI App",
        "What u wanna do?\nCredits to bcsarah@github.com",
        {"To-Do": todo, "Routine": routine, "Options": options})

main()