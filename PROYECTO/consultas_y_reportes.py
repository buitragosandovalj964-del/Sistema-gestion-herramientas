# -*- coding: utf-8 -*-
import json
from datetime import datetime
from colorama import Fore, Style, init
from logs import registrar_log

init(autoreset=True)

ARCHIVO_HERRAMIENTAS = "herramientas.json"
ARCHIVO_PRESTAMOS = "prestamos.json"
ARCHIVO_SOLICITUDES = "solicitudes.json"

# =====================================
# UTILIDADES VISUALES
# =====================================

def linea():
    print(Fore.CYAN + "═" * 60)

def titulo(texto):
    linea()
    print(Fore.YELLOW + Style.BRIGHT + f"   {texto}")
    linea()

def pausa():
    input(Fore.LIGHTBLACK_EX + "\nPresione ENTER para continuar...")

# =====================================
# CARGAR Y GUARDAR
# =====================================

def cargar_datos(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(archivo, datos):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        registrar_log(f"Error al guardar {archivo}: {e}", "ERROR")
        print(Fore.RED + f"Error al guardar: {e}")

# =====================================
# 1. HERRAMIENTAS CON STOCK BAJO
# =====================================

def stock_bajo():
    herramientas = cargar_datos(ARCHIVO_HERRAMIENTAS)

    titulo("HERRAMIENTAS CON STOCK BAJO (<3)")

    bajas = [h for h in herramientas if h.get("cantidad", 0) < 3]

    if not bajas:
        print(Fore.GREEN + "No hay herramientas con stock bajo.")
        pausa()
        return

    for h in bajas:
        print(Fore.WHITE + f"""
Nombre   : {h['nombre']}
Cantidad : {h['cantidad']}
Categoría: {h['categoria']}
-----------------------------------------
""")
    
    registrar_log(f"Consulta de stock bajo - {len(bajas)} herramientas encontradas", "INFO")
    pausa()

# =====================================
# 2. PRÉSTAMOS ACTIVOS
# =====================================

def prestamos_activos():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    titulo("PRÉSTAMOS ACTIVOS")

    activos = [p for p in prestamos if p.get("estado") == "Activo"]

    if not activos:
        print(Fore.YELLOW + "No hay préstamos activos.")
        pausa()
        return

    for p in activos:
        print(Fore.WHITE + f"""
ID          : {p['id_prestamo']}
Usuario     : {p['nombre_usuario']}
Herramienta : {p['herramienta']}
Cantidad    : {p['cantidad']}
Devolución  : {p['fecha_estimada_devolucion']}
-----------------------------------------
""")
    pausa()

# =====================================
# 3. PRÉSTAMOS VENCIDOS
# =====================================

def prestamos_vencidos():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)
    hoy = datetime.now().date()
    hubo_cambios = False

    titulo("PRÉSTAMOS VENCIDOS")

    vencidos = []

    for p in prestamos:
        if p.get("estado") == "Activo":
            fecha_texto = p.get("fecha_estimada_devolucion")

            if not fecha_texto:
                continue

            try:
                fecha_estimada = datetime.strptime(
                    fecha_texto, "%Y-%m-%d"
                ).date()
            except ValueError:
                continue

            if fecha_estimada < hoy:
                dias_vencido = (hoy - fecha_estimada).days
                p["estado"] = "Vencido"
                vencidos.append((p, dias_vencido))
                hubo_cambios = True

    if not vencidos:
        print(Fore.GREEN + "No hay préstamos vencidos.")
    else:
        for p, dias in vencidos:
            print(Fore.RED + f"""
ID          : {p['id_prestamo']}
Usuario     : {p['nombre_usuario']}
Herramienta : {p['herramienta']}
Vencido hace: {dias} día(s)
-----------------------------------------
""")
        
        registrar_log(f"Préstamos vencidos detectados: {len(vencidos)} préstamos actualizados a estado 'Vencido'", "WARNING")

    if hubo_cambios:
        guardar_datos(ARCHIVO_PRESTAMOS, prestamos)

    pausa()

# =====================================
# 4. HISTORIAL POR USUARIO
# =====================================

