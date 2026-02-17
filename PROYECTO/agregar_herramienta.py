# -*- coding: utf-8 -*-
import json
from colorama import Fore, Style, init
from logs import registrar_log

init(autoreset=True)

ARCHIVO_HERRAMIENTAS = "herramientas.json"

ESTADOS_VALIDOS = ["activa", "en reparacion", "fuera de servicio"]

# =====================================
# UTILIDADES VISUALES
# =====================================

def linea():
    print(Fore.CYAN + "=" * 65)

def titulo(texto):
    linea()
    print(Fore.YELLOW + Style.BRIGHT + texto)
    linea()

def pausa():
    input(Fore.LIGHTBLACK_EX + "\nPresione ENTER para continuar...")

# =====================================
# CARGAR Y GUARDAR
# =====================================

def cargar_herramientas():
    try:
        with open(ARCHIVO_HERRAMIENTAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        registrar_log("Archivo herramientas.json no encontrado, creando nuevo", "WARNING")
        return []
    except json.JSONDecodeError as e:
        registrar_log("Error al leer herramientas.json: " + str(e), "ERROR")
        return []

def guardar_herramientas(herramientas):
    try:
        with open(ARCHIVO_HERRAMIENTAS, "w", encoding="utf-8") as archivo:
            json.dump(herramientas, archivo, indent=4, ensure_ascii=False)
    except Exception as e:
        registrar_log("Error al guardar herramientas: " + str(e), "ERROR")
        print(Fore.RED + "Error al guardar: " + str(e))

# =====================================
# AGREGAR HERRAMIENTA
# =====================================

def agregar_herramienta():
    herramientas = cargar_herramientas()

    titulo("AGREGAR HERRAMIENTA")

    id_h = input(Fore.CYAN + "ID: ").strip()

    if not id_h:
        print(Fore.RED + "ID inválido.")
        registrar_log("Intento de agregar herramienta con ID vacío", "WARNING")
        pausa()
        return

    # Verificar si ya existe el ID
    for h in herramientas:
        if str(h["id"]) == id_h:
            print(Fore.RED + "Ya existe una herramienta con ese ID.")
            registrar_log("Intento de agregar herramienta con ID duplicado: " + id_h, "WARNING")
            pausa()
            return

    nombre = input("Nombre: ").strip().title()
    categoria = input("Categoría: ").strip().lower()
    estado = input("Estado (activa, en reparacion, fuera de servicio): ").strip().lower()

    if not nombre or not categoria or estado not in ESTADOS_VALIDOS:
        print(Fore.RED + "Datos inválidos o estado no permitido.")
        registrar_log("Datos inválidos al agregar herramienta", "WARNING")
        pausa()
        return

    try:
        cantidad = int(input("Cantidad disponible: "))
        if cantidad < 0:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Cantidad inválida.")
        registrar_log("Cantidad inválida al agregar herramienta", "WARNING")
        pausa()
        return

    try:
        valor = int(input("Valor estimado: "))
        if valor < 0:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Valor inválido.")
        registrar_log("Valor inválido al agregar herramienta", "WARNING")
        pausa()
        return

    nueva = {
        "id": id_h,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "estado": estado,
        "valor": valor
    }

    herramientas.append(nueva)
    guardar_herramientas(herramientas)

    print(Fore.GREEN + Style.BRIGHT + "\nHerramienta agregada correctamente.")
    registrar_log("Herramienta agregada: " + nombre + " (ID: " + id_h + ", Cantidad: " + str(cantidad) + ")", "INFO")
    pausa()

# =====================================
# LISTAR HERRAMIENTAS
# =====================================

def listar_herramientas():
    herramientas = cargar_herramientas()

    titulo("LISTA DE HERRAMIENTAS")

    if not herramientas:
        print(Fore.RED + "No hay herramientas registradas.")
        pausa()
        return

    for h in herramientas:
        # Color según estado
        if h['estado'] == 'activa':
            color_estado = Fore.GREEN
        elif h['estado'] == 'en reparacion':
            color_estado = Fore.YELLOW
        else:
            color_estado = Fore.RED

        print(Fore.WHITE + "\n" + "-" * 50)
        print("ID: " + str(h['id']))
        print("Nombre: " + h['nombre'])
        print("Categoría: " + h['categoria'])
        print("Cantidad: " + str(h['cantidad']))
        print("Estado: " + color_estado + h['estado'] + Fore.WHITE)
        print("Valor: $" + str(h['valor']))
    
    print("-" * 50)
    pausa()

# =====================================
# BUSCAR HERRAMIENTA
# =====================================

def buscar_herramienta():
    herramientas = cargar_herramientas()

    titulo("BUSCAR HERRAMIENTA")

    nombre_buscar = input("Ingrese el nombre: ").strip().lower()

    encontrada = False
    for h in herramientas:
        if nombre_buscar in h["nombre"].lower():
            if not encontrada:
                print(Fore.GREEN + "\nHerramientas encontradas:\n")
                encontrada = True
            
            print(Fore.WHITE + "-" * 50)
            print("ID: " + str(h['id']))
            print("Nombre: " + h['nombre'])
            print("Categoría: " + h['categoria'])
            print("Cantidad: " + str(h['cantidad']))
            print("Estado: " + h['estado'])
            print("Valor: $" + str(h['valor']))

    if not encontrada:
        print(Fore.RED + "Herramienta no encontrada.")
        registrar_log("Búsqueda sin resultados: " + nombre_buscar, "INFO")
    
    pausa()

# =====================================
# ACTUALIZAR HERRAMIENTA
# =====================================

def actualizar_herramienta():
    herramientas = cargar_herramientas()

    titulo("ACTUALIZAR HERRAMIENTA")

    id_buscar = input("Ingrese ID: ").strip()

    for h in herramientas:
        if str(h["id"]) == id_buscar:

            print(Fore.LIGHTBLACK_EX + "\nDeje en blanco si no desea cambiar el valor.\n")

            nuevo_nombre = input("Nuevo nombre (" + h['nombre'] + "): ").strip()
            nueva_categoria = input("Nueva categoría (" + h['categoria'] + "): ").strip()
            nueva_cantidad = input("Nueva cantidad (" + str(h['cantidad']) + "): ").strip()
            nuevo_estado = input("Nuevo estado (" + h['estado'] + "): ").strip().lower()
            nuevo_valor = input("Nuevo valor (" + str(h['valor']) + "): ").strip()

            cambios = []

            if nuevo_nombre:
                h["nombre"] = nuevo_nombre.title()
                cambios.append("nombre: " + nuevo_nombre)

            if nueva_categoria:
                h["categoria"] = nueva_categoria.lower()
                cambios.append("categoría: " + nueva_categoria)

            if nueva_cantidad:
                try:
                    cantidad_int = int(nueva_cantidad)
                    if cantidad_int >= 0:
                        h["cantidad"] = cantidad_int
                        cambios.append("cantidad: " + str(cantidad_int))
                except ValueError:
                    print(Fore.RED + "Cantidad inválida.")

            if nuevo_estado:
                if nuevo_estado in ESTADOS_VALIDOS:
                    h["estado"] = nuevo_estado
                    cambios.append("estado: " + nuevo_estado)
                else:
                    print(Fore.RED + "Estado no válido.")

            if nuevo_valor:
                try:
                    valor_int = int(nuevo_valor)
                    if valor_int >= 0:
                        h["valor"] = valor_int
                        cambios.append("valor: " + str(valor_int))
                except ValueError:
                    print(Fore.RED + "Valor inválido.")

            guardar_herramientas(herramientas)
            print(Fore.GREEN + Style.BRIGHT + "\nHerramienta actualizada correctamente.")
            
            if cambios:
                registrar_log("Herramienta " + id_buscar + " actualizada: " + ", ".join(cambios), "INFO")
            
            pausa()
            return

    print(Fore.RED + "Herramienta no encontrada.")
    registrar_log("Intento de actualizar herramienta inexistente: " + id_buscar, "WARNING")
    pausa()

# =====================================
# ELIMINAR HERRAMIENTA
# =====================================

def eliminar_herramienta():
    herramientas = cargar_herramientas()

    titulo("ELIMINAR HERRAMIENTA")

    id_eliminar = input("Ingrese ID: ").strip()

    for h in herramientas:
        if str(h["id"]) == id_eliminar:

            confirmacion = input(Fore.RED + "¿Está seguro? (s/n): ").strip().lower()

            if confirmacion == "s":
                nombre_eliminado = h["nombre"]
                herramientas.remove(h)
                guardar_herramientas(herramientas)
                print(Fore.GREEN + "Herramienta eliminada correctamente.")
                registrar_log("Herramienta eliminada: " + nombre_eliminado + " (ID: " + id_eliminar + ")", "INFO")
            else:
                print(Fore.YELLOW + "Operación cancelada.")

            pausa()
            return

    print(Fore.RED + "Herramienta no encontrada.")
    registrar_log("Intento de eliminar herramienta inexistente: " + id_eliminar, "WARNING")
    pausa()

# =====================================
# MENÚ DE GESTIÓN
# =====================================

def menu_herramientas():
    while True:
        titulo("GESTION DE HERRAMIENTAS")

        print(Fore.WHITE + "[1] Agregar herramienta")
        print(Fore.WHITE + "[2] Listar herramientas")
        print(Fore.WHITE + "[3] Buscar herramienta")
        print(Fore.WHITE + "[4] Actualizar herramienta")
        print(Fore.WHITE + "[5] Eliminar herramienta")
        print(Fore.RED   + "[6] Volver")

        linea()

        opcion = input(Fore.CYAN + "\nSeleccione opción: ")

        if opcion == "1":
            agregar_herramienta()
        elif opcion == "2":
            listar_herramientas()
        elif opcion == "3":
            buscar_herramienta()
        elif opcion == "4":
            actualizar_herramienta()
        elif opcion == "5":
            eliminar_herramienta()
        elif opcion == "6":
            break
        else:
            print(Fore.RED + "Opción inválida.")
            pausa()