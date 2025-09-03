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


# Software Development Methodologies: Types, Selection Criteria & Stats

Este documento resume el artículo **"Software Development Methodologies: Types, Selection Criteria & Stats"** publicado por Itransition, siguiendo los lineamientos solicitados para el curso *Diseño de Software para Ingeniería*.

---

## 1. Resumen General
Una **metodología de desarrollo de software** es un conjunto de prácticas, principios y procesos que guían cómo planificar, diseñar, desarrollar, probar y entregar productos de software.  
Su **propósito fundamental** es:
- Asegurar **calidad** en el producto final.
- Establecer **orden y estructura** en cada fase del proyecto.
- Permitir una **comunicación clara** entre equipos técnicos y clientes.
- Reducir **riesgos y costos** asociados al desarrollo.

En otras palabras, es el mapa que dirige todo el proceso de construcción del software, desde la idea inicial hasta la implementación y mantenimiento.

---

## 2. Principales Enfoques

### 2.1 Metodologías Secuenciales
Ejemplos: **Waterfall** y **V-Model**.

**Características principales**  
- Se basan en un **flujo lineal** y bien estructurado.  
- Cada fase debe completarse **antes** de pasar a la siguiente.  
- Las etapas típicas incluyen:
  1. Requerimientos
  2. Diseño
  3. Implementación
  4. Pruebas
  5. Despliegue
  6. Mantenimiento

**Ventajas:**  
- Documentación clara y exhaustiva.  
- Ideal para proyectos **con requisitos fijos** y poco propensos a cambios.  
- Facilita la gestión en entornos altamente regulados.  

**Desventajas:**  
- **Rigidez** ante cambios durante el desarrollo.  
- Los problemas pueden descubrirse **tarde**, encareciendo correcciones.  

**Casos de uso:**  
- Industria aeroespacial, sistemas embebidos, proyectos de infraestructura crítica.

---

### 2.2 Metodologías Ágiles
Ejemplos: **Scrum**, **Kanban**, **Extreme Programming (XP)**.

**Características principales:**  
- Se basan en **iteraciones cortas** e incrementales.  
- Enfoque en **colaboración continua** entre equipos y clientes.  
- Priorizan **entregas rápidas** y adaptabilidad a cambios.  

**Estadísticas de adopción:**  
- El **71 % de las empresas** en todo el mundo ya utilizan Agile como principal metodología.  

**Ventajas:**  
- Alta **flexibilidad** y capacidad de adaptación.  
- Retroalimentación rápida y continua.  
- Mayor **satisfacción del cliente** al recibir versiones funcionales tempranas.  

**Desventajas:**  
- Requiere **madurez del equipo** y comunicación constante.  
- Puede generar **falta de documentación** en algunos contextos.  

**Casos de uso:**  
- Startups tecnológicas, desarrollo de aplicaciones móviles, entornos con requisitos cambiantes.

---

## 3. Criterios para Elegir una Metodología
Las empresas deben considerar factores como:
- **Tamaño y complejidad del proyecto.**
- **Presupuesto y tiempo disponible.**
- **Riesgos e incertidumbre** del entorno.  
- **Requisitos de documentación** vs. velocidad de entrega.  
- **Restricciones regulatorias** (ejemplo: banca, salud, gobierno).  
- **Capacidades del equipo** y nivel de experiencia en cada enfoque.  

La decisión ideal equilibra **flexibilidad**, **calidad** y **cumplimiento de objetivos** según el tipo de proyecto.

---

## 4. Tendencias Recientes y Observaciones Clave
- **Enfoques híbridos:** combinación de Agile con **DevOps** para integrar desarrollo, pruebas e implementación continua (CI/CD).  
- **Modelos escalados:** como **SAFe** o **LeSS** para coordinar múltiples equipos ágiles en grandes organizaciones.  
- **Mayor automatización:** herramientas para pruebas, integración y despliegue reducen tiempos y errores humanos.  
- **Industria 4.0:** metodologías adaptadas a entornos con IoT, IA y software embebido con mayores requisitos de calidad.  

---

## 5. Opinión Personal
En mi opinión:  
- Para un **proyecto de aplicación móvil**, una metodología **Agile** (como **Scrum**) sería ideal por su **capacidad de adaptación** y entregas rápidas que permiten incorporar retroalimentación temprana.  
- En un **sistema bancario** como el realizado en Estructuras de Datos y algoritmos Abstractos, que tiene requisitos regulatorios estrictos, un **enfoque híbrido** sería más adecuado:  
  - **Waterfall** para etapas iniciales de análisis y diseño (documentación detallada).  
  - **Agile** para el desarrollo e implementación iterativa, reduciendo riesgos y mejorando la calidad final.  

Esta combinación ofrece **control y flexibilidad** al mismo tiempo, aprovechando lo mejor de ambos mundos.

---

## 6. Conclusión
Las metodologías de desarrollo de software han evolucionado para adaptarse a **diferentes tipos de proyectos y entornos empresariales**.  
- Las metodologías **secuenciales** siguen siendo útiles en contextos con **alta predictibilidad**.  
- Las metodologías **ágiles** lideran la adopción en proyectos modernos por su **capacidad de respuesta y eficiencia**.  
- Las **tendencias híbridas** apuntan hacia el futuro, buscando equilibrio entre **estructura y flexibilidad**.

La clave está en **elegir el enfoque adecuado** según los objetivos, restricciones y características del proyecto.

---


