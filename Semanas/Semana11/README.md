# Laboratorio de Depuracion en C++ con gdb, Valgrind y Sanitizers

## Introducción rápida a gdb y sus comandos

gdb es el depurador clásico para programas en C/C++. Permite ejecutar el binario de forma controlada, detenerse en puntos concretos, inspeccionar variables, recorrer el código línea a línea y obtener trazas de pila cuando ocurre un fallo. En la práctica se usa para reproducir errores, localizar la línea exacta donde se detiene el programa y entender por qué ocurrió.

Comandos típicos y su aplicación breve:

- run: inicia la ejecución.

- start: ejecuta hasta entrar a main y se detiene en su primera línea.

- break archivo:línea o break función: crea un punto de ruptura.

- continue: reanuda hasta el siguiente breakpoint o evento.

- next: avanza una línea sin entrar a las funciones llamadas.

- step: avanza una línea entrando en las funciones llamadas.

- finish: ejecuta hasta salir de la función actual.

- where o bt: muestra la traza de pila en el punto de parada.

- print expr: imprime el valor de una variable o expresión.

- list: muestra el código fuente alrededor de la línea actual.

A continuación, respuestas basadas en el código que suma un vector y luego accede a datos.at(4) con un vector de tamaño 4.

### 1. ¿Qué tipo de error genera el fallo de ejecución?

El acceso datos.at(4) provoca una excepción de tiempo de ejecución del tipo std::out_of_range. Si no es capturada, el programa terminará con una señal SIGABRT por excepción no manejada.

### 2. ¿Qué comando permite identificar la línea exacta donde ocurre el fallo?

Tras ejecutar con gdb y reproducir el fallo:

Usa where o bt para ver la traza de pila; el frame 0 indica la línea exacta.

Usa list para ver el código alrededor de esa línea.

Si hace falta, frame 0 para seleccionar el marco superior.

Secuencia típica:

(gdb) start              # o: break main; run
... reproducir el fallo ...
(gdb) where              # o: bt
(gdb) list

### 3. ¿Qué diferencia existe entre los comandos next y step en gdb?

Next (n) ejecuta la siguiente línea de código y salta por encima de las llamadas a funciones, deteniéndose en la siguiente línea del llamador . Mientras que step (s) ejecuta la siguiente línea y, si hay una llamada a función, entra en esa función y se detiene en su primera línea.



En C/C++ es común cometer errores de memoria (desbordes, dobles liberaciones, fugas, etc.). Para detectarlos existen dos enfoques populares:

 - sanitizers (instrumentación en tiempo de compilación/enlace que inserta comprobaciones en el binario)

- Valgrind/Memcheck (instrumentación dinámica que emula/ensancha la ejecución del binario sin recompilar con flags especiales).

Ambas herramientas ayudan a localizar fallos con trazas y contexto, pero no deben usarse a la vez sobre el mismo binario.

**¿Qué hace cada sanitizer y Valgrind?**
AddressSanitizer (ASan): detecta lecturas/escrituras fuera de rango en heap/stack/globales, use-after-free/use-after-scope, double free, etc. Suele reportar la línea exacta y un mapa de memoria sombra.

- LeakSanitizer (LSan): detecta fugas de memoria (bloques asignados no liberados al finalizar el proceso). En muchas plataformas viene integrado con ASan.

- UndefinedBehaviorSanitizer (UBSan): detecta comportamientos indefinidos (overflow con signo, división por cero en enteros, shift inválidos, punteros mal alineados, violaciones de tipo, etc.).

- ThreadSanitizer (TSan): detecta data races y errores de sincronización en programas multihilo.

- MemorySanitizer (MSan): detecta uso de memoria no inicializada (uninitialized reads). Requiere instrumentar todas las dependencias.

- Valgrind/Memcheck: sin recompilar con sanitizers, intercepta asignaciones y accesos para detectar overflows en heap, use-after-free, dobles free y fugas. También da orígenes de datos (track-origins) para lecturas no inicializadas. Suele ser más lento que ASan, pero muy útil cuando no puedes recompilar todo.

