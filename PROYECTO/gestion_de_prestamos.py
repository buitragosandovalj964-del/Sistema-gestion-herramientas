import json
from datetime import datetime, timedelta
from gestion_de_usuarios import cargar_usuarios
from colorama import Fore, Style, init
from logs import registrar_log

init(autoreset=True)

ARCHIVO_PRESTAMOS = "prestamos.json"
ARCHIVO_HERRAMIENTAS = "herramientas.json"
ARCHIVO_SOLICITUDES = "solicitudes.json"

# ==========================================
# UTILIDADES
# ==========================================

def linea():
    print(Fore.CYAN + "═" * 55)

def pausa():
    input(Fore.LIGHTBLACK_EX + "\nPresione ENTER para continuar...")

def cargar_datos(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        registrar_log(f"Archivo {archivo} no encontrado, creando nuevo", "WARNING")
        return []
    except json.JSONDecodeError as e:
        registrar_log(f"Error al decodificar {archivo}: {e}", "ERROR")
        return []

def guardar_datos(archivo, datos):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        registrar_log(f"Error al guardar {archivo}: {e}", "ERROR")
        print(Fore.RED + f"Error al guardar: {e}")

# ==========================================
# GENERADORES DE ID
# ==========================================

def generar_id_prestamo(prestamos):
    if not prestamos:
        return 1
    return max(p["id_prestamo"] for p in prestamos) + 1

def generar_id_solicitud(solicitudes):
    if not solicitudes:
        return 1
    return max(s["id_solicitud"] for s in solicitudes) + 1

# ==========================================
# REGISTRAR PRÉSTAMO
# ==========================================

def registrar_prestamo():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)
    usuarios = cargar_usuarios()
    herramientas = cargar_datos(ARCHIVO_HERRAMIENTAS)
    solicitudes = cargar_datos(ARCHIVO_SOLICITUDES)

    linea()
    print(Fore.YELLOW + Style.BRIGHT + "        REGISTRAR PRÉSTAMO")
    linea()

    id_usuario = input("Ingrese ID del usuario: ").strip()
    usuario = next((u for u in usuarios if str(u["id"]) == id_usuario), None)

    if not usuario:
        print(Fore.RED + "Usuario no registrado.")
        registrar_log(f"Intento de préstamo con usuario inexistente: {id_usuario}", "WARNING")
        pausa()
        return

    id_herramienta = input("Ingrese ID de herramienta: ").strip()
    herramienta = next((h for h in herramientas if str(h["id"]) == id_herramienta), None)

    if not herramienta:
        print(Fore.RED + "Herramienta no encontrada.")
        registrar_log(f"Intento de préstamo con herramienta inexistente: {id_herramienta}", "WARNING")
        pausa()
        return

    # ✅ VALIDAR ESTADO DE LA HERRAMIENTA
    if herramienta["estado"] != "activa":
        print(Fore.RED + f"\nLa herramienta no está disponible.")
        print(Fore.YELLOW + f"Estado actual: {herramienta['estado']}")
        registrar_log(
            f"Intento de préstamo de herramienta en estado '{herramienta['estado']}': "
            f"{herramienta['nombre']} (ID: {id_herramienta})",
            "WARNING"
        )
        pausa()
        return

    try:
        cantidad = int(input("Cantidad a prestar: "))
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Cantidad inválida.")
        registrar_log("Cantidad inválida al registrar préstamo", "WARNING")
        pausa()
        return

    # 🔴 SI NO HAY STOCK → CREAR SOLICITUD
    if herramienta["cantidad"] < cantidad:

        nueva_solicitud = {
            "id_solicitud": generar_id_solicitud(solicitudes),
            "id_usuario": id_usuario,
            "nombre_usuario": usuario["nombres"],
            "id_herramienta": id_herramienta,
            "herramienta": herramienta["nombre"],
            "cantidad_solicitada": cantidad,
            "fecha_solicitud": datetime.now().strftime("%Y-%m-%d"),
            "estado": "Pendiente"
        }

        solicitudes.append(nueva_solicitud)
        guardar_datos(ARCHIVO_SOLICITUDES, solicitudes)

        print(Fore.YELLOW + "\nNo hay stock suficiente.")
        print(Fore.YELLOW + f"Disponible: {herramienta['cantidad']}, Solicitado: {cantidad}")
        print(Fore.GREEN + "Se ha generado una solicitud pendiente.")
        
        registrar_log(
            f"Solicitud creada por falta de stock - Usuario: {usuario['nombres']}, "
            f"Herramienta: {herramienta['nombre']}, Cantidad: {cantidad}, "
            f"Disponible: {herramienta['cantidad']}",
            "INFO"
        )
        
        pausa()
        return

    observaciones = input("Observaciones: ")

    fecha_inicio = datetime.now()
    fecha_devolucion = fecha_inicio + timedelta(days=7)

    nuevo_prestamo = {
        "id_prestamo": generar_id_prestamo(prestamos),
        "id_usuario": id_usuario,
        "nombre_usuario": usuario["nombres"],
        "id_herramienta": id_herramienta,
        "herramienta": herramienta["nombre"],
        "cantidad": cantidad,
        "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d"),
        "fecha_estimada_devolucion": fecha_devolucion.strftime("%Y-%m-%d"),
        "estado": "Activo",
        "observaciones": observaciones
    }

    prestamos.append(nuevo_prestamo)
    herramienta["cantidad"] -= cantidad

    guardar_datos(ARCHIVO_PRESTAMOS, prestamos)
    guardar_datos(ARCHIVO_HERRAMIENTAS, herramientas)

    print(Fore.GREEN + "\nPréstamo registrado correctamente.")
    registrar_log(
        f"Préstamo registrado - Usuario: {usuario['nombres']}, "
        f"Herramienta: {herramienta['nombre']}, Cantidad: {cantidad}",
        "INFO"
    )
    pausa()

