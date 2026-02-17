# CASO 04 - Registrar Préstamo Sin Stock Suficiente

## 📌 Objetivo
Verificar que el sistema crea una solicitud cuando no hay stock suficiente.

## 🔧 Precondiciones
- Sistema ejecutándose
- Login como administrador
- Existe usuario ID: U001
- Existe herramienta ID: H001 (Taladro, cantidad disponible: 2)

## 📥 DATOS DE ENTRADA
```
Opción menú admin : 3 (Gestión de Préstamos)
Opción sub-menú   : 1 (Registrar préstamo)
ID usuario        : U001
ID herramienta    : H001
Cantidad          : 5   ← más de lo disponible (solo hay 2)
Fecha de hoy      : 17/02/2025
```

## 📤 SALIDA ESPERADA
```
No hay stock suficiente.
Disponible: 2, Solicitado: 5
Se ha generado una solicitud pendiente.
```

## 📁 VERIFICACIÓN EN ARCHIVOS
**solicitudes.json debe contener:**
```json
{
    "id_solicitud": 1,
    "id_usuario": "U001",
    "nombre_usuario": "Juan Pérez",
    "id_herramienta": "H001",
    "herramienta": "Taladro",
    "cantidad_solicitada": 5,
    "fecha_solicitud": "17/02/2025",
    "estado": "Pendiente"
}
```

**herramientas.json NO debe cambiar** (no se prestó nada)

**logs.txt debe contener:**
```
[INFO] Solicitud creada por falta de stock - Usuario: Juan, Herramienta: Taladro
```

## ✅ RESULTADO
PASÓ - El sistema detecta la falta de stock y crea la solicitud automáticamente.
