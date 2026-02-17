# CASO 07 - Eliminar Usuario con Préstamos Activos

## 📌 Objetivo
Verificar que el sistema NO permite eliminar un usuario que tiene préstamos activos.

## 🔧 Precondiciones
- Sistema ejecutándose
- Login como administrador
- Existe usuario ID: U001 (Juan Pérez)
- Juan Pérez tiene un préstamo con estado: Activo

## 📥 DATOS DE ENTRADA
```
Opción menú admin : 1 (Gestión de Usuarios)
Opción sub-menú   : 5 (Eliminar usuario)
ID                : U001   ← usuario con préstamo activo
```

## 📤 SALIDA ESPERADA
```
No se puede eliminar. Tiene préstamos activos.
```

## 📁 VERIFICACIÓN EN ARCHIVOS
**usuarios.json NO debe cambiar** (usuario no eliminado)

**logs.txt debe contener:**
```
[WARNING] Intento de eliminar usuario con préstamos activos: Juan Pérez (ID: U001)
```

## ✅ RESULTADO
PASÓ - El sistema protege la integridad de datos bloqueando la eliminación.