def historial_usuario():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    titulo("HISTORIAL POR USUARIO")

    nombre_usuario = input("Ingrese nombre del usuario: ").strip().lower()

    encontrados = [
        p for p in prestamos
        if p.get("nombre_usuario", "").lower() == nombre_usuario
    ]

    if not encontrados:
        print(Fore.YELLOW + "No tiene préstamos registrados.")
        pausa()
        return

    print(Fore.GREEN + f"\nSe encontraron {len(encontrados)} préstamos:\n")

    for p in encontrados:
        print(Fore.WHITE + f"""
ID          : {p['id_prestamo']}
Herramienta : {p['herramienta']}
Cantidad    : {p['cantidad']}
Estado      : {p['estado']}
Inicio      : {p['fecha_inicio']}
Devolución  : {p['fecha_estimada_devolucion']}
-----------------------------------------
""")

    pausa()

# =====================================
# 5. HERRAMIENTAS MÁS SOLICITADAS
# =====================================

def herramientas_mas_solicitadas():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    titulo("HERRAMIENTAS MÁS SOLICITADAS")

    contador = {}

    for p in prestamos:
        nombre = p.get("herramienta", "").lower()
        cantidad = p.get("cantidad", 0)

        if nombre:
            contador[nombre] = contador.get(nombre, 0) + cantidad

    if not contador:
        print(Fore.YELLOW + "No hay datos suficientes.")
        pausa()
        return

    ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    print(Fore.GREEN + f"\nTop {min(10, len(ordenadas))} herramientas más solicitadas:\n")

    for i, (nombre, total) in enumerate(ordenadas[:10], 1):
        print(Fore.WHITE + f"{i}. {nombre.title()}  ➤  Total solicitado: {total}")

    pausa()

# =====================================
# 6. USUARIOS MÁS ACTIVOS
# =====================================

def usuarios_mas_activos():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    titulo("USUARIOS MÁS ACTIVOS")

    contador = {}

    for p in prestamos:
        nombre = p.get("nombre_usuario", "").lower()
        cantidad = p.get("cantidad", 0)

        if nombre:
            contador[nombre] = contador.get(nombre, 0) + cantidad

    if not contador:
        print(Fore.YELLOW + "No hay datos suficientes.")
        pausa()
        return

    ordenados = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    print(Fore.GREEN + f"\nTop {min(10, len(ordenados))} usuarios más activos:\n")

    for i, (nombre, total) in enumerate(ordenados[:10], 1):
        print(Fore.WHITE + f"{i}. {nombre.title()}  ➤  Total solicitado: {total}")

    pausa()

# =====================================
# 7. SOLICITUDES PENDIENTES
# =====================================

def solicitudes_pendientes():
    solicitudes = cargar_datos(ARCHIVO_SOLICITUDES)

    titulo("SOLICITUDES PENDIENTES")

    pendientes = [s for s in solicitudes if s.get("estado") == "Pendiente"]

    if not pendientes:
        print(Fore.GREEN + "No hay solicitudes pendientes.")
        pausa()
        return

    print(Fore.YELLOW + f"\nHay {len(pendientes)} solicitud(es) pendiente(s):\n")

    for s in pendientes:
        print(Fore.WHITE + f"""
ID Solicitud : {s['id_solicitud']}
Usuario      : {s['nombre_usuario']}
Herramienta  : {s['herramienta']}
Cantidad     : {s['cantidad_solicitada']}
Fecha        : {s['fecha_solicitud']}
Estado       : {s['estado']}
-----------------------------------------
""")

    pausa()

# =====================================
# MENÚ
# =====================================

def menu_consultas():
    while True:
        titulo("CONSULTAS Y REPORTES")

        print(Fore.WHITE + " 1 ➤ Herramientas con stock bajo")
        print(Fore.WHITE + " 2 ➤ Préstamos activos")
        print(Fore.WHITE + " 3 ➤ Préstamos vencidos")
        print(Fore.WHITE + " 4 ➤ Historial por usuario")
        print(Fore.WHITE + " 5 ➤ Herramientas más solicitadas")
        print(Fore.WHITE + " 6 ➤ Usuarios más activos")
        print(Fore.WHITE + " 7 ➤ Solicitudes pendientes")
        print(Fore.RED   + " 8 ➤ Volver")

        linea()

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            stock_bajo()
        elif opcion == "2":
            prestamos_activos()
        elif opcion == "3":
            prestamos_vencidos()
        elif opcion == "4":
            historial_usuario()
        elif opcion == "5":
            herramientas_mas_solicitadas()
        elif opcion == "6":
            usuarios_mas_activos()
        elif opcion == "7":
            solicitudes_pendientes()
        elif opcion == "8":
            break
        else:
            print(Fore.RED + "Opción inválida.")
            pausa()

