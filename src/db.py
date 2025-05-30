import sqlite3
import bcrypt


# Devuelve una conexión a la base de datos SQLite
def obtener_conexion():
    return sqlite3.connect("users.db")


# Inicializa la base de datos y crea la tabla de usuarios si no existe.
# También crea el usuario admin por defecto si no está presente.
def inicializar_bd():
    with obtener_conexion() as conn:
        c = conn.cursor()
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS usuarios (
            usuario TEXT PRIMARY KEY,
            contrasena TEXT NOT NULL,
            nombre TEXT NOT NULL,
            rol TEXT NOT NULL
        )
        """
        )
        # Crear el usuario admin si no existe
        c.execute("SELECT * FROM usuarios WHERE usuario = 'admin'")
        if not c.fetchone():
            hashed = bcrypt.hashpw("admin123".encode(), bcrypt.gensalt()).decode()
            c.execute(
                "INSERT INTO usuarios (usuario, contrasena, nombre, rol) VALUES (?, ?, ?, ?)",
                ("admin", hashed, "Administrador", "admin"),
            )
        conn.commit()


# Obtiene un usuario por su nombre de usuario
def obtener_usuario(usuario):
    with obtener_conexion() as conn:
        c = conn.cursor()
        c.execute(
            "SELECT usuario, contrasena, nombre, rol FROM usuarios WHERE usuario = ?",
            (usuario,),
        )
        return c.fetchone()


# Agrega un nuevo usuario a la base de datos
def agregar_usuario(usuario, contrasena, nombre, rol="usuario"):
    with obtener_conexion() as conn:
        c = conn.cursor()
        c.execute(
            "INSERT INTO usuarios (usuario, contrasena, nombre, rol) VALUES (?, ?, ?, ?)",
            (usuario, contrasena, nombre, rol),
        )
        conn.commit()


# Actualiza el nombre de un usuario existente
def actualizar_usuario(usuario, nombre):
    with obtener_conexion() as conn:
        c = conn.cursor()
        c.execute("UPDATE usuarios SET nombre = ? WHERE usuario = ?", (nombre, usuario))
        conn.commit()


# Elimina un usuario de la base de datos
def eliminar_usuario(usuario):
    with obtener_conexion() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM usuarios WHERE usuario = ?", (usuario,))
        conn.commit()


# Devuelve una lista de todos los usuarios (usuario, nombre, rol)
def listar_usuarios():
    with obtener_conexion() as conn:
        c = conn.cursor()
        c.execute("SELECT usuario, nombre, rol FROM usuarios")
        return c.fetchall()


# Inicializa la base de datos al importar el módulo
inicializar_bd()
