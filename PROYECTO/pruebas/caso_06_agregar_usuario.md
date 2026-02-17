# CASO 06 - Agregar Usuario Correctamente

## 📌 Objetivo
Verificar que el sistema permite registrar un nuevo usuario con datos válidos.

## 🔧 Precondiciones
- Sistema ejecutándose
- Login como administrador
- No existe usuario con ID U001

## 📥 DATOS DE ENTRADA
```
Opción menú admin : 1 (Gestión de Usuarios)
Opción sub-menú   : 1 (Agregar usuario)
ID                : U001
Nombres           : Juan
Apellidos         : Pérez
Teléfono          : 3001234567
Dirección         : Calle 123 # 45-67
Tipo              : residente
```

## 📤 SALIDA ESPERADA
```
Usuario agregado correctamente.
```

## 📁 VERIFICACIÓN EN ARCHIVOS
**usuarios.json debe contener:**
```json
{
    "id": "U001",
    "nombres": "Juan",
    "apellidos": "Pérez",
    "telefono": "3001234567",
    "direccion": "Calle 123 # 45-67",
    "tipo": "residente"
}
```

**logs.txt debe contener:**
```
[INFO] Usuario agregado: Juan Pérez (ID: U001, Tipo: residente)
```

## ✅ RESULTADO
PASÓ - El usuario se registra correctamente en el sistema.
