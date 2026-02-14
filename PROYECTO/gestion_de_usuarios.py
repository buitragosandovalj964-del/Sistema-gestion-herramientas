# -*- coding: utf-8 -*-
import json
from colorama import Fore, Style, init
from logs import registrar_log

init(autoreset=True)

ARCHIVO_USUARIOS = "usuarios.json"
ARCHIVO_PRESTAMOS = "prestamos.json"

TIPOS_VALIDOS = ["residente", "administrador"]

# ==========================================
# UTILIDADES VISUALES
# ==========================================

def linea():
    print(Fore.CYAN + "═" * 60)

def titulo(texto):
    linea()
    print(Fore.YELLOW + Style.BRIGHT + f"   {texto}")
    linea()

def pausa():
    input(Fore.LIGHTBLACK_EX + "\nPresione ENTER para continuar...")

# ==========================================
# CARGAR Y GUARDAR
# ==========================================

def cargar_usuarios():
    try:
        with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        registrar_log(f"Archivo {ARCHIVO_USUARIOS} no encontrado, creando nuevo", "WARNING")
        return []
    except json.JSONDecodeError as e:
        registrar_log(f"Error al decodificar {ARCHIVO_USUARIOS}: {e}", "ERROR")
        return []

def guardar_usuarios(usuarios):
    try:
        with open(ARCHIVO_USUARIOS, "w", encoding="utf-8") as archivo:
            json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        registrar_log(f"Error al guardar usuarios: {e}", "ERROR")
        print(Fore.RED + f"Error al guardar: {e}")

def cargar_prestamos():
    try:
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# ==========================================
# AGREGAR
# ==========================================

def agregar_usuario():
    usuarios = cargar_usuarios()

    titulo("AGREGAR USUARIO")

    id_u = input("ID: ").strip()

    if not id_u:
        print(Fore.RED + "ID inválido.")
        registrar_log("Intento de agregar usuario con ID vacío", "WARNING")
        pausa()
        return

    if any(str(u["id"]) == id_u for u in usuarios):
        print(Fore.RED + "Ya existe un usuario con ese ID.")
        registrar_log(f"Intento de agregar usuario con ID duplicado: {id_u}", "WARNING")
        pausa()
        return

    nombres = input("Nombres: ").strip().title()
    apellidos = input("Apellidos: ").strip().title()
    telefono = input("Teléfono: ").strip()
    direccion = input("Dirección: ").strip()
    tipo = input("Tipo (residente / administrador): ").strip().lower()

    if not nombres or not apellidos:
        print(Fore.RED + "Nombre y apellido son obligatorios.")
        registrar_log("Intento de agregar usuario sin nombre o apellido", "WARNING")
        pausa()
        return

    if tipo not in TIPOS_VALIDOS:
        print(Fore.RED + "Tipo inválido.")
        registrar_log(f"Tipo de usuario inválido: {tipo}", "WARNING")
        pausa()
        return

    usuario = {
        "id": id_u,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo
    }

    usuarios.append(usuario)
    guardar_usuarios(usuarios)

    print(Fore.GREEN + "Usuario agregado correctamente.")
    registrar_log(f"Usuario agregado: {nombres} {apellidos} (ID: {id_u}, Tipo: {tipo})", "INFO")
    pausa()

# ==========================================
# LISTAR
# ==========================================

def listar_usuarios():
    usuarios = cargar_usuarios()

    titulo("LISTA DE USUARIOS")

    if not usuarios:
        print(Fore.YELLOW + "No hay usuarios registrados.")
        pausa()
        return

    for u in usuarios:
        # Color según tipo
        if u['tipo'] == 'administrador':
            color_tipo = Fore.RED
        else:
            color_tipo = Fore.GREEN

        print(Fore.WHITE + f"""
ID        : {u['id']}
Nombre    : {u['nombres']} {u['apellidos']}
Teléfono  : {u['telefono']}
Dirección : {u['direccion']}
Tipo      : {color_tipo}{u['tipo']}{Fore.WHITE}
-----------------------------------------
""")
    pausa()

# ==========================================
# BUSCAR
# ==========================================

def buscar_usuario():
    usuarios = cargar_usuarios()

    titulo("BUSCAR USUARIO")

    id_buscar = input("Ingrese ID: ").strip()

    for u in usuarios:
        if str(u["id"]) == id_buscar:
            print(Fore.GREEN + "\nUsuario encontrado:")
            print(Fore.WHITE + f"""
ID        : {u['id']}
Nombre    : {u['nombres']} {u['apellidos']}
Teléfono  : {u['telefono']}
Dirección : {u['direccion']}
Tipo      : {u['tipo']}
""")
            pausa()
            return

    print(Fore.RED + "Usuario no encontrado.")
    registrar_log(f"Búsqueda de usuario sin resultados: {id_buscar}", "INFO")
    pausa()

