# CASO 03 - Registrar Préstamo con Stock Disponible

## 📌 Objetivo
Verificar que el sistema registra un préstamo cuando hay stock suficiente.

## 🔧 Precondiciones
- Sistema ejecutándose
- Login como administrador
- Existe usuario ID: U001 (Juan Pérez)
- Existe herramienta ID: H001 (Taladro, activa, cantidad: 5)

## 📥 DATOS DE ENTRADA
```
Opción menú admin : 3 (Gestión de Préstamos)
Opción sub-menú   : 1 (Registrar préstamo)
ID usuario        : U001
ID herramienta    : H001
Cantidad          : 2
Fecha inicio      : 17/02/2025
Fecha devolución  : 24/02/2025
Observaciones     : Para trabajo en casa
```

## 📤 SALIDA ESPERADA
```
Préstamo registrado correctamente.
```

## 📁 VERIFICACIÓN EN ARCHIVOS
**prestamos.json debe contener:**
```json
{
    "id_prestamo": 1,
    "id_usuario": "U001",
    "nombre_usuario": "Juan Pérez",
    "id_herramienta": "H001",
    "herramienta": "Taladro",
    "cantidad": 2,
    "fecha_inicio": "17/02/2025",
    "fecha_estimada_devolucion": "24/02/2025",
    "estado": "Activo",
    "observaciones": "Para trabajo en casa"
}
```

**herramientas.json debe actualizarse:**
```
cantidad: 5 → 3  (se restaron 2)
```

**logs.txt debe contener:**
```
[INFO] Préstamo registrado - Usuario: Juan, Herramienta: Taladro, Cantidad: 2
```

## ✅ RESULTADO
PASÓ - El préstamo se registra y el stock se actualiza correctamente.
