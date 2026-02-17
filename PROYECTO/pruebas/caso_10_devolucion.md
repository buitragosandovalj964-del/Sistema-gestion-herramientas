# CASO 10 - Devolución de Herramienta

## 📌 Objetivo
Verificar que el sistema registra correctamente la devolución y restaura el stock.

## 🔧 Precondiciones
- Sistema ejecutándose
- Login como administrador
- Existe préstamo ID: 1 (estado: Activo)
  * Herramienta: Taladro
  * Cantidad prestada: 2
  * Stock actual de Taladro: 3

## 📥 DATOS DE ENTRADA
```
Opción menú admin : 3 (Gestión de Préstamos)
Opción sub-menú   : 2 (Devolver herramienta)
ID préstamo       : 1
Fecha devolución  : 20/02/2025
```

## 📤 SALIDA ESPERADA
```
Préstamo finalizado correctamente.
```

## 📁 VERIFICACIÓN EN ARCHIVOS
**prestamos.json debe actualizarse:**
```
estado: "Activo" → "Devuelto"
fecha_devolucion_real: "20/02/2025"
```

**herramientas.json debe actualizarse:**
```
cantidad: 3 → 5  (se sumaron 2 devueltos)
```

**logs.txt debe contener:**
```
[INFO] Devolución registrada - Préstamo ID: 1, Herramienta: Taladro, Cantidad: 2
```

## ✅ RESULTADO
PASÓ - La devolución se registra y el stock se restaura correctamente.
