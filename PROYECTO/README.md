# 🔧 Sistema de Gestión de Herramientas Comunitarias

Sistema desarrollado en Python para gestionar herramientas compartidas entre vecinos.

## 📋 Requisitos del Sistema

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 📦 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/buitragosandovalj964-del/Sistema-gestion-herramientas.git
cd Sistema-gestion-herramientas/PROYECTO
```

2. **Instalar dependencias**
```bash
pip install colorama
```

## 🚀 Ejecución
```bash
python principal.py
```

## 👤 Credenciales de Prueba

**Administrador:**
- Contraseña: `0611JB`

**Usuario:**
- Sin contraseña (acceso libre)

## 📖 Uso del Sistema

### Como Administrador
1. Ejecutar el programa
2. Seleccionar opción [1] Administrador
3. Ingresar contraseña: `0611JB`
4. Acceder a:
   - Gestión de usuarios
   - Gestión de herramientas
   - Gestión de préstamos
   - Aprobar solicitudes
   - Consultas y reportes

### Como Usuario
1. Ejecutar el programa
2. Seleccionar opción [2] Usuario
3. Acceder a:
   - Ver herramientas disponibles
   - Ver préstamos activos
   - Crear solicitud de herramienta
   - Consultas y reportes

## 📂 Estructura del Proyecto
```
PROYECTO/
├── principal.py              # Archivo principal
├── agregar_herramienta.py    # Gestión de herramientas
├── gestion_de_usuarios.py    # Gestión de usuarios
├── gestion_de_prestamos.py   # Gestión de préstamos
├── consultas_y_reportes.py   # Reportes
├── registros.py              # Sistema de logs
├── usuarios.json             # Datos de usuarios
├── herramientas.json         # Datos de herramientas
├── prestamos.json            # Datos de préstamos
├── solicitudes.json          # Solicitudes pendientes
└── logs.txt                  # Registro de eventos
```

## 🎯 Funcionalidades

- ✅ Gestión completa de herramientas (CRUD)
- ✅ Gestión de usuarios con roles (admin/residente)
- ✅ Sistema de préstamos con validaciones
- ✅ Sistema de solicitudes cuando no hay stock
- ✅ Aprobación de solicitudes por administrador
- ✅ Reportes y estadísticas de uso
- ✅ Sistema de logs para auditoría
- ✅ Validación de disponibilidad antes de prestar
- ✅ Control de préstamos vencidos

## 📝 Ejemplos de Uso

### Ejemplo 1: Registrar una herramienta
```
1. Login como administrador
2. Opción [2] Gestión de Herramientas
3. Opción [1] Agregar herramienta
4. Ingresar datos:
   - ID: H001
   - Nombre: Taladro
   - Categoría: construcción
   - Cantidad: 5
   - Estado: activa
   - Valor: 150000
```

### Ejemplo 2: Crear un préstamo
```
1. Login como administrador
2. Opción [3] Gestión de Préstamos
3. Opción [1] Registrar préstamo
4. Ingresar ID de usuario y herramienta
5. Sistema verifica disponibilidad
6. Se crea el préstamo y reduce stock
```

### Ejemplo 3: Solicitud cuando no hay stock
```
1. Acceso como usuario
2. Opción [3] Crear solicitud
3. Seleccionar herramienta deseada
4. Sistema crea solicitud "Pendiente"
5. Admin aprueba desde su menú
```

## 🐛 Solución de Problemas

**Error: ModuleNotFoundError: No module named 'colorama'**
```bash
pip install colorama
```

**Error: Archivos JSON no encontrados**
- Los archivos se crean automáticamente al ejecutar el programa

**Caracteres raros en la consola**
- Windows: `chcp 65001` en CMD antes de ejecutar

## 👨‍💻 Autor

Proyecto académico - 2025

## 📄 Licencia

Proyecto educativo
```

---

### **SOLUCIÓN 2: Crear Carpeta de Pruebas**

Crea la siguiente estructura:
```
PROYECTO/
└── pruebas/
    ├── README_PRUEBAS.md
    ├── caso_prueba_1.md
    ├── caso_prueba_2.md
    └── caso_prueba_3.md