# ==========================================
# DEVOLVER HERRAMIENTA
# ==========================================

def devolver_herramienta():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)
    herramientas = cargar_datos(ARCHIVO_HERRAMIENTAS)

    linea()
    print(Fore.YELLOW + Style.BRIGHT + "        DEVOLVER HERRAMIENTA")
    linea()

    id_prestamo = input("Ingrese ID del préstamo: ").strip()

    prestamo = next(
        (p for p in prestamos
         if str(p["id_prestamo"]) == id_prestamo and p["estado"] == "Activo"),
        None
    )

    if not prestamo:
        print(Fore.RED + "No existe préstamo activo con ese ID.")
        registrar_log(f"Intento de devolución con préstamo inexistente o inactivo: {id_prestamo}", "WARNING")
        pausa()
        return

    herramienta = next(
        (h for h in herramientas
         if str(h["id"]) == str(prestamo["id_herramienta"])),
        None
    )

    if herramienta:
        herramienta["cantidad"] += prestamo["cantidad"]

    prestamo["estado"] = "Devuelto"
    prestamo["fecha_devolucion_real"] = datetime.now().strftime("%Y-%m-%d")

    guardar_datos(ARCHIVO_PRESTAMOS, prestamos)
    guardar_datos(ARCHIVO_HERRAMIENTAS, herramientas)

    print(Fore.GREEN + "Préstamo finalizado correctamente.")
    registrar_log(
        f"Devolución registrada - Préstamo ID: {id_prestamo}, "
        f"Herramienta: {prestamo['herramienta']}, Cantidad: {prestamo['cantidad']}",
        "INFO"
    )
    pausa()

# ==========================================
# APROBAR SOLICITUD
# ==========================================

