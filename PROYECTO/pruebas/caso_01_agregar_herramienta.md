# CASO 01 - Agregar Herramienta Correctamente

## 📌 Objetivo
Verificar que el sistema permite agregar una herramienta con datos válidos.

## 🔧 Precondiciones
- Sistema ejecutándose
- Login como administrador (contraseña: 0611JB)
- No existe herramienta con ID H001

## 📥 DATOS DE ENTRADA
```
Opción menú admin : 2 (Gestión de Herramientas)
Opción sub-menú   : 1 (Agregar herramienta)
ID                : H001
Nombre            : Taladro
Categoría         : construcción
Estado            : activa
Cantidad          : 5
Valor             : 150000
```

## 📤 SALIDA ESPERADA
```
Herramienta agregada correctamente.
```

## 📁 VERIFICACIÓN EN ARCHIVOS
**herramientas.json debe contener:**
```json
{
    "id": "H001",
    "nombre": "Taladro",
    "categoria": "construcción",
    "cantidad": 5,
    "estado": "activa",
    "valor": 150000
}
```

**logs.txt debe contener:**
```
[INFO] Herramienta agregada: Taladro (ID: H001, Cantidad: 5)
```

## ✅ RESULTADO
PASÓ - El sistema agrega la herramienta y actualiza el JSON correctamente.
