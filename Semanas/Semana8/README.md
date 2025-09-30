# Contenedores

### ¿Qué es un contenedor?
- Un contenedor es una unidad estándar de software que empaqueta el código y todas sus dependencias para que la aplicación se ejecute rápidamente y de manera confiable de un entorno informático a otro.
- Azure ofrece recursos en la nube, incluyendo planes con hasta 2 millones de requests por mes para hospedar contenedores y servicios.

## Contenedores vs máquinas virtuales

| Característica                | Contenedores                                  | Máquinas Virtuales                             |
|------------------------------|----------------------------------------------|------------------------------------------------|
| Sistema operativo             | Comparten el kernel del SO del host          | Cada VM tiene su propio sistema operativo      |
| Tamaño                       | Más ligeros (MBs)                             | Más pesadas (GBs)                              |
| Tiempo de arranque            | Muy rápido (segundos)                         | Más lento (minutos)                            |
| Aislamiento                   | Aislamiento a nivel de proceso y sistema de archivos | Aislamiento completo con hardware virtualizado |
| Uso de recursos              | Menor consumo de CPU y memoria                | Mayor consumo debido a SO completo              |
| Caso de uso                  | Microservicios, despliegue rápido             | Aplicaciones legadas, entornos con requerimientos de SO completo |

### Máquinas virtuales
- Una máquina virtual (VM) emula un sistema informático completo, incluyendo hardware virtualizado.
- Se ejecuta sobre un hipervisor (como Hyper-V, VMware o KVM).
- Son ideales para aplicaciones que requieren un sistema operativo completo y aislamiento fuerte.

### ¿Qué es Docker?
- Docker es una plataforma que permite crear, desplegar y gestionar contenedores.
- **Docker Daemon**: Servicio que corre en segundo plano y gestiona la creación, ejecución y monitoreo de contenedores e imágenes. Facilita la comunicación entre contenedores, imágenes y el host.
- Docker utiliza un motor de contenedores que permite empaquetar aplicaciones con todo lo necesario para funcionar (código, runtime, bibliotecas).

### ¿Qué es un Dockerfile?
- Es un archivo de texto que contiene una serie de instrucciones que Docker utiliza para construir una imagen.
- Permite definir desde la base del sistema operativo hasta las dependencias, comandos y configuración necesaria para la aplicación.
- Ejemplo básico de Dockerfile:

- Cada instrucción genera una nueva capa en la imagen, lo que permite reutilización y optimización.

### Comandos de Docker:
- `docker run`: Crea y ejecuta un nuevo contenedor a partir de una imagen.
- `docker start`: Inicia un contenedor que está detenido.
- `docker stop`: Detiene un contenedor en ejecución.
- `docker ps`: Lista los contenedores en ejecución.
- `docker images`: Lista las imágenes disponibles localmente.
- `docker build`: Construye una imagen desde un Dockerfile.
- `docker exec`: Ejecuta un comando dentro de un contenedor en ejecución.

### Volúmenes, redes y persistencia en Docker
- **Volúmenes**: Permiten almacenar datos de forma persistente, independiente del ciclo de vida del contenedor. Son gestionados por Docker y almacenados fuera del sistema de archivos del contenedor.
- Crear un volumen:
  ```
  docker volume create mi-volumen
  ```
- Montar volumen en contenedor:
  ```
  docker run -v mi-volumen:/data myimage
  ```
- **Redes en Docker**:
- `bridge`: Red por defecto, conecta contenedores en una red privada aislada.
- `host`: El contenedor comparte la red con el host, sin aislamiento.
- `none`: Contenedor sin red.
- Permiten comunicación entre contenedores y con el exterior según la configuración.

### Buenas prácticas al usar Docker
- Mantener imágenes ligeras y específicas.
- Usar `.dockerignore` para evitar copiar archivos innecesarios.
- Ejecutar `docker system prune` regularmente para eliminar recursos no utilizados (contenedores, imágenes, volúmenes, redes).
- Etiquetar imágenes con versiones claras (`tags`).
- Separar la construcción en etapas (multi-stage builds) para optimizar tamaño de la imagen.
- No ejecutar contenedores con permisos de root si no es necesario.

### Kubernetes (K8s)
- Plataforma de orquestación de contenedores que automatiza el despliegue, escalado y gestión de aplicaciones en contenedores.
- Permite administrar clusters de máquinas físicas o virtuales, ejecutando aplicaciones en contenedores de forma resiliente.
- Facilita la distribución de carga, auto-recuperación, despliegue continuo y escalado automático.

### Objetos fundamentales en Kubernetes
- **Pod**: Unidad básica de ejecución, puede contener uno o varios contenedores que comparten red y almacenamiento.
- **ReplicaSet**: Garantiza que un número especificado de Pods idénticos estén corriendo.
- **Service**: Abstracción que define un conjunto lógico de Pods y la política para acceder a ellos.
- Otros objetos importantes:
- **Deployment**: Controla la creación y actualización de ReplicaSets.
- **ConfigMap** y **Secret**: Manejan configuración y datos sensibles respectivamente.
- **Namespace**: Permite dividir recursos en grupos lógicos.

### Containerd
- Runtime de contenedores diseñado para ser simple, robusto y eficiente.
- Administra el ciclo de vida de los contenedores: descarga imágenes, ejecución, supervisión y almacenamiento.
- Utilizado por Docker como runtime subyacente y también integrado en Kubernetes para ejecutar contenedores.
- Está enfocado en ser un componente modular y ligero para entornos de producción.
