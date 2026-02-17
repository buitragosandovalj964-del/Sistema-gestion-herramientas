# -*- coding: utf-8 -*-
import json
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
    print(Fore.CYAN + "=" * 60)

def titulo(texto):
    linea()
    print(Fore.YELLOW + Style.BRIGHT + texto)
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
        registrar_log("Error al guardar " + archivo + ": " + str(e), "ERROR")
        print(Fore.RED + "Error al guardar: " + str(e))

# =====================================
# 1. HERRAMIENTAS CON STOCK BAJO
# =====================================

def stock_bajo():
    herramientas = cargar_datos(ARCHIVO_HERRAMIENTAS)

    titulo("HERRAMIENTAS CON STOCK BAJO (<3)")

    bajas = []
    for h in herramientas:
        if h.get("cantidad", 0) < 3:
            bajas.append(h)

    if not bajas:
        print(Fore.GREEN + "No hay herramientas con stock bajo.")
        pausa()
        return

    for h in bajas:
        print(Fore.WHITE + "\nNombre   : " + h['nombre'])
        print("Cantidad : " + str(h['cantidad']))
        print("Categoría: " + h['categoria'])
        print("-" * 41)
    
    registrar_log("Consulta de stock bajo - " + str(len(bajas)) + " herramientas encontradas", "INFO")
    pausa()

# =====================================
# 2. PRÉSTAMOS ACTIVOS
# =====================================

def prestamos_activos():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    titulo("PRESTAMOS ACTIVOS")

    activos = []
    for p in prestamos:
        if p.get("estado") == "Activo":
            activos.append(p)

    if not activos:
        print(Fore.YELLOW + "No hay préstamos activos.")
        pausa()
        return

    for p in activos:
        print(Fore.WHITE + "\nID          : " + str(p['id_prestamo']))
        print("Usuario     : " + p['nombre_usuario'])
        print("Herramienta : " + p['herramienta'])
        print("Cantidad    : " + str(p['cantidad']))
        print("Devolución  : " + p['fecha_estimada_devolucion'])
        print("-" * 41)

    pausa()

# =====================================
# 3. PRÉSTAMOS VENCIDOS
# =====================================

def prestamos_vencidos():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    titulo("PRESTAMOS (Verificar vencidos manualmente)")

    print(Fore.YELLOW + "\nNOTA: Compare las fechas con la fecha actual")
    print("para identificar cuáles están vencidos.\n")

    activos = []
    for p in prestamos:
        if p.get("estado") == "Activo":
            activos.append(p)

    if not activos:
        print(Fore.GREEN + "No hay préstamos activos.")
        pausa()
        return

    for p in activos:
        print(Fore.WHITE + "\nID          : " + str(p['id_prestamo']))
        print("Usuario     : " + p['nombre_usuario'])
        print("Herramienta : " + p['herramienta'])
        print("Fecha devolución: " + p['fecha_estimada_devolucion'])
        print("Estado      : " + p['estado'])
        print("-" * 41)

    pausa()

# =====================================
# 4. HISTORIAL POR USUARIO
# =====================================

def historial_usuario():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    titulo("HISTORIAL POR USUARIO")

    nombre_usuario = input("Ingrese nombre del usuario: ").strip().lower()

    encontrados = []
    for p in prestamos:
        if p.get("nombre_usuario", "").lower() == nombre_usuario:
            encontrados.append(p)

    if not encontrados:
        print(Fore.YELLOW + "No tiene préstamos registrados.")
        pausa()
        return

    print(Fore.GREEN + "\nSe encontraron " + str(len(encontrados)) + " préstamos:\n")

    for p in encontrados:
        print(Fore.WHITE + "\nID          : " + str(p['id_prestamo']))
        print("Herramienta : " + p['herramienta'])
        print("Cantidad    : " + str(p['cantidad']))
        print("Estado      : " + p['estado'])
        print("Inicio      : " + p['fecha_inicio'])
        print("Devolución  : " + p['fecha_estimada_devolucion'])
        print("-" * 41)

    pausa()

# =====================================
# 5. HERRAMIENTAS MÁS SOLICITADAS
# =====================================

