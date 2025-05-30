from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.table import Table
import db
import utils

console = Console()

# Clase Usuario (no es obligatoria para el flujo, pero útil si quieres OO)
class Usuario:
    def __init__(self, usuario, contrasena, nombre):
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre

    def actualizar_datos(self, nombre=None):
        if nombre:
            self.nombre = nombre

    @staticmethod
    def validar_credenciales(contrasena_guardada, contrasena_ingresada):
        return contrasena_guardada == contrasena_ingresada

    def a_diccionario(self):
        return {
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "nombre": self.nombre,
        }

# Función para iniciar sesión con control de intentos y espera
def iniciar_sesion():
    intentos = 0
    while True:
        console.clear()
        console.print(Panel("[bold cyan]Inicio de Sesión[/bold cyan]", expand=False))
        usuario = Prompt.ask("Usuario")
        contrasena = Prompt.ask("Contraseña", password=True)
        datos = db.obtener_usuario(usuario)
        if datos and utils.verificar_contrasena(contrasena, datos[1]):
            return {"usuario": datos[0], "nombre": datos[2], "rol": datos[3]}
        else:
            intentos += 1
            console.print(f"[red]Usuario o contraseña incorrectos. Intento {intentos}/5[/red]")
            if intentos >= 5:
                console.print("[yellow]Demasiados intentos fallidos. Espere 5 segundos...[/yellow]")
                import time; time.sleep(5)
                intentos = 0

# Función para registrar un nuevo usuario
def registrar_usuario():
    console.clear()
    console.print(Panel("[bold green]Registro de Usuario[/bold green]", expand=False))
    usuario = Prompt.ask("Nuevo usuario")
    if db.obtener_usuario(usuario):
        console.print("[red]El usuario ya existe.[/red]")
        return
    nombre = Prompt.ask("Nombre completo")
    contrasena = Prompt.ask("Contraseña", password=True)
    hashed = utils.hash_contrasena(contrasena)
    db.agregar_usuario(usuario, hashed, nombre)
    console.print("[green]¡Usuario registrado correctamente![/green]")

# Menú principal según el rol del usuario
def menu_usuario(usuario):
    while True:
        console.clear()
        console.print(Panel(f"[bold blue]Bienvenido, {usuario['nombre']} ({usuario['usuario']})[/bold blue]\n[cyan]Rol: {usuario['rol']}[/cyan]", expand=False))
        if usuario['rol'] == "admin":
            console.print("[yellow]Usuarios registrados:[/yellow]")
            tabla = Table("Usuario", "Nombre", "Rol")
            for u in db.listar_usuarios():
                tabla.add_row(*u)
            console.print(tabla)
            console.print("\n[bold]Opciones:[/bold]\n1. Crear usuario\n2. Editar usuario\n3. Eliminar usuario\n4. Cerrar sesión")
            op = Prompt.ask("Selecciona una opción", choices=["1", "2", "3", "4"])
            if op == "1":
                registrar_usuario()
            elif op == "2":
                usuario_editar = Prompt.ask("Usuario a editar")
                if db.obtener_usuario(usuario_editar):
                    nombre = Prompt.ask("Nuevo nombre")
                    db.actualizar_usuario(usuario_editar, nombre)
                    console.print("[green]Usuario actualizado.[/green]")
                else:
                    console.print("[red]Usuario no encontrado.[/red]")
                Prompt.ask("Presiona Enter para continuar")
            elif op == "3":
                usuario_eliminar = Prompt.ask("Usuario a eliminar")
                if usuario_eliminar == "admin":
                    console.print("[red]No puedes eliminar el usuario admin.[/red]")
                elif db.obtener_usuario(usuario_eliminar):
                    db.eliminar_usuario(usuario_eliminar)
                    console.print("[green]Usuario eliminado.[/green]")
                else:
                    console.print("[red]Usuario no encontrado.[/red]")
                Prompt.ask("Presiona Enter para continuar")
            elif op == "4":
                break
        else:
            console.print("\n[bold]Opciones:[/bold]\n1. Ver mis datos\n2. Editar mi nombre\n3. Cerrar sesión")
            op = Prompt.ask("Selecciona una opción", choices=["1", "2", "3"])
            if op == "1":
                console.print(f"Usuario: {usuario['usuario']}\nNombre: {usuario['nombre']}")
                Prompt.ask("Presiona Enter para continuar")
            elif op == "2":
                nombre = Prompt.ask("Nuevo nombre")
                db.actualizar_usuario(usuario['usuario'], nombre)
                usuario['nombre'] = nombre
                console.print("[green]Nombre actualizado.[/green]")
                Prompt.ask("Presiona Enter para continuar")
            elif op == "3":
                break