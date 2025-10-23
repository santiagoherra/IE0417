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

1) ¿Qué tipo de error genera el fallo de ejecución?

El acceso datos.at(4) provoca una excepción de tiempo de ejecución del tipo std::out_of_range. Si no es capturada, el programa terminará con una señal SIGABRT por excepción no manejada.

2) ¿Qué comando permite identificar la línea exacta donde ocurre el fallo?

Tras ejecutar con gdb y reproducir el fallo:

Usa where o bt para ver la traza de pila; el frame 0 indica la línea exacta.

Usa list para ver el código alrededor de esa línea.

Si hace falta, frame 0 para seleccionar el marco superior.

Secuencia típica:

(gdb) start              # o: break main; run
... reproducir el fallo ...
(gdb) where              # o: bt
(gdb) list

3) ¿Qué diferencia existe entre los comandos next y step en gdb?

next (n) ejecuta la siguiente línea de código y salta por encima de las llamadas a funciones, deteniéndose en la siguiente línea del llamador.

step (s) ejecuta la siguiente línea y, si hay una llamada a función, entra en esa función y se detiene en su primera línea.