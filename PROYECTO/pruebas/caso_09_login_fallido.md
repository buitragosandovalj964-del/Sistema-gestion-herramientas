# CASO 09 - Login con Contraseña Incorrecta

## 📌 Objetivo
Verificar que el sistema rechaza el acceso con contraseña incorrecta y registra el intento.

## 🔧 Precondiciones
- Sistema ejecutándose
- En el menú principal

## 📥 DATOS DE ENTRADA
```
Opción menú principal : 1 (Administrador)
Contraseña            : 12345   ← contraseña incorrecta
```

## 📤 SALIDA ESPERADA
```
Contraseña incorrecta.
```

## 📁 VERIFICACIÓN
**El sistema NO debe mostrar el menú admin**

**logs.txt debe contener:**
```
[WARNING] Intento de acceso de administrador fallido
```

## ✅ RESULTADO
PASÓ - El sistema rechaza contraseñas incorrectas y registra el intento fallido.
