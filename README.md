# Sistema de Gestión de Usuarios

Bienvenido al **Sistema de Gestión de Usuarios**: una aplicación de consola moderna y fácil de usar para administrar usuarios, con control de sesiones, seguridad y una interfaz enriquecida gracias a la librería [`rich`](https://github.com/Textualize/rich).

---

## Características principales

- **Registro de usuarios:** El administrador puede crear usuarios o los usuarios pueden registrarse por sí mismos.
- **Inicio de sesión seguro:** Acceso para usuarios normales y administrador con control de intentos (5 intentos, luego espera de 5 segundos).
- **Gestión completa:** El administrador puede ver, crear, actualizar y eliminar cualquier usuario.
- **Privacidad:** Los usuarios normales solo pueden ver y editar su propia información.
- **Sesiones activas:** Cambia de usuario fácilmente cerrando sesión.
- **Actualización en tiempo real:** El administrador ve los cambios de usuarios al instante.
- **Persistencia:** Todos los datos se guardan en una base de datos SQLite.

---

## Estructura del proyecto

```
Project
├── src
│   ├── main.py              # Inicio de la aplicación
│   ├── db.py                # Funciones para la base de datos SQLite
│   ├── user_management.py   # Lógica para gestionar usuarios y sesiones
│   └── utils.py             # Utilidades para validación y contraseñas
├── requirements.txt         # Lista de dependencias
├── README.md                # Este archivo
└── Documentacion.md         # Documentación completa del proyecto
```

---

## Instalación rápida

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/EM-DEV03/Sistema-de-Gesti-n-de-Usuarios.git
   cd Sistema-de-Gesti-n-de-Usuarios
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación:**
   ```bash
   python src/main.py
   ```

4. **Accede como administrador** (`admin` / `admin123`) o crea un usuario nuevo.

---

## Requisitos

- Python 3.x
- SQLite (incluido en Python)
- Librerías: [`rich`](https://github.com/Textualize/rich), [`bcrypt`](https://pypi.org/project/bcrypt/)

---

## ¡Contribuye!

¿Tienes ideas o mejoras? ¡Eres bienvenido! Abre un issue o envía un pull request.

---

>  **¿Quieres más detalles?**  
> Consulta la [Documentación completa del proyecto](Documentacion.md).

---
