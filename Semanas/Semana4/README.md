# Semana 4

## Sistema de Control de Versiones

Un sistema de control de versiones es una herramienta que permite registrar los cambios realizados en los archivos de un proyecto a lo largo del tiempo. Es fundamental para el trabajo colaborativo, ya que permite ver quién hizo qué cambio, cuándo y por qué.

> **Nota:** Nunca se debe generar un PDF directamente desde el código. En su lugar, se debe documentar correctamente usando un archivo `README.md` y luego, si es necesario, generar el PDF a partir de esa documentación.

---

## Tipos de Sistemas de Control de Versiones

1. **Sistemas Locales:**  
   - Manejan versiones en una única máquina.
   - Ejemplo: RCS.

2. **Sistemas Centralizados (CVCS):**  
   - Un servidor central almacena todas las versiones.
   - Ejemplo: Subversion (SVN).

3. **Sistemas Distribuidos (DVCS):**  
   - Cada usuario tiene una copia completa del repositorio.
   - Ejemplo: Git, Mercurial.

---

## ¿Qué es GitHub?

**GitHub** es una plataforma en línea que permite alojar repositorios Git. Es ampliamente usada para el desarrollo colaborativo de software, control de versiones y revisión de código.

**Funciones principales:**
- Almacenamiento en la nube de repositorios Git.
- Herramientas para colaboración y revisión de código.
- Integración con herramientas de CI/CD.
- Seguimiento de issues y tareas del proyecto.

---

## Resumen de Etapas de Desarrollo de Cambios en el Código

1. **Working Directory (Directorio de trabajo):**  
   Donde se hacen los cambios en el código.

2. **Staging Area (Área de preparación):**  
   Donde se seleccionan los cambios que se desean incluir en el próximo commit con `git add`.

3. **Local Repository (Repositorio local):**  
   Donde se guardan los commits localmente usando `git commit`.

4. **Remote Repository (Repositorio remoto):**  
   Donde se suben los commits para compartir con otros colaboradores usando `git push`.

---

## Documentación en Proyectos de Software

La documentación es una parte crítica de cualquier proyecto de software. Permite entender el funcionamiento del sistema, facilita el mantenimiento y mejora la comunicación entre los miembros del equipo.

**Importancia:**
- Ayuda a nuevos desarrolladores a integrarse al proyecto.
- Facilita la detección de errores y mejora la calidad del código.
- Permite escalar y mantener el software a largo plazo.

---

## Tipos de Documentación

1. **Documentación Técnica:**
   - Describe el funcionamiento interno del software (API, arquitectura, dependencias).

2. **Documentación de Usuario:**
   - Instrucciones sobre cómo instalar, configurar y utilizar el software.

3. **Documentación de Proyecto:**
   - Información general como objetivos, planificación, cronogramas, etc.

4. **Documentación de Código:**
   - Comentarios y descripciones dentro del código fuente.

---

## Buenas Prácticas para Documentar Software

- Usar formatos estándar como Markdown (`.md`) para mantener legibilidad.
- Mantener la documentación actualizada con el código.
- Escribir pensando en el lector (claro, conciso y completo).
- Usar comentarios útiles en el código, evitando obviedades.
- Organizar la documentación en secciones: instalación, uso, ejemplos, etc.
- Incluir ejemplos de uso del software o código.
- Añadir un `README.md` completo en cada repositorio.

---

## Herramientas de Documentación Automática

Estas herramientas generan documentación a partir del código fuente, lo cual ahorra tiempo y asegura precisión.

**Algunas herramientas comunes:**
- **Doxygen** (C, C++, Java, etc.)
- **Sphinx** (Python)
- **Javadoc** (Java)
- **DocFX** (C#, .NET)
- **MkDocs** (Markdown + Python)

---

## Doxygen

**Doxygen** es una herramienta que permite generar documentación en formato HTML, LaTeX o PDF directamente desde comentarios estructurados en el código fuente.

### Características:
- Soporta múltiples lenguajes (C, C++, Python, Java, etc.).
- Extrae la estructura del código y genera documentación navegable.
- Permite incluir diagramas y ejemplos.
- Compatible con herramientas como Graphviz para visualizar diagramas de clases y dependencias.

### Ejemplo de comentario para Doxygen en C++:

```cpp
/**
 * @brief Calcula el área de un círculo.
 * 
 * @param radio Radio del círculo.
 * @return Área calculada.
 */
double calcularArea(double radio);
