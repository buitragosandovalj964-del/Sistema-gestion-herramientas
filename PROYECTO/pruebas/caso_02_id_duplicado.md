# CASO 02 - Agregar Herramienta con ID Duplicado

## 📌 Objetivo
Verificar que el sistema rechaza agregar una herramienta con ID ya existente.

## 🔧 Precondiciones
- Sistema ejecutándose
- Login como administrador
- Ya existe herramienta con ID H001

## 📥 DATOS DE ENTRADA
```
Opción menú admin : 2 (Gestión de Herramientas)
Opción sub-menú   : 1 (Agregar herramienta)
ID                : H001   ← ID que ya existe
```

## 📤 SALIDA ESPERADA
```
Ya existe una herramienta con ese ID.
```

## 📁 VERIFICACIÓN EN ARCHIVOS
**herramientas.json NO debe cambiar** (no se agrega nada nuevo)

**logs.txt debe contener:**
```
[WARNING] Intento de agregar herramienta con ID duplicado: H001
```

## ✅ RESULTADO
PASÓ - El sistema detecta el duplicado y rechaza la operación.
