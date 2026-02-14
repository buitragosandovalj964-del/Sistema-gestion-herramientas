# -*- coding: utf-8 -*-
from colorama import Fore, Style, init
from gestion_de_usuarios import menu_usuarios
from agregar_herramienta import menu_herramientas, listar_herramientas
from gestion_de_prestamos import menu_prestamos, reporte_prestamos_activos, aprobar_solicitud, crear_solicitud_usuario
from consultas_y_reportes import menu_consultas
from logs import registrar_log
from datetime import datetime
import time

init(autoreset=True)

CLAVE_ADMIN = "0611JB"   # 🔐 puedes cambiarla

# =========================================
# DISEÑO VISUAL
# =========================================

def linea():
    print(Fore.CYAN + "═" * 70)

def encabezado():
    fecha = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")

    print("\n")
    print(Fore.CYAN + "╔" + "═" * 68 + "╗")
    print(Fore.CYAN + "║" + " " * 68 + "║")
    print(Fore.YELLOW + Style.BRIGHT +
          "║" + " SISTEMA INTEGRAL DE GESTIÓN DE HERRAMIENTAS ".center(68) + "║")
    print(Fore.LIGHTBLACK_EX +
          "║" + f" Fecha: {fecha}".ljust(68) + "║")
    print(Fore.CYAN + "║" + " " * 68 + "║")
    print(Fore.CYAN + "╚" + "═" * 68 + "╝")

# =========================================
# LOGIN ADMIN
# =========================================

def login_admin():
    encabezado()
    print(Fore.GREEN + Style.BRIGHT + "\n        ║ ACCESO ADMINISTRADOR ║\n")

    clave = input(Fore.CYAN + "   ➤ Ingrese contraseña: ")

    if clave == CLAVE_ADMIN:
        print(Fore.GREEN + "\n   ✔ Acceso concedido.")
        registrar_log("Acceso de administrador exitoso", "INFO")
        time.sleep(1)
        menu_admin()
    else:
        print(Fore.RED + "\n   ✖ Contraseña incorrecta.")
        registrar_log("Intento de acceso de administrador fallido", "WARNING")
        time.sleep(1)

# =========================================
# PANEL ADMINISTRADOR
# =========================================

def menu_admin():
    while True:
        encabezado()

        print(Fore.GREEN + Style.BRIGHT + "\n        ║ PANEL ADMINISTRADOR ║\n")

        print(Fore.WHITE + "   ▸ [1] Gestión de Usuarios")
        print(Fore.WHITE + "   ▸ [2] Gestión de Herramientas")
        print(Fore.WHITE + "   ▸ [3] Gestión de Préstamos")
        print(Fore.WHITE + "   ▸ [4] Aprobar Solicitudes")
        print(Fore.WHITE + "   ▸ [5] Consultas y Reportes")
        print(Fore.WHITE + "   ▸ [6] Ver préstamos activos")
        print(Fore.RED +   "   ▸ [7] Cerrar sesión")

        linea()

        opcion = input(Fore.CYAN + "   ➤ Seleccione opción: ")

        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_herramientas()
        elif opcion == "3":
            menu_prestamos()
        elif opcion == "4":
            aprobar_solicitud()
        elif opcion == "5":
            menu_consultas()
        elif opcion == "6":
            reporte_prestamos_activos()
        elif opcion == "7":
            print(Fore.YELLOW + "\n   Cerrando sesión...")
            registrar_log("Administrador cerró sesión", "INFO")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "   Opción inválida.")
            time.sleep(1)

# =========================================
# PANEL USUARIO
# =========================================

def menu_usuario():
    while True:
        encabezado()

        print(Fore.BLUE + Style.BRIGHT + "\n        ║ PANEL USUARIO ║\n")

        print(Fore.WHITE + "   ▸ [1] Ver herramientas disponibles")
        print(Fore.WHITE + "   ▸ [2] Ver préstamos activos")
        print(Fore.WHITE + "   ▸ [3] Crear solicitud de herramienta")
        print(Fore.WHITE + "   ▸ [4] Consultas y reportes")
        print(Fore.RED +   "   ▸ [5] Cerrar sesión")

        linea()

        opcion = input(Fore.CYAN + "   ➤ Seleccione opción: ")

        if opcion == "1":
            listar_herramientas()
        elif opcion == "2":
            reporte_prestamos_activos()
        elif opcion == "3":
            crear_solicitud_usuario()
        elif opcion == "4":
            menu_consultas()
        elif opcion == "5":
            print(Fore.YELLOW + "\n   Cerrando sesión...")
            registrar_log("Usuario cerró sesión", "INFO")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "   Opción inválida.")
            time.sleep(1)

# =========================================
# MENÚ PRINCIPAL
# =========================================

def menu_principal():
    registrar_log("Sistema iniciado", "INFO")
    
    while True:
        encabezado()

        print(Fore.MAGENTA + Style.BRIGHT + "\n        ║ SELECCIONE TIPO DE ACCESO ║\n")

        print(Fore.WHITE + "   ▸ [1] Administrador")
        print(Fore.WHITE + "   ▸ [2] Usuario")
        print(Fore.RED +   "   ▸ [3] Salir del sistema")

        linea()

        opcion = input(Fore.CYAN + "   ➤ Ingrese su opción: ")

        if opcion == "1":
            login_admin()
        elif opcion == "2":
            menu_usuario()
        elif opcion == "3":
            print(Fore.YELLOW + "\n   Cerrando sistema...")
            registrar_log("Sistema cerrado", "INFO")
            time.sleep(1)
            print(Fore.GREEN + "   Hasta pronto.\n")
            break
        else:
            print(Fore.RED + "   Opción inválida.")
            time.sleep(1)

# =========================================

if __name__ == "__main__":
    menu_principal()
