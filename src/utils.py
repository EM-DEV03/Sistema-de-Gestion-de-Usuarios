import bcrypt

# Hashea una contraseña usando bcrypt
def hash_contrasena(contrasena):
    return bcrypt.hashpw(contrasena.encode(), bcrypt.gensalt()).decode()

# Verifica si la contraseña ingresada coincide con el hash almacenado
def verificar_contrasena(contrasena, hash_almacenado):
    return bcrypt.checkpw(contrasena.encode(), hash_almacenado.encode())

# Valida que el nombre de usuario tenga al menos 3 caracteres
def validar_usuario(usuario):
    return len(usuario) >= 3

# Valida que la contraseña tenga al menos 6 caracteres
def validar_contrasena(contrasena):
    return len(contrasena) >= 6

# Imprime un mensaje de error
def imprimir_error(mensaje):
    print(f"[ERROR] {mensaje}")

# Imprime un mensaje de éxito
def imprimir_exito(mensaje):
    print(f"[ÉXITO] {mensaje}")