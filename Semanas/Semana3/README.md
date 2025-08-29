## Semana 3: Proceso de Desarrollo de Software
### Modelos de desarrollo de software
1. Modelo en cascada

- Descripción: Proceso lineal y secuencial. Cada fase debe completarse antes de pasar a la siguiente.

- Fases típicas: Requisitos → Diseño → Implementación → Pruebas → Despliegue → Mantenimiento.

- Ventaja: Simple y fácil de seguir.

- Desventaja: No permite volver atrás si hay errores en fases anteriores.

2. Modelo en espiral

- Descripción: Combina características del modelo en cascada e incremental, usando ciclos (espirales).

- Cada ciclo incluye: Planificación, Análisis de riesgos, Desarrollo y Evaluación.

- Ventaja: Muy bueno para proyectos grandes con riesgos altos.

- Desventaja: Complejo y costoso de gestionar.

3. Modelo incremental

- Descripción: El software se desarrolla por partes o módulos funcionales. Cada incremento añade una funcionalidad.

- Ventaja: Permite ver resultados rápidamente y aplicar mejoras conforme avanza el desarrollo.

- Desventaja: Puede ser difícil mantener una arquitectura coherente si no se planifica bien.

4. Modelo iterativo

- Descripción: Se desarrolla el sistema en versiones repetidas (iteraciones), mejorando cada una según retroalimentación.

- Similar al incremental, pero con más énfasis en la repetición y mejora continua.

- Ventaja: Adaptable al cambio y al feedback del cliente.

- Desventaja: Puede llevar a extender el proyecto más de lo planeado si no se controla bien.

### 6 etapas del ciclo de vida del software

**Recolección de requisitos**

Qué necesita el cliente o usuario.

Se documentan requerimientos funcionales y no funcionales.

**Análisis**

Se estudian los requisitos para entenderlos a fondo y planificar soluciones.

Se detectan posibles problemas.

**Diseño**

Se elabora la arquitectura y diseño del sistema (estructura, interfaz, base de datos, etc.).

**Implementación (o codificación)**

Los programadores escriben el código basado en el diseño.

**Pruebas**

Se verifican errores, bugs y si el software cumple los requisitos.

Incluye pruebas unitarias, de integración, de sistema, etc.

**Mantenimiento**

Corrección de errores posteriores, actualizaciones y mejoras futuras.

Etapa más larga del ciclo de vida.


### Diferencias entre KanBan y Scrum

| Característica         | Kanban                                  | Scrum                                     |
|------------------------|------------------------------------------|--------------------------------------------|
| **Enfoque**            | Flujo continuo de trabajo                | Iteraciones llamadas "sprints"             |
| **Estructura del tiempo** | No hay sprints, trabajo continuo       | Sprints fijos (usualmente de 2-4 semanas)  |
| **Roles definidos**    | No requiere roles específicos            | Requiere roles: Scrum Master, Product Owner, y equipo de desarrollo |
| **Planificación**      | Flexible, basada en prioridades          | Planificación al inicio de cada sprint     |
| **Entrega**            | Entrega continua                         | Entrega al final de cada sprint            |
| **Tablero**            | Tablero Kanban con columnas personalizables | Tablero Scrum con backlog y sprint board |
| **Cambio durante el proceso** | Se permite en cualquier momento       | No se permite hasta que termine el sprint  |
| **Métricas comunes**   | Lead time, cycle time, throughput        | Velocidad del equipo (story points/sprint) |
| **Ideal para**         | Proyectos con tareas cambiantes o soporte continuo | Proyectos con entregables definidos y planificación detallada |

## Charla SIMOVI
### Realizada por el Ing. Fabian Abarca Phd.
Se plantea un desarrollo de una guia practica de diseño e implementacion para tomadores de decisiones y otra entidades del sector, dentro y fuera de la universidad.
**Data Bus**: Es la plataforma para recoleccion y suministro de datos.
**InfoBus**: Plataforma para consumo de datos y distribucion de informacion.

