# Documentación del Proyecto: Sistema de Gestión de Usuarios

Este proyecto es una **aplicación de consola** para gestionar usuarios, con un usuario administrador y usuarios normales. Permite **registrar, actualizar, eliminar y validar usuarios**, con control de sesiones, intentos de acceso y persistencia en base de datos SQLite. La interfaz es amigable gracias a la librería [`rich`](https://rich.readthedocs.io/).

---

## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Descripción de Archivos Principales](#descripción-de-archivos-principales)
- [Flujo de Uso](#flujo-de-uso)
- [Documentación de Módulos](#documentación-de-módulos)
  - [utils.py](#utilspy)
  - [db.py](#dbpy)
  - [user_management.py](#user_managementpy)
  - [main.py](#mainpy)
- [Notas](#notas)

---

## Estructura del Proyecto

```
Project
├── src
│   ├── main.py              # Inicio de la aplicación
│   ├── db.py                # Funciones para la base de datos SQLite
│   ├── user_management.py   # Lógica para gestionar usuarios y sesiones
│   └── utils.py             # Utilidades para validación y contraseñas
├── requirements.txt         # Lista de dependencias
├── README.md                # Documentación
└── Documentacion.md         # Este archivo
```

---

## Requisitos

- **Python 3.x**
- **SQLite** (incluido en Python)
- Librerías:
  - [`rich`](https://pypi.org/project/rich/)
  - [`bcrypt`](https://pypi.org/project/bcrypt/)

---

## Instalación y Ejecución

1. **Clona el repositorio:**
   ```sh
   git clone https://github.com/EM-DEV03/Sistema-de-Gestion-de-Usuarios.git
   cd Sistema-de-Gestion-de-Usuarios
   ```
2. **Instala las dependencias:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Ejecuta la aplicación:**
   ```sh
   python src/main.py
   ```

---

## Descripción de Archivos Principales

| Archivo              | Descripción                                                                |
| -------------------- | -------------------------------------------------------------------------- |
| `main.py`            | Punto de entrada. Muestra el menú principal y gestiona el flujo de la app. |
| `db.py`              | Maneja la conexión y operaciones con la base de datos SQLite.              |
| `user_management.py` | Lógica de negocio para registro, login y menús de usuario/admin.           |
| `utils.py`           | Funciones auxiliares para validación y manejo seguro de contraseñas.       |

---

## Flujo de Uso

1. **Inicio:** Puedes iniciar sesión como usuario existente o registrarte.
2. **Roles:**
   - El usuario **admin** tiene acceso total (ver, crear, editar, eliminar usuarios).
   - Los usuarios normales pueden ver y editar solo su información.
3. **Seguridad:** El sistema limita a **5 intentos de inicio de sesión**; si se superan, hay que esperar 5 segundos.
4. **Sesión:** Al cerrar sesión, puedes ingresar con cualquier usuario o con el admin.
5. **Persistencia:** Todos los cambios se reflejan en la base de datos en tiempo real.

---

## Documentación de Módulos

### `utils.py`

Funciones auxiliares para la gestión de usuarios y contraseñas:

- **`hash_contrasena(contrasena)`**  
   Genera un hash seguro de la contraseña usando `bcrypt`.
- **`verificar_contrasena(contrasena, hash_almacenado)`**  
   Comprueba si una contraseña coincide con su hash almacenado.
- **`validar_usuario(usuario)`**  
   Verifica que el nombre de usuario tenga al menos 3 caracteres.
- **`validar_contrasena(contrasena)`**  
   Verifica que la contraseña tenga al menos 6 caracteres.
- **`imprimir_error(mensaje)`**  
   Muestra un mensaje de error en consola con formato destacado.
- **`imprimir_exito(mensaje)`**  
   Muestra un mensaje de éxito en consola con formato destacado.

---

### `db.py`

Módulo encargado de la interacción con la base de datos SQLite:

- **`obtener_conexion()`**  
   Retorna una conexión activa a la base de datos.
- **`inicializar_bd()`**  
   Crea la tabla de usuarios y el usuario administrador si no existen.
- **`obtener_usuario(usuario)`**  
   Recupera los datos de un usuario específico.
- **`agregar_usuario(usuario, contrasena, nombre, rol)`**  
   Añade un nuevo usuario a la base de datos.
- **`actualizar_usuario(usuario, nombre)`**  
   Modifica el nombre de un usuario existente.
- **`eliminar_usuario(usuario)`**  
   Elimina un usuario de la base de datos.
- **`listar_usuarios()`**  
   Devuelve una lista de todos los usuarios registrados.

---

### `user_management.py`

Contiene la lógica principal para la gestión de usuarios y sesiones:

- **`iniciar_sesion()`**  
   Gestiona el proceso de inicio de sesión, incluyendo el control de intentos y tiempos de espera.
- **`registrar_usuario()`**  
   Permite crear un nuevo usuario en el sistema.
- **`menu_usuario(usuario)`**  
   Muestra el menú adecuado según el rol del usuario (admin o normal).

---

### `main.py`

Archivo principal y punto de entrada de la aplicación:

- **Inicializa la base de datos** automáticamente al iniciar el programa.
- **Muestra el menú principal** con opciones para:
  - Iniciar sesión
  - Registrarse como nuevo usuario
  - Salir de la aplicación
- **Gestiona el flujo de navegación**: según el usuario autenticado, redirige al menú de administrador o usuario normal.
- **Controla el ciclo de vida** de la aplicación, asegurando que todas las operaciones sean seguras y persistentes.

---

## Notas

- **Usuario administrador por defecto:**
  - Usuario: `admin`
  - Contraseña: `admin123`
- Todos los datos se almacenan en el archivo `users.db` (SQLite).
- El sistema es fácilmente ampliable y puede integrarse con interfaces gráficas o web en el futuro.
- Las funciones de impresión pueden mejorarse usando la librería `rich` para una mejor experiencia visual.

---