def aprobar_solicitud():
    solicitudes = cargar_datos(ARCHIVO_SOLICITUDES)
    herramientas = cargar_datos(ARCHIVO_HERRAMIENTAS)
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    linea()
    print(Fore.YELLOW + Style.BRIGHT + "        APROBAR SOLICITUDES")
    linea()

    pendientes = [s for s in solicitudes if s["estado"] == "Pendiente"]

    if not pendientes:
        print(Fore.GREEN + "No hay solicitudes pendientes.")
        pausa()
        return

    # Mostrar solicitudes pendientes
    print(Fore.WHITE + "\nSOLICITUDES PENDIENTES:\n")
    for s in pendientes:
        print(f"""
ID Solicitud : {s['id_solicitud']}
Usuario      : {s['nombre_usuario']}
Herramienta  : {s['herramienta']}
Cantidad     : {s['cantidad_solicitada']}
Fecha        : {s['fecha_solicitud']}
-----------------------------------------------
""")

    # Seleccionar solicitud
    id_solicitud = input("\nIngrese ID de solicitud a revisar (0 para cancelar): ").strip()

    if id_solicitud == "0":
        return

    solicitud = next(
        (s for s in solicitudes if str(s["id_solicitud"]) == id_solicitud and s["estado"] == "Pendiente"),
        None
    )

    if not solicitud:
        print(Fore.RED + "Solicitud no encontrada o ya procesada.")
        pausa()
        return

    # Verificar disponibilidad actual
    herramienta = next(
        (h for h in herramientas if str(h["id"]) == str(solicitud["id_herramienta"])),
        None
    )

    if not herramienta:
        print(Fore.RED + "Herramienta no encontrada.")
        solicitud["estado"] = "Rechazada - Herramienta no existe"
        guardar_datos(ARCHIVO_SOLICITUDES, solicitudes)
        registrar_log(f"Solicitud rechazada - herramienta inexistente: {solicitud['id_solicitud']}", "WARNING")
        pausa()
        return

    print(f"\nStock actual: {herramienta['cantidad']}")
    print(f"Cantidad solicitada: {solicitud['cantidad_solicitada']}")
    print(f"Estado herramienta: {herramienta['estado']}")

    # Decisión
    decision = input(Fore.CYAN + "\n¿Aprobar solicitud? (s/n): ").lower()

    if decision == "s":
        if herramienta["estado"] != "activa":
            print(Fore.RED + f"\nNo se puede aprobar. La herramienta está '{herramienta['estado']}'")
            solicitud["estado"] = "Rechazada - Herramienta no disponible"
            guardar_datos(ARCHIVO_SOLICITUDES, solicitudes)
            registrar_log(
                f"Solicitud rechazada - herramienta en estado '{herramienta['estado']}': {solicitud['id_solicitud']}",
                "INFO"
            )
            pausa()
            return

        if herramienta["cantidad"] >= solicitud["cantidad_solicitada"]:
            # Crear préstamo
            fecha_inicio = datetime.now()
            fecha_devolucion = fecha_inicio + timedelta(days=7)

            nuevo_prestamo = {
                "id_prestamo": generar_id_prestamo(prestamos),
                "id_usuario": solicitud["id_usuario"],
                "nombre_usuario": solicitud["nombre_usuario"],
                "id_herramienta": solicitud["id_herramienta"],
                "herramienta": solicitud["herramienta"],
                "cantidad": solicitud["cantidad_solicitada"],
                "fecha_inicio": fecha_inicio.strftime("%Y-%m-%d"),
                "fecha_estimada_devolucion": fecha_devolucion.strftime("%Y-%m-%d"),
                "estado": "Activo",
                "observaciones": f"Aprobado desde solicitud {solicitud['id_solicitud']}"
            }

            prestamos.append(nuevo_prestamo)
            herramienta["cantidad"] -= solicitud["cantidad_solicitada"]
            solicitud["estado"] = "Aprobada"

            guardar_datos(ARCHIVO_PRESTAMOS, prestamos)
            guardar_datos(ARCHIVO_HERRAMIENTAS, herramientas)
            guardar_datos(ARCHIVO_SOLICITUDES, solicitudes)

            print(Fore.GREEN + "\n✔ Solicitud aprobada y préstamo creado.")
            registrar_log(
                f"Solicitud aprobada - ID: {solicitud['id_solicitud']}, "
                f"Usuario: {solicitud['nombre_usuario']}, "
                f"Herramienta: {solicitud['herramienta']}, "
                f"Cantidad: {solicitud['cantidad_solicitada']}",
                "INFO"
            )

        else:
            print(Fore.RED + "\nNo hay stock suficiente para aprobar.")
            solicitud["estado"] = "Rechazada - Stock insuficiente"
            guardar_datos(ARCHIVO_SOLICITUDES, solicitudes)
            registrar_log(
                f"Solicitud rechazada por stock insuficiente - ID: {solicitud['id_solicitud']}",
                "INFO"
            )
    else:
        solicitud["estado"] = "Rechazada - Por administrador"
        guardar_datos(ARCHIVO_SOLICITUDES, solicitudes)
        print(Fore.YELLOW + "\nSolicitud rechazada.")
        registrar_log(f"Solicitud rechazada por administrador - ID: {solicitud['id_solicitud']}", "INFO")

    pausa()

# ==========================================
# CREAR SOLICITUD (USUARIO)
# ==========================================