### 1 ¿Qué tipo de error detectó AddressSanitizer primero?
heap-buffer-overflow (escritura fuera de los límites del buffer en el heap) al copiar n + 1 bytes en un bloque reservado con solo n bytes.

### 2 ¿Cuál fue la causa de la fuga de memoria?
Se reservó memoria (por ejemplo, malloc(128)) y nunca se liberó con free(...) antes de terminar el programa; Valgrind la reportó como definitely lost.

### 3 ¿Por qué es importante compilar con la opción -g?
Porque añade símbolos de depuración (archivos, líneas, nombres de funciones/variables), permitiendo que gdb, ASan y Valgrind muestren exactamente dónde ocurre el fallo y produzcan trazas legibles para corregir rápidamente el problema.


En la programación concurrente, los errores relacionados con la sincronización —como las condiciones de carrera (data races)— pueden generar comportamientos impredecibles y difíciles de reproducir. Para detectarlos, existen herramientas de análisis dinámico como ThreadSanitizer y Helgrind, que permiten examinar el acceso concurrente a la memoria y los mecanismos de sincronización utilizados por un programa multihilo.

**ThreadSanitizer** es una herramienta desarrollada por Google que forma parte del compilador Clang/LLVM y GCC.
Su función principal es detectar condiciones de carrera, bloqueos incorrectos y accesos simultáneos no protegidos a variables compartidas durante la ejecución del programa.

- Se ejecuta junto con el binario instrumentado con -fsanitize=thread.

- Analiza en tiempo real los accesos de lectura y escritura en memoria.

- Indica el origen de los hilos involucrados, las líneas de código conflictivas y el tipo de acceso detectado.

**Helgrind** es una herramienta del conjunto Valgrind, diseñada para detectar errores de sincronización en programas con múltiples hilos (como condiciones de carrera, bloqueos no balanceados y uso incorrecto de mutexes).

- Supervisa todas las operaciones de memoria y sincronización del programa.

- Detecta accesos simultáneos a memoria compartida sin exclusión mutua.

- Aunque es muy precisa, tiene un alto costo en tiempo de ejecución, ya que instrumenta cada instrucción y operación de memoria del programa.

### 1. ¿Qué tipo de acceso detecta ThreadSanitizer como data race?

ThreadSanitizer detecta una condición de carrera (data race) cuando dos o más hilos acceden simultáneamente a la misma variable compartida, y al menos uno de esos accesos es de escritura, sin estar protegidos por mecanismos de sincronización (como std::mutex o std::atomic).

### 2. ¿Por qué Helgrind tiene un mayor costo de ejecución?

Helgrind presenta un mayor costo de ejecución porque instrumenta todas las operaciones de memoria y sincronización del programa, simulando su comportamiento interno para verificar dependencias entre hilos.

En concreto:

- Supervisa cada lectura y escritura en memoria.

- Mantiene un historial detallado de los bloqueos (mutex, join, wait, etc.).

Evalúa las relaciones de orden y exclusión mutua entre hilos. Esto implica un gran consumo de CPU y memoria, ralentizando el programa entre 10 y 50 veces. A cambio, proporciona una detección muy precisa de errores de concurrencia complejos.

### 3. ¿Qué ventajas tiene usar std::atomic frente a std::mutex?

std::atomic permite realizar operaciones seguras entre hilos sin necesidad de bloqueos explícitos, usando instrucciones atómicas de hardware.
En cambio, std::mutex bloquea completamente una sección crítica hasta que el hilo termine su tarea.

**Comparación entre `std::atomic` y `std::mutex`** 

