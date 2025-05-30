import os
import time
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
import db
import user_management

console = Console(force_terminal=True)

def main():
    # Inicializa la base de datos (crea tablas y admin si no existen)
    db.inicializar_bd()
    while True:
        console.clear()
        console.print(Panel(
            "[bold yellow]Sistema de Gestión de Usuarios[/bold yellow]\n"
            "1. Iniciar sesión\n2. Registrarse\n3. Salir",
            expand=False
        ))
        opcion = Prompt.ask("Selecciona una opción", choices=["1", "2", "3"])
        if opcion == "1":
            usuario = user_management.iniciar_sesion()
            user_management.menu_usuario(usuario)
        elif opcion == "2":
            user_management.registrar_usuario()
        elif opcion == "3":
            console.print("[cyan]¡Hasta luego![/cyan]")
            break

if __name__ == "__main__":
    main()