# ==========================================
# ACTUALIZAR
# ==========================================

def actualizar_usuario():
    usuarios = cargar_usuarios()

    titulo("ACTUALIZAR USUARIO")

    id_buscar = input("Ingrese ID: ").strip()

    for u in usuarios:
        if str(u["id"]) == id_buscar:

            print(Fore.LIGHTBLACK_EX + "Deje en blanco si no desea cambiar.")

            nuevo_nombre = input(f"Nombres ({u['nombres']}): ").strip()
            nuevo_apellido = input(f"Apellidos ({u['apellidos']}): ").strip()
            nuevo_telefono = input(f"Teléfono ({u['telefono']}): ").strip()
            nueva_direccion = input(f"Dirección ({u['direccion']}): ").strip()
            nuevo_tipo = input(f"Tipo ({u['tipo']}): ").strip().lower()

            cambios = []

            if nuevo_nombre:
                u["nombres"] = nuevo_nombre.title()
                cambios.append(f"nombres: {nuevo_nombre}")
            if nuevo_apellido:
                u["apellidos"] = nuevo_apellido.title()
                cambios.append(f"apellidos: {nuevo_apellido}")
            if nuevo_telefono:
                u["telefono"] = nuevo_telefono
                cambios.append(f"teléfono: {nuevo_telefono}")
            if nueva_direccion:
                u["direccion"] = nueva_direccion
                cambios.append(f"dirección: {nueva_direccion}")
            if nuevo_tipo:
                if nuevo_tipo in TIPOS_VALIDOS:
                    u["tipo"] = nuevo_tipo
                    cambios.append(f"tipo: {nuevo_tipo}")
                else:
                    print(Fore.RED + "Tipo inválido.")

            guardar_usuarios(usuarios)
            print(Fore.GREEN + "Usuario actualizado correctamente.")
            
            if cambios:
                registrar_log(f"Usuario {id_buscar} actualizado: {', '.join(cambios)}", "INFO")
            
            pausa()
            return

    print(Fore.RED + "Usuario no encontrado.")
    registrar_log(f"Intento de actualizar usuario inexistente: {id_buscar}", "WARNING")
    pausa()

# ==========================================
# ELIMINAR
# ==========================================

def eliminar_usuario():
    usuarios = cargar_usuarios()
    prestamos = cargar_prestamos()

    titulo("ELIMINAR USUARIO")

    id_buscar = input("Ingrese ID: ").strip()

    for u in usuarios:
        if str(u["id"]) == id_buscar:

            # 🔒 BLOQUEAR SI TIENE PRÉSTAMOS ACTIVOS
            tiene_prestamo = any(
                str(p["id_usuario"]) == id_buscar and p["estado"] == "Activo"
                for p in prestamos
            )

            if tiene_prestamo:
                print(Fore.RED + "No se puede eliminar. Tiene préstamos activos.")
                registrar_log(
                    f"Intento de eliminar usuario con préstamos activos: "
                    f"{u['nombres']} {u['apellidos']} (ID: {id_buscar})",
                    "WARNING"
                )
                pausa()
                return

            confirmacion = input(Fore.RED + "¿Está seguro? (s/n): ").lower()

            if confirmacion == "s":
                nombre_eliminado = f"{u['nombres']} {u['apellidos']}"
                usuarios.remove(u)
                guardar_usuarios(usuarios)
                print(Fore.GREEN + "Usuario eliminado correctamente.")
                registrar_log(f"Usuario eliminado: {nombre_eliminado} (ID: {id_buscar})", "INFO")
            else:
                print(Fore.YELLOW + "Operación cancelada.")

            pausa()
            return

    print(Fore.RED + "Usuario no encontrado.")
    registrar_log(f"Intento de eliminar usuario inexistente: {id_buscar}", "WARNING")
    pausa()

# ==========================================
# MENÚ
# ==========================================

def menu_usuarios():
    while True:
        titulo("GESTIÓN DE USUARIOS")

        print(Fore.WHITE + " 1 ➤ Agregar usuario")
        print(Fore.WHITE + " 2 ➤ Listar usuarios")
        print(Fore.WHITE + " 3 ➤ Buscar usuario")
        print(Fore.WHITE + " 4 ➤ Actualizar usuario")
        print(Fore.WHITE + " 5 ➤ Eliminar usuario")
        print(Fore.RED   + " 6 ➤ Volver")

        linea()

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            buscar_usuario()
        elif opcion == "4":
            actualizar_usuario()
        elif opcion == "5":
            eliminar_usuario()
        elif opcion == "6":
            break
        else:
            print(Fore.RED + "Opción inválida.")
            pausa()

