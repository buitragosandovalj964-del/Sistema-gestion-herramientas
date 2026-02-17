# CASO 05 - Préstamo de Herramienta No Activa

## 📌 Objetivo
Verificar que el sistema NO permite prestar herramientas en reparación o fuera de servicio.

## 🔧 Precondiciones
- Sistema ejecutándose
- Login como administrador
- Existe herramienta ID: H002 (Cortadora, estado: en reparacion)

## 📥 DATOS DE ENTRADA
```
Opción menú admin : 3 (Gestión de Préstamos)
Opción sub-menú   : 1 (Registrar préstamo)
ID usuario        : U001
ID herramienta    : H002   ← herramienta en reparación
Cantidad          : 1
```

## 📤 SALIDA ESPERADA
```
La herramienta no está disponible.
Estado actual: en reparacion
```

## 📁 VERIFICACIÓN EN ARCHIVOS
**prestamos.json NO debe cambiar** (no se creó préstamo)

**herramientas.json NO debe cambiar** (stock intacto)

**logs.txt debe contener:**
```
[WARNING] Intento de préstamo de herramienta en estado 'en reparacion': Cortadora
```

## ✅ RESULTADO
PASÓ - El sistema bloquea correctamente el préstamo de herramientas no disponibles.