def herramientas_mas_solicitadas():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    titulo("HERRAMIENTAS MAS SOLICITADAS")

    contador = {}

    for p in prestamos:
        nombre = p.get("herramienta", "").lower()
        cantidad = p.get("cantidad", 0)

        if nombre:
            if nombre in contador:
                contador[nombre] += cantidad
            else:
                contador[nombre] = cantidad

    if not contador:
        print(Fore.YELLOW + "No hay datos suficientes.")
        pausa()
        return

    # Ordenar de mayor a menor
    ordenadas = []
    for nombre, total in contador.items():
        ordenadas.append((nombre, total))
    
    # Ordenar manualmente (bubble sort simple)
    for i in range(len(ordenadas)):
        for j in range(i + 1, len(ordenadas)):
            if ordenadas[j][1] > ordenadas[i][1]:
                ordenadas[i], ordenadas[j] = ordenadas[j], ordenadas[i]

    # Mostrar top 10
    limite = min(10, len(ordenadas))
    print(Fore.GREEN + "\nTop " + str(limite) + " herramientas más solicitadas:\n")

    for i in range(limite):
        nombre, total = ordenadas[i]
        print(Fore.WHITE + str(i + 1) + ". " + nombre.title() + " - Total solicitado: " + str(total))

    pausa()

# =====================================
# 6. USUARIOS MÁS ACTIVOS
# =====================================

def usuarios_mas_activos():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    titulo("USUARIOS MAS ACTIVOS")

    contador = {}

    for p in prestamos:
        nombre = p.get("nombre_usuario", "").lower()
        cantidad = p.get("cantidad", 0)

        if nombre:
            if nombre in contador:
                contador[nombre] += cantidad
            else:
                contador[nombre] = cantidad

    if not contador:
        print(Fore.YELLOW + "No hay datos suficientes.")
        pausa()
        return

    # Ordenar de mayor a menor
    ordenados = []
    for nombre, total in contador.items():
        ordenados.append((nombre, total))
    
    # Ordenar manualmente
    for i in range(len(ordenados)):
        for j in range(i + 1, len(ordenados)):
            if ordenados[j][1] > ordenados[i][1]:
                ordenados[i], ordenados[j] = ordenados[j], ordenados[i]

    # Mostrar top 10
    limite = min(10, len(ordenados))
    print(Fore.GREEN + "\nTop " + str(limite) + " usuarios más activos:\n")

    for i in range(limite):
        nombre, total = ordenados[i]
        print(Fore.WHITE + str(i + 1) + ". " + nombre.title() + " - Total solicitado: " + str(total))

    pausa()

# =====================================
# 7. SOLICITUDES PENDIENTES
# =====================================

def solicitudes_pendientes():
    solicitudes = cargar_datos(ARCHIVO_SOLICITUDES)

    titulo("SOLICITUDES PENDIENTES")

    pendientes = []
    for s in solicitudes:
        if s.get("estado") == "Pendiente":
            pendientes.append(s)

    if not pendientes:
        print(Fore.GREEN + "No hay solicitudes pendientes.")
        pausa()
        return

    print(Fore.YELLOW + "\nHay " + str(len(pendientes)) + " solicitud(es) pendiente(s):\n")

    for s in pendientes:
        print(Fore.WHITE + "\nID Solicitud : " + str(s['id_solicitud']))
        print("Usuario      : " + s['nombre_usuario'])
        print("Herramienta  : " + s['herramienta'])
        print("Cantidad     : " + str(s['cantidad_solicitada']))
        print("Fecha        : " + s['fecha_solicitud'])
        print("Estado       : " + s['estado'])
        print("-" * 41)

    pausa()

# =====================================
# MENÚ
# =====================================

def menu_consultas():
    while True:
        titulo("CONSULTAS Y REPORTES")

        print(Fore.WHITE + "[1] Herramientas con stock bajo")
        print(Fore.WHITE + "[2] Préstamos activos")
        print(Fore.WHITE + "[3] Préstamos vencidos")
        print(Fore.WHITE + "[4] Historial por usuario")
        print(Fore.WHITE + "[5] Herramientas más solicitadas")
        print(Fore.WHITE + "[6] Usuarios más activos")
        print(Fore.WHITE + "[7] Solicitudes pendientes")
        print(Fore.RED   + "[8] Volver")

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