| **Característica** | **`std::atomic`** | **`std::mutex`** |
|----------------------|-------------------|------------------|
| Tipo de sincronización | No bloqueante (*lock-free* en la mayoría de los casos) | Bloqueante (requiere adquirir y liberar el candado) |
| Costo de ejecución | Bajo (usa instrucciones atómicas del CPU) | Alto (implica cambio de contexto entre hilos) |
| Uso recomendado | Operaciones simples sobre variables individuales (contadores, flags, punteros) | Secciones críticas más grandes o estructuras de datos complejas |
| Riesgo de deadlock | Ninguno | Posible si no se libera correctamente el bloqueo |
| Rendimiento | Alto, ideal para tareas concurrentes ligeras | Medio o bajo, depende del número de hilos y bloqueos |
| Complejidad de uso | Sencillo para operaciones básicas | Mayor complejidad, requiere cuidado con los bloqueos |
| Ejemplo típico | `std::atomic<int> counter{0}; counter++;` | `std::mutex mtx; std::lock_guard<std::mutex> lock(mtx); counter++;` |


## Preguntas sobre depuración de programas

### 1. ¿Qué diferencias existen entre un error de ejecución y un error lógico?

| **Tipo de error**     | **Descripción**                                                                 | **Ejemplo**                                      |
|-----------------------|----------------------------------------------------------------------------------|--------------------------------------------------|
| Ejecución (runtime) | Ocurre durante la ejecución y suele detener el programa o producir fallos (accesos inválidos a memoria, división por cero, punteros nulos). | Acceder a `arr[10]` cuando `arr` tiene 5 elementos. |
| Lógico            | El programa corre, pero entrega resultados incorrectos por errores de cálculo o de diseño. | Calcular un promedio dividiendo por el total equivocado. |

**Resumen:** los de ejecución impiden el funcionamiento normal; los lógicos permiten ejecutar, pero con resultados erróneos.

---

### 2. ¿Qué ventajas presenta AddressSanitizer frente a Valgrind?

| **Aspecto**     | **AddressSanitizer (ASan)**                                      | **Valgrind (Memcheck)**                       |
|-----------------|-------------------------------------------------------------------|-----------------------------------------------|
| Rendimiento | Penalización moderada (~2–3× más lento que native).              | Penalización alta (hasta ~20–50×).            |
| Uso         | Se activa al compilar: `-fsanitize=address`.                      | Se ejecuta con Valgrind: `valgrind ./prog`.   |
| Cobertura   | Overflows de heap/stack/global, use-after-free, red zones, etc.   | Errores de memoria y fugas muy exhaustivo.    |
| Integración | Ideal para CI/CD y depuración rápida en desarrollo.               | Ideal para análisis profundo puntuales.       |

**Conclusión:** ASan es más rápido y fácil de integrar en el día a día; Valgrind es más exhaustivo pero mucho más lento.

---

### 3. ¿Cómo afectan las herramientas de depuración el rendimiento del programa?

Las herramientas instrumentan accesos a memoria y sincronización, añaden comprobaciones y consumen más CPU/RAM, por lo que **ralentizan** la ejecución:

- **ASan:** ~2–3× más lento.  
- **TSan:** ~5–10× más lento.  
- **Valgrind/Helgrind:** ~20–50× más lento.

**Beneficio:** a cambio, detectan errores críticos (fugas, overflows, data races) que son difíciles de reproducir.

---

### 4. ¿Por qué se recomienda compilar con `-O0` durante la depuración?

- Desactiva optimizaciones del compilador entonces el binario se parece más al código fuente.
- Facilita el paso a paso y el mapeo línea–instrucción.
- Evita reordenamientos/eliminaciones de variables que confunden el depurado.

**Resumen:** `-O0` hace la depuración más predecible y precisa.

---

### 5. ¿Qué se aprende sobre la importancia de diagnosticar errores antes de liberar un programa?

- Aumenta estabilidad, seguridad y confiabilidad del software.
- Detecta fugas de memoria, data races y fallos lógicos antes de que afecten a usuarios.
- Reduce costes de soporte y mantenimiento.
- Fomenta buenas prácticas de pruebas, validación y documentación.

**Conclusión:** depurar con ASan/TSan/Valgrind antes de liberar es esencial para entregar software robusto y seguro.
