# Laboratorio de Programacion Paralela y Concurrente
Santiago Herra Castro - Prof. Esteban Badilla - Curso: Diseño de Software
---
## Fundamentos practicos de concurrencia

El programa crea cuatro hilos que ejecutan una misma función llamada tarea. Cada hilo recibe un número identificador y ejecuta un bucle que imprime su id junto con el número de iteración actual. Entre cada impresión, el hilo se detiene durante 200 milisegundos mediante la función sleep_for, lo que simula una pausa o trabajo en progreso. Mientras tanto, los otros hilos pueden ejecutarse en paralelo. El hilo principal crea los cuatro hilos y luego llama a join en cada uno para asegurarse de que todos terminen antes de imprimir el mensaje de finalización. La salida generada refleja la ejecución concurrente de los hilos.

![resultado de la ejecución](./salida_ejecucion.png)

### Patrón de ejecución observado

El patrón observado en la salida es intercalado y no determinista. Esto significa que las líneas impresas por los diferentes hilos aparecen mezcladas y el orden puede variar cada vez que se ejecuta el programa. Esta variabilidad ocurre porque el sistema operativo decide qué hilo ejecutar en cada instante, distribuyendo el tiempo de CPU entre ellos. La llamada a sleep introduce pausas uniformes dentro de cada hilo, pero no sincroniza los hilos entre sí. La única secuencia garantizada es que el mensaje final de ejecución aparece al final, cuando todos los hilos han completado su trabajo.

### Control del orden de ejecución

Existen formas de controlar el orden sin modificar la lógica principal de la función tarea.  
1. Ejecutar y unir cada hilo de forma secuencial, creando un hilo, esperando a que termine con join y luego lanzando el siguiente. Este método asegura un orden predecible pero elimina la ejecución concurrente.  
2. Usar mecanismos de sincronización como condition_variable o semáforos para permitir que un hilo ejecute su parte solo cuando sea su turno, manteniendo la concurrencia pero coordinando el orden de impresión.  
3. Si el objetivo es únicamente evitar que las salidas se mezclen, se puede proteger la escritura en consola con un mutex, lo que hace que las líneas se impriman completas pero en un orden determinado por el planificador.

## Sincronizacion y exclusion mutua

## Variables de condicion (modelo productor-consumidor)

### Se elimina el cv_productor.wait

Si se elimina la llamada a  
cv_productor.wait(lock, [] { return buffer.size() < BUFFER_SIZE; });  
el productor dejaría de verificar si el búfer tiene espacio disponible antes de insertar una nueva tarea.  
Esto causaría que todos los productores continúen generando tareas sin detenerse, llenando el búfer sin límite. Como consecuencia:

- El búfer (std::queue<int> buffer) crecería indefinidamente, provocando un uso excesivo de memoria.  
- Se perdería la sincronización entre productores y consumidores, ya que los consumidores podrían quedarse atrás en el procesamiento.  
- El objetivo de mantener un tamaño máximo del búfer (BUFFER_SIZE = 5) se rompería completamente.  

## ¿Por qué se usa unique_lock y no lock_guard en este caso?

Se usa std::unique_lock<std::mutex> en lugar de std::lock_guard<std::mutex> porque unique_lock permite bloquear y desbloquear el mutex de manera flexible y es compatible con las variables de condición.

En particular:
- cv_productor.wait(lock, ...) y cv_consumidor.wait(lock, ...) necesitan un unique_lock, ya que la función wait libera automáticamente el mutex mientras el hilo está dormido y lo vuelve a bloquear cuando se despierta.  
- lock_guard no permite ese comportamiento; su diseño es más simple y el mutex permanece bloqueado hasta que el objeto sale de alcance.  

Por tanto, el unique_lock es necesario cuando se usa una condition_variable, ya que proporciona control dinámico del bloqueo y permite coordinar la espera y reanudación de los hilos.

## ¿Qué garantiza cv_consumidor.notify_all()?

La instrucción  
cv_consumidor.notify_all();  
sirve para despertar a todos los hilos consumidores que estén esperando en la condición:  
cv_consumidor.wait(lock, [] { return !buffer.empty() || done; });  

Esto garantiza que, una vez que un productor ha insertado una tarea en el búfer, los consumidores sean notificados de que hay trabajo disponible.  
De esta forma:
- Si el búfer estaba vacío, los consumidores bloqueados se reactivan para procesar las nuevas tareas.  
- También se usa al final del programa para notificar a los consumidores de que el proceso ha terminado (done = true), permitiendo que salgan del bucle while y finalicen correctamente.

## Mecanismos avanzados y analisis de rendimiento

Se realizo el programa pool_conections.cpp para poder emplear el uso de semaforos y barreras, donde los hilos son manejados por un semaforos en un vector hasta llegar a una barrera donde todos esperan hasta que lleguen todos. En el comando de compilacion se le debe agregar como bandera -std=c++20 -pthreads, para especificar la version del compilador.


