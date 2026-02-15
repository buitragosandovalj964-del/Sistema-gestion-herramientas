# 🔧 Sistema de Gestión de Herramientas Comunitarias

Proyecto desarrollado en Python para la administración eficiente de herramientas en un sistema comunitario o institucional. Este sistema facilita el préstamo y control de herramientas entre vecinos, evitando pérdidas y desorganización.

---

## 📌 Planteamiento del Problema

En muchos barrios existe la costumbre de compartir herramientas entre vecinos para evitar que cada persona tenga que comprarlas todas. El problema es que, con el tiempo, se pierde el control: algunas herramientas no se devuelven a tiempo, otras se dañan y no se sabe quién las tiene, o simplemente no hay registro claro de cuántas hay disponibles.

La junta comunal de tu barrio ha decidido organizar este proceso mediante un programa de consola que registra las herramientas, los vecinos y los beneficios obtenidos. Con esta solución, esperan que cualquier integrante de la comunidad pueda consultar la información sin depender de cuadernos ni llamadas telefónicas.

---

## 🎯 Requisitos del Sistema

### Gestión de Herramientas
Cada herramienta debe registrar: ID, nombre, categoría (ej. construcción, jardinería), cantidad disponible, estado (activa, en reparación, fuera de servicio) y valor estimado.  
El programa debe permitir: crear, listar, buscar, actualizar y eliminar o inactivar herramientas.

### Gestión de Usuarios
Cada vecino debe registrar: ID, nombres, apellidos, teléfono, dirección y tipo de usuario (ej. residente, administrador).  
Operaciones: crear, listar, buscar, actualizar y eliminar usuarios.

### Gestión de Préstamos
Al registrar un préstamo se debe guardar: ID del préstamo, usuario, herramienta, cantidad, fecha de inicio, fecha estimada de devolución, estado y observaciones.  
El sistema debe verificar la disponibilidad de la herramienta y ajustar la cantidad en stock.  
Cuando se devuelva la herramienta, se debe actualizar el estado del préstamo y restaurar la cantidad disponible.

### Consultas e Informes
- Herramientas con stock bajo (por ejemplo, menos de 3 unidades).
- Préstamos activos y vencidos.
- Historial de préstamos de un usuario.
- Herramientas más solicitadas por la comunidad.
- Usuarios que han solicitado más herramientas.

### Registro de Eventos (Logs)
Todo error o evento relevante (ejemplo: intentar prestar más herramientas de las disponibles) debe quedar registrado en un archivo de texto para seguimiento de la administración.

### Permisos a Manejar
- **Administrador**: Se encargará de registrar a los usuarios y sus herramientas con el fin de evitar la suplantación de identidad.
- **Usuario**: Puede consultar el estado de las herramientas, cuándo quedarán disponibles y quién la posee. Del mismo modo, puede crear una solicitud de herramienta que debe ser aprobada por el administrador.

---

## 🚀 Funcionalidades

- ✅ Registro y gestión completa de herramientas (CRUD: Crear, Leer, Actualizar, Eliminar).
- ✅ Gestión de usuarios con roles diferenciados (residente, administrador).
- ✅ Control de préstamos con validación de stock y fechas.
- ✅ Generación de reportes y consultas avanzadas.
- ✅ Registro automático de logs para auditoría y seguimiento.
- ✅ Interfaz de consola intuitiva y fácil de usar.

---

## 🛠 Tecnologías Utilizadas

- **Python 3**: Lenguaje principal para el desarrollo del programa.
- **Manejo de Archivos**: Almacenamiento de datos en archivos JSON para persistencia simple.
- **JSON**: Formato de datos para bases de datos ligeras.
- **Git y GitHub**: Control de versiones y colaboración.

---

## 📂 Estructura del Proyecto

sistema-herramientas/
# Archivo principal del programa 
 ├── main.py 
  # Módulo para gestión de herramientas
   ├── herramientas.py
   # Módulo para gestión de usuarios
  ├── usuarios.py 
   # Módulo para gestión de préstamos
  ├── prestamos.py
  # Módulo para consultas e informes 
  ├── reportes.py 
   # Módulo para registro de eventos
   ├── logs.py 
   # Archivo JSON para herramientas 
    ├── herramientas.json 
    # Archivo JSON para usuarios 
     │ ├── usuarios.json  
     # Archivo JSON para préstamos 
      ├──prestamos.json
 # Archivo de texto para logs 
  │└── logs.txt

  
---

## 🖥 Instalación y Configuración

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/buitragosandovalj964-del/sistema-herramientas.git
   cd sistema-herramientas


   
---

## 👨‍💻 Autor

**Jhoan Sebastián Buitrago Sandoval**  
camper de campusland 
Proyecto python – 2026
