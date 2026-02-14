from datetime import datetime
import os

ARCHIVO_LOG = "logs.txt"

def registrar_log(mensaje, nivel="INFO"):
    try:
        # Crear archivo si no existe
        if not os.path.exists(ARCHIVO_LOG):
            with open(ARCHIVO_LOG, "w", encoding="utf-8") as f:
                f.write("===== SISTEMA DE INVENTARIO - LOGS =====\n")

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
            archivo.write(f"[{fecha}] [{nivel}] {mensaje}\n")

    except Exception as e:
        print(f"Error al escribir en el log: {e}")


