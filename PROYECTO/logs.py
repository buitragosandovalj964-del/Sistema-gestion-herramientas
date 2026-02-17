# -*- coding: utf-8 -*-

ARCHIVO_LOG = "logs.txt"

# Contador simple para simular timestamp
contador_logs = 0

def registrar_log(mensaje, nivel="INFO"):
    global contador_logs
    try:
        # Intentar leer el archivo para ver si existe
        try:
            archivo_existente = open(ARCHIVO_LOG, "r", encoding="utf-8")
            archivo_existente.close()
        except:
            # Si no existe, crearlo
            archivo_nuevo = open(ARCHIVO_LOG, "w", encoding="utf-8")
            archivo_nuevo.write("===== SISTEMA DE INVENTARIO - LOGS =====\n")
            archivo_nuevo.close()

        contador_logs += 1
        
        # Agregar el nuevo log
        archivo = open(ARCHIVO_LOG, "a", encoding="utf-8")
        archivo.write("[Evento " + str(contador_logs) + "] [" + nivel + "] " + mensaje + "\n")
        archivo.close()

    except Exception as e:
        print("Error al escribir en el log: " + str(e))

