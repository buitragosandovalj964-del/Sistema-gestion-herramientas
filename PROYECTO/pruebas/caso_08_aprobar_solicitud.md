# CASO 08 - Aprobar Solicitud Pendiente

## 📌 Objetivo
Verificar que el administrador puede aprobar una solicitud y el sistema crea el préstamo automáticamente.

## 🔧 Precondiciones
- Sistema ejecutándose
- Login como administrador
- Existe solicitud ID: 1 (estado: Pendiente)
  * Usuario: U001 - Juan Pérez
  * Herramienta: H001 - Taladro
  * Cantidad solicitada: 3
- Stock actual de Taladro: 5 unidades
- Estado Taladro: activa

## 📥 DATOS DE ENTRADA
```
Opción menú admin : 4 (Aprobar Solicitudes)
ID solicitud      : 1
¿Aprobar?         : s
Fecha inicio      : 17/02/2025
Fecha devolución  : 24/02/2025
```

## 📤 SALIDA ESPERADA
```
Solicitud aprobada y préstamo creado.
```

## 📁 VERIFICACIÓN EN ARCHIVOS
**solicitudes.json debe actualizarse:**
```
estado: "Pendiente" → "Aprobada"
```

**prestamos.json debe contener nuevo préstamo:**
```json
{
    "id_prestamo": 2,
    "id_usuario": "U001",
    "nombre_usuario": "Juan Pérez",
    "herramienta": "Taladro",
    "cantidad": 3,
    "fecha_inicio": "17/02/2025",
    "fecha_estimada_devolucion": "24/02/2025",
    "estado": "Activo"
}
```

**herramientas.json debe actualizarse:**
```
cantidad: 5 → 2  (se restaron 3)
```

**logs.txt debe contener:**
```
[INFO] Solicitud aprobada - ID: 1, Usuario: Juan Pérez, Herramienta: Taladro
```

## ✅ RESULTADO
PASÓ - La solicitud se aprueba y el préstamo se crea automáticamente.