def crear_solicitud_usuario():
    from agregar_herramienta import cargar_herramientas
    
    herramientas = cargar_herramientas()
    solicitudes = cargar_datos(ARCHIVO_SOLICITUDES)

    linea()
    print(Fore.YELLOW + Style.BRIGHT + "   CREAR SOLICITUD DE HERRAMIENTA")
    linea()

    # Mostrar solo herramientas activas
    print("\nHERRAMIENTAS DISPONIBLES:\n")
    activas = [h for h in herramientas if h["estado"] == "activa"]
    
    if not activas:
        print(Fore.RED + "No hay herramientas disponibles en este momento.")
        pausa()
        return

    for h in activas:
        print(f"ID: {h['id']} - {h['nombre']} - Disponibles: {h['cantidad']} - Categoría: {h['categoria']}")

    print()
    id_herramienta = input("Ingrese ID de herramienta: ").strip()
    herramienta = next((h for h in herramientas if str(h["id"]) == id_herramienta), None)

    if not herramienta:
        print(Fore.RED + "Herramienta no encontrada.")
        pausa()
        return

    try:
        cantidad = int(input("Cantidad deseada: "))
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Cantidad inválida.")
        pausa()
        return

    nombre_usuario = input("Su nombre: ").strip()
    id_usuario = input("Su ID de usuario: ").strip()

    if not nombre_usuario or not id_usuario:
        print(Fore.RED + "Debe ingresar su nombre e ID.")
        pausa()
        return

    nueva_solicitud = {
        "id_solicitud": generar_id_solicitud(solicitudes),
        "id_usuario": id_usuario,
        "nombre_usuario": nombre_usuario,
        "id_herramienta": id_herramienta,
        "herramienta": herramienta["nombre"],
        "cantidad_solicitada": cantidad,
        "fecha_solicitud": datetime.now().strftime("%Y-%m-%d"),
        "estado": "Pendiente"
    }

    solicitudes.append(nueva_solicitud)
    guardar_datos(ARCHIVO_SOLICITUDES, solicitudes)

    print(Fore.GREEN + "\n✔ Solicitud creada correctamente.")
    print(Fore.YELLOW + "Espere la aprobación del administrador.")
    
    registrar_log(
        f"Solicitud creada por usuario - Usuario: {nombre_usuario}, "
        f"Herramienta: {herramienta['nombre']}, Cantidad: {cantidad}",
        "INFO"
    )
    
    pausa()

# ==========================================
# REPORTE
# ==========================================

def reporte_prestamos_activos():
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)
    activos = [p for p in prestamos if p["estado"] == "Activo"]

    linea()
    print(Fore.YELLOW + Style.BRIGHT + "        PRÉSTAMOS ACTIVOS")
    linea()

    if not activos:
        print(Fore.YELLOW + "No hay préstamos activos.")
        pausa()
        return

    hoy = datetime.now().date()

    for p in activos:
        try:
            fecha_dev = datetime.strptime(
                p["fecha_estimada_devolucion"], "%Y-%m-%d"
            ).date()

            if fecha_dev < hoy:
                vencido = f"{Fore.RED}⚠ VENCIDO{Fore.WHITE}"
            else:
                vencido = f"{Fore.GREEN}✓ Al día{Fore.WHITE}"
        except:
            vencido = "?"

        print(Fore.WHITE + f"""
ID Préstamo : {p['id_prestamo']}
Usuario     : {p['nombre_usuario']}
Herramienta : {p['herramienta']}
Cantidad    : {p['cantidad']}
Inicio      : {p['fecha_inicio']}
Devolución  : {p['fecha_estimada_devolucion']} {vencido}
Estado      : {p['estado']}
-----------------------------------------------
""")

    pausa()

# ==========================================
# MENÚ
# ==========================================

def menu_prestamos():
    while True:
        linea()
        print(Fore.YELLOW + Style.BRIGHT + "     SISTEMA DE GESTIÓN DE PRÉSTAMOS")
        linea()

        print(Fore.GREEN + " 1 ➤ Registrar préstamo")
        print(Fore.BLUE + " 2 ➤ Devolver herramienta")
        print(Fore.MAGENTA + " 3 ➤ Ver préstamos activos")
        print(Fore.RED + " 4 ➤ Volver")

        linea()

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            devolver_herramienta()
        elif opcion == "3":
            reporte_prestamos_activos()
        elif opcion == "4":
            break
        else:
            print(Fore.RED + "Opción inválida.")
            pausa()



