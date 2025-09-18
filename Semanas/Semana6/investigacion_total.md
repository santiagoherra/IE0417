# Investigación sobre Frontend
Estudiantes: 
- Luis Soto
- Santiago Herra 
- Josué M. Jiménez Ramírez


## 1. Introducción al desarrollo web

### ¿Qué es el desarrollo web?
El desarrollo web engloba todos los procesos de creación y mantenimiento de sitios web y aplicaciones web que se ejecutan sobre Internet. Incluye tanto la parte visible al usuario (interfaz, diseño, interactividad) como la parte invisible (servidor, bases de datos, lógica de negocio) [1].

### Diferencia entre frontend y backend
- **Frontend** (lado del cliente): todo lo que ve y con lo que interactúa el usuario en su navegador. Incluye la interfaz visual, la experiencia de usuario, estilos, animaciones, manejo de eventos, etc.
- **Backend** (lado del servidor): todo lo que ocurre tras bambalinas para que la aplicación funcione correctamente: lógica de negocio, gestión de datos, base de datos, autenticación, seguridad, APIs, etc [1].  

#### ¿Por qué se divide en frontend y backend?
- Para separar responsabilidades: una parte se enfoca en qué ve/usa el usuario, la otra en cómo se procesan los datos, se almacenan, se ejecuta la lógica interna [2].   
- Permite optimizar distintos aspectos: la parte frontend optimiza experiencias visuales, interactivas, tiempos de respuesta perceptibles; el backend optimiza rendimiento, seguridad, fiabilidad de servidores, bases de datos.  

#### Evolución del desarrollo web
1. **Páginas estáticas (Web 1.0)**  
   - Sitios donde cada página era un archivo HTML con contenido fijo, imágenes, enlaces [3].  

2. **Páginas dinámicas / Web 2.0**  
   - Inclusión de lógica del servidor para generar páginas “al vuelo” según datos (base de datos, variables de usuario, etc.) [4].  

3. **Aplicaciones modernas**  
   - **SPA (Single Page Application):** la aplicación carga una vez y luego solo cambia contenido dinámicamente, sin recargar toda la página.
   - **PWA (Progressive Web App):** aplicaciones web que se comportan como apps nativas en algunos aspectos: capacidad offline, notificaciones push, carga rápida, seguridad, instalación.  

#### Roles de frontend y backend
- El **frontend** “presenta” la aplicación: interfaz gráfica, interacción del usuario, validaciones del lado cliente, respuesta inmediata visual.  
- El **backend** “sostiene” la aplicación: procesos intensivos, lógica de negocio, persistencia de datos, seguridad, autenticación/autorización, APIs, etc.  

---
## 2. Frontend

### Tecnologías base: HTML, CSS, JavaScript

### ¿Qué es HTML?

- HTML (HyperText Markup Language) es el lenguaje de marcado estándar para documentos diseñados para ser mostrados en un navegador web. Define la **estructura** del contenido: encabezados, párrafos, listas, enlaces, imágenes, etc [5].  
- HTML permite semántica: etiquetas que no solo organizan visualmente, sino que comunican el tipo de contenido (por ejemplo `<header>`, `<nav>`, `<article>`) lo que ayuda con accesibilidad, SEO, dispositivos de asistencia [6].  
- También permite incrustar contenido multimedia (audio, video), formularios, links a otras páginas o recursos [7]. 

### ¿Qué es CSS?

- CSS (Cascading Style Sheets) es un lenguaje de hojas de estilo usado para describir la **presentación** de un documento HTML o XML. Esto incluye colores, tipografía, diseño de cajas (márgenes, relleno), disposiciones visuales, estilos para distintos medios (pantalla, impresión, etc.) [8].  
- CSS permite separar contenido (HTML) de presentación (cómo se ve). Esa separación permite mantener mejor el código, reusar estilos, hacer temas visuales distintos y adaptar la apariencia sin cambiar la estructura [9].  
- También soporta animaciones, transiciones, transformaciones, layouts responsivos (flexbox, grid), estilos adaptativos a distintos dispositivos (uso de media queries) [10].   

### ¿Qué es JavaScript?

- JavaScript es un lenguaje de programación interpretado (o compilado just-in-time) ampliamente usado para proporcionar **dinamismo** e interactividad en páginas web [11].  
- Con JS puedes modificar el contenido del DOM (Document Object Model) logrando añadir, eliminar o cambiar objetos, responder a eventos de usuario (clicks, movimientos del mouse, entradas de formulario), validar datos, controlar multimedia, animaciones, llamadas a servidores sin recargar la página (fetch, AJAX), etc [12]. 
- JavaScript funciona en el navegador del usuario, aunque también puede ejecutarse en otros entornos (por ejemplo, Node.js) para lógica de backend, procesamiento, etc [13].  

---

### ¿Cómo se complementan HTML, CSS, JavaScript?

| Componente | Rol principal | Complemento con los demás |
|------------|----------------|-----------------------------|
| **HTML** | Estructura y contenido: define qué elementos hay, su jerarquía, su semántica. | Sin HTML no hay contenido que estilizar ni con qué interactuar. Es la base. |
| **CSS** | Presentación visual: hace que el contenido estructurado por HTML se vea bien, con estilos, diseño, estética. | Aplica estilos sobre la estructura dada por HTML. También reacciona al DOM (modificado por JS) para cambios visuales. |
| **JavaScript** | Comportamiento e interactividad: actualizaciones dinámicas, responder eventos, lógica de usuario, animaciones, modificaciones del contenido y del estilo en respuesta a acciones. | Usa HTML como punto de partida (DOM), manipula el DOM generado, puede cambiar estilos definidos en CSS, puede insertar clases, estilos inline, etc. También puede cargar contenido nuevo que HTML por sí solo no hubiese tenido. |

---

### Ejemplo conceptual

- Imagina una página de formulario de contacto:
  1. **HTML** define los campos: `<form>`, `<input>`, `<textarea>`, `<button>`, etiquetas `<label>`, etc.  
  2. **CSS** define cómo se ven esos campos: colores, bordes, espaciado, tipografía, disposición (por ejemplo dos columnas si la pantalla es grande, una columna si es móvil), estilo hover en botones, etc.  
  3. **JavaScript** añade validaciones: si el usuario deja un campo vacío, muestra mensaje de error, impide enviar hasta que esté bien, quizá envía los datos mediante AJAX para no recargar la página, muestra animaciones o feedback visual.

---

### Beneficios de usarlos juntos

- Mejora la **experiencia de usuario**: páginas que no solo muestran contenido, sino que se ven bien y responden a lo que el usuario hace.  
- Mantenimiento más fácil: separar lógica, estructura y presentación hace que cada parte se pueda modificar sin afectar demasiado a las otras.  
- Adaptabilidad: diferentes dispositivos, distintos tamaños de pantalla, diferentes medios (pantalla vs impresión) son más fáciles de soportar.  
- Optimización: carga inicial más rápida si CSS separado, HTML ligero; JS cargado asincrónicamente; mejoras en rendimiento visual.  


---
## Frameworks modernos: React, Angular, Vue

### Qué aportan respecto al JavaScript puro

- **Componentes reutilizables**: Permiten dividir la interfaz en piezas independientes que se pueden reutilizar en diferentes partes de la aplicación. Esto reduce duplicación de código y mejora mantenimiento. Por ejemplo, en React se crean componentes que encapsulan lógica, estilos y estructura [13].   
- **Virtual DOM / renderizado eficiente**: React y Vue utilizan Virtual DOM para minimizar manipulaciones costosas del DOM real, solo actualizar lo que cambia. Esto mejora el rendimiento en aplicaciones con interfaces dinámicas [14].   
- **Arquitectura y organización**: Los frameworks ofrecen formas estructuradas de organizar el código — separaciones de componentes, gestión de estado, routing, ciclo de vida, etc. Esto facilita escalar la aplicación, trabajar en equipo y mantener el código. JavaScript puro puede volverse desordenado si se hace todo manualmente [14].  
- **Herramientas adicionales y ecosistema**: Los frameworks vienen con (o suelen tener) herramientas para testing, compilación, optimización, integración con backends, soporte para renderizado del lado servidor o isomórfico, etc. Esa infraestructura facilita que se puedan construir aplicaciones más complejas de forma más segura y mantenible [15].  

---

### Ejemplos de sitios que los utilizan

Aquí algunos ejemplos de sitios/apps reales que usan React, Angular o Vue:

- **Vue.js**: Alibaba, Nintendo, Adobe’s Behance, GitLab, BMW.  
- **Angular**: Netflix, Google, Microsoft, Samsung, Tesla.  
- **React**: Varias grandes plataformas usan React en su interfaz principal o en partes de sus sitios (por ejemplo, Facebook lo mantiene). Además, React es muy usado en SPAs, dashboards y grandes aplicaciones web [12].  

---


### Comparación breve entre ellos

| Característica            | React                                   | Angular                                 | Vue.js                                |
|----------------------------|------------------------------------------|-------------------------------------------|-----------------------------------------|
| Origen / Apoyo             | Creado por Facebook, comunidad muy activa | Desarrollado por Google, framework completo | Creado por Evan You y comunidad amplia |
| Filosofía / enfoque        | Librería-UI basada en componentes, Virtual DOM, foco en la vista       | Framework completo “todo-incluido”, con muchas funcionalidades integradas (routing, inyección de dependencias, etc.) | Framework progresivo, modular, fácil de integrar en proyectos existentes |
| Curva de aprendizaje       | Moderada. JSX, manejo del estado, ecosistema [12].           | Más pronunciada; muchas funcionalidades; estructura más rígida [13].             | Más suave; buena para empezar; sintaxis más simple comparativa [13].             |
| Rendimiento                | Muy buen rendimiento cuando se usan bien las optimizaciones; virtual DOM ayuda a minimizar actualizaciones innecesarias [14].      | Excelente en aplicaciones grandes si se usa bien, pero puede generar tamaños de bundle grandes y requerir optimización [15].          | Ligero, rápido, buen rendimiento; Vue 3 mejora muchas cosas y permite adoptar progresivamente [15].            |
| Flexibilidad / modularidad | Alta; puedes usar solo lo que necesitas del ecosistema.             | Menos flexible en algunos aspectos; muchas decisiones ya hechas por defecto.         | Muy flexible; puedes ir añadiendo partes de Vue según se necesite.              |
| Casos ideales              | SPAs, dashboards, apps con muchas interacciones y componentes reutilizables | Aplicaciones corporativas grandes, donde se requiere estructura, escalabilidad, equipo grande | Proyectos nuevos medianos, experimentos, apps donde se quiere equilibrio entre simplicidad y funcionalidad |

---
## 3. Backend

El backend se encarga de recibir, procesar, almacenar y enviar datos de manera confiable y eficiente (idealmente), implementando  las reglas del negocio que definen el comportamiento de la aplicación. 

Para desarrollar el back-end se requiere de hacer uso de diversos lenguajes de programación como Python, PHP, Javascript (por medio de Node Js), Ruby, Java, C# en conjunto con frameworks especializados en desarrollo web, los cuales se encargan de brindar estructuras y componentes para funciones del servidor, lo que permite seguridad, escalabilidad y la posibilidad de mantener más fácilemente las aplicaciones web. 

Es importante destacar que no existe un lenguaje de programación superior a los demás, el uso del lenguaje depende del caso de uso, la experiencia del equipo y los requerimientos del sistema. 

Además, cada lenguaje debe de ser acompañado por frameworks que permitan el desarrollo web utilizando el lenguaje.

### Javascript
Para utilizar Javascript en backend se requiere hacer uso de Node.js, el cual es un entorno de ejecución que permite ejecutar código de Javascript fuera del navegador. Es asincrónico y no bloqueante.

Es de gran utilidad ya que si el front-end está programado con Javascript, se puede desarrollar un proyecto completo utilizando únicamente Javascript como lenguaje de programación. 

Es el lenguaje en el que trabajan muchos start-ups ya que se puede contratar a un full stack developer en vez de uno enfocado en front end y otra persona en back end. 

Diversas compañías utilizan este lenguaje para desarrollar sus servicios. Ejemplos de estas son: Paypal, Netflix, LinkedIn, Uber.

Javascript suele ser utilizado en conjunto con diversos frameworks como Express.js, NestJS, Fastify, Koa.js

#### Express.js
- Brinda suficientes herramientas para construir servidores web y APIs sin forzar una arquitectura grande.
- Es relativamente sencillo y flexible (el programador define la estructura del proyecto)
- Es utilizado en startups, para prototipar y para generar microservicios.

#### NestJS
- Construido sobre Express o Fastify.
- Implementa una arquitectura modular forzosamente
- Resulta en un codebase más uniforme y sostenible a lo largo de equipos grandes de trabajo pero puede ser más complicado el aprender a utilizarlo. 
- Es utilizado en empresas de gran escala y arquitecturas de micorservicios.

#### Fastify
- Optimizado para manejar más solicitudes por segundo utilizando menos cantidad de recursos.
- Es un framework enfocado en la capa de comunicaciones para realizar transferencias de forma eficiente.
- En aplicaciones grandes/complejas se utiliza con otros frameworks y se utiliza fastify para manejar el área de comunicaciones.
- Es bueno cuando se construyen APIs con tráfico alto de solicitudes o para microservicios.

#### Koa.js
- Más sencillo y menos pesado que Express, creado por el mismo equipo que creó Express.js
- Utiliza async/wait, lo que dice hacer el código más legible y claro que utilizar callbacks.
- Posee menos funcionalidades.
- Utilizado en proyectos en donde se requiere de una alternativa más ligera que Express.

### Python 
Python es de gran utilidad cuando el back-end debe de interactuar con procesamiento de datos masivo o complejo como analíticas o interactuar con modelos relacionados a aprendizaje de máquina. 

Algunas de las compañías que utilizan Python para desarrollar sus servicios son: Instagram, Netflix (algoritmo de recomendación), Spotify (recomendaciones de música nueva).

Para desarrollar proyectos web de Python se requiere el uso de diferentes frameworks como Django, Flask y FastAPI.

#### Django
- Usualmente se le describe como un "batteries included" framework porque contiene casi que todo lo necesario para desarrollar una aplicación web. 
- Incluye un ORM (Object-Relational Mapper) propio, que permite utilizar clases de Python para generar tablas de bases de datos.
- Brinda gran cantidad de funciones como URL routing, validación y manejo de "forms", manejo de usuarios y autenticación, un dashboard para administradores para manejar datos y está áltamente enfocado en seguridad.
- El usuario debe de seguir una estructura definida para desarrollar proyectos, por lo que es sencillo seguir la estructura de trabajo en equipos grandes.
- Los proyectos realizados con Django suelen ser escalables.
- Se puede escribir código asincrónico en la versión de Django 3.1 en adelante.
- Es de gran utilidad para desarrollos rápidos y si se desea utilizar las funcionalidades que ya trae predeterminadas.
- Compañías que han utilizado Django para desarrollar sus servicios son: Spotify, Instagram, Youtube.

#### Flask
- Es un framework de desarrollo web que proporciona funcionalidades mínimas para el desarrollo web.
- Toda función adicional como bases de datos, autenticación, manejo de forms; debe de ser agregado por el programador.
- Está construido sobre Werkzeug, que proporciona el funcionamiento de bajo nivel de HTTP. En conjunto con Jinja2, que permite generar documentos HTML con código de Python dentro de él.
- Es de gran utilidad para generar APIs sencillas y microservicios ya que es simple y ligero, además de aplicaciones en IoT. 
- Se pueden generar prototipos de manera eficiente por su simplicidad.
- Compañías como Netflix utilizan flask para crear APIs como parte de su arquitectura de microservicios.

#### FastAPI
- Es un web framework moderno para construir APIs con Python.
- Genera documentación automática.
- Tiene soporte para operaciones asincrónicas.
- Está construido sobre Starlette (comunicaciones) y Pydantic (para validación de información)
- Ideal para crear REST APIs, microservicios, APIs para modelos de aprendizaje de máquina.

### Java
Java es ampliamente utilizado en sectores en donde se requiere escalabilidad, estabilidad y mantenimiento a largo plazo. El lenguaje presenta la cualidad de ser "strong typed" (estricto al momento de declarar variables), lo que genera menos errores en runtime. 

Además, Java tiene un amplio soporte de librerías actualizadas que, en conjunto con su enfoque de programación orientada a objetos, brindan funcionalidades útiles en el desarrollo web escalable y mantenible. 

El código de Java es compilado a bytecode y se ejecuta en un Java Virtual Machine (JVM). Y, debido a su gran uso a lo largo de los años, es ampliamente usado por grandes empresas.

El frameowrk más utilizado en conjunto con Java para el desarrollo web principalmente es Spring / Spring Boot.

#### Spring / Spring Boot
- Spring Boot es una versión simplificada de Spring, lo que permite que el desarollo de proyectos sea más sencillo.
- Al utilizar Spring, se deben de realizar más configuraciones relacionadas al desarrollo web manualmente, mientras que Spring Boot realiza la configuración automáticamente.
- Ambos son áltamente integrables con diversos servicios como plataformas en la nube, diversas bases de datos.
- Spring existe desde alrededor desde el 2003 y ha demostrado ser una buena fuente de desarrollo web estable, por lo que muchas compañías lo siguen utilizando en conjunto con Java para desarrollar back-end en proyectos web.
- Requiere de una estructura fija, por lo que no es la principal opción para realizar prototipado. 
- Es útil para generar microservicios interconectados entre sí y en escenarios en los que se necesita robustez al momento de ejecución, como aplicaciones de pago. Sin embargo, presenta una curva de aprendizaje más compleja que otros lenguajes y frameworks.
- Es utilizada en la industria por diversas compañías, como por ejemplo, JPMorgan en su arquitectura de microservicios, Amazon en gran parte de sus operaciones e Ebay.


### C#
C# es un lenguaje orientado a objetos el cual se ejecute en el ambiente .NET (análogo al JVM de Java). El lenguaje de cierta forma se considera la versión de Java de Microsoft, el cual tiene una sintaxis similar. El framework más utilizado en conjunto con C# para desarrollo web es ASP.NET Core. 

#### ASP.NET Core
- Este framework es uno de los más veloces en los presentes para desarrollo web.
- Utiliza I/O asincrónico y presenta grandes optimizaciones que lo hacen ideal para un alto tráfico de APIs y servicios en tiempo real. 
- Tiene una gran integración con los productos existentes de Microsoft como Azure Cloud.
- También es considerado "strongly-typed", lo que promueve codigo estable y mantenible.
- Está diseñado para crear apliaciones web veloces y escalables.
- Puede tener una curva de aprendizaje superior a otros lenguajes como Python y Javascript, por lo que muchas veces no es utilizado para prototipado.
- Utilizado por compañías como Microsoft y Stack Overflow.


### PHP
Utilizado para generar páginas dinámicas de manera sencilla. El framework más utilizdo de PHP es Laravel. Fue creado en el año 1995 y fue uno de los primeros lenguajes creado con el propósito de crear páginas web.

El lenguaje suele ser utilizado en proyectos "sencillos" sin embargo también ha sido utilizado para desarrollar grandes proyectos como Facebook y WordPress. De hecho, al ser utilizado por WordPress aproximadamente el 40% de las páginas utilizan PHP debido a esto. En su totalidad, aprxoximadamente un 80% de las páginas web existentes en el internet en la actualidad utilizan PHP.

#### Laravel
- Existe para simplificar el uso de PHP al brindar funcionalidades de bajo nivel al programador. 
- Requiere un proyecto estructurado y brinda funcionalidades de seguridad, autenticación.

### Go (Golang)
Es un lenguaje compilado diseñado con la idea de combinar la simplicidad de Python, el rendimiento de C y un modelo de concurrencia necesitado para aplicaciones modernas en la nube.
Este lenguaje produce archivos binarios que no necesitan de un entorno virtual para ejecutarse como Java o C#. Fue diseñado con librerías con funcionalidades necesarias para generar el funcionamiento necesario del backend, sin embargo, existen frameworks que optimizan el desarrollo web como Gin y Fiber. 

Es de gran utilidad para el desarollo de APIs de gran rendimiento. Y además, es ideal para la creación de microservicios y el desarrollo de ambientes de contenedores. También es utilizado en flujos de trabajo de DevOps por su 

### Rust
Es un lenguaje enfocado en combinar el rendimiento de C utilizando manejo de memoria seguro y manejo de concurrencia seguro. En sistemas como C# se utiliza un sitema de "garbage collector" para limpiar memoria que no está siendo utilizada mientras el programa corre, lo que puede generar retardos. Rust utiliza una serie de reglas que el compilador debe checkear cuando compila el programa, si estas reglas no se cumplen el programa no compila del todo y estas reglas aseguran la liberación de memoria eficiente si un elemento en memoria no está siendo utilizada.

Puede ser utilizado en servicios de API para la nube y contenedores y en áreas de finanzas como blockchain.

En la industria es utilizado por diversas industrias como lo es AWS Firecracker y Kraken.

Frameworks utilizados con este lenguaje normalmente son Actix Web y Rocket.

#### Actix Web
- Presenta gran velocidad con respecto a otros web frameworks.
- Implementa un buen manejo de concurrencia.
- Utilizado para desarrollar microservicios y APIs de alto rendimiento

#### Rocket
- Tiene un desarrollo de estilo "batteries included".
- Enfocado en la facilidad de uso y la productividad del desarrollador.
- Utilizado por desarrolladores que están familiarizados con Flask/Django.

### Ruby
Es un lenguaje de programación de alto nivel dinámico de propósito general. Es utilizado en desarollo web en conjunto con el framework Ruby on Rails.

#### Ruby on Rails
- Normalmente es utilizado para prototipar y generar MVPs.
- Fue utilizado ampliamente por startups en años pasados.
- Presenta muchas facilidades para el programador.
- Sus aplicaciones normalmente son más lentas que las desarrolladas en Go, Java o inclusive en Node.js moderno.
- Su forma de escalabilidad no es óptima.
- Este framework puede consumir bastante memoria.
- En los últimos años su uso ha disminuido porque hay otras opciones de desarrollo más óptimas para la mayoría de casos.


## 4. Casos de uso del desarrollo web
En la actualidad un negocio sin presencia en la web está de facto en una posición de desventaja frente a la competencia que sí lo está. El desarrollo web está presente en la cotidianidad de la mayoría de personas, sean conscientes o no de ello. Ejemplo: Al despertar tomar tu celular e ingresas a "correo.ucr.ac.cr" para revisar la bandeja de entrada de correos. Por la tarde noche deciste visitar "Amazon.com" para comprar ese nuevo LEGO que tanto querías. 

Con el fin de comprender de manera más concreta cómo se aplica el desarrollo web en la práctica, a continuación se presentan algunos de sus principales casos de uso:

### 4.1. E-commerce

Según Hayes y Downie, el "e-commerce" se puede definir como: 

>Comercio electrónico, o e-commerce, es el proceso de comprar y vender bienes y servicios a través de Internet. Implica el intercambio de productos o servicios entre empresas, consumidores o ambos.

Conociendo lo anterior, un ejemplo claro de e-commerce es el gigante **Amazon.com**. Como parte del ejercico se desglosa a continuación y grandes rasgos cómo interactuan los siguientes elementos en dicho sitio web: 



- **Front-end:** 
 
  En Amazon, el frontend es todo lo que el usuario ve y con lo que interactúa desde su navegador. Esto incluye la interfaz gráfica del catálogo de productos, el buscador, los filtros, las reseñas, el carrito de compras y el sistema de pago. Está diseñado para ser intuitivo, atractivo y responsivo, de manera que funcione igual de bien en una computadora de escritorio, una tableta o un teléfono móvil. Detrás de esta experiencia visual se utilizan tecnologías como HTML, CSS y JavaScript, además de frameworks modernos que permiten que la interacción sea dinámica y que el sitio cargue rápidamente incluso cuando se manejan millones de productos.

- **Back-end:**
  
   El backend de Amazon se encarga de toda la lógica que el usuario no ve, pero que hace posible la experiencia de compra. Esto incluye la gestión del inventario, la autenticación de usuarios, la validación de pagos, la seguridad de las transacciones, la recomendación de productos mediante algoritmos, y la administración de una gigantesca base de datos con millones de artículos. Se apoya en lenguajes de programación como Java, Python o Node.js, junto con frameworks y arquitecturas distribuidas que garantizan que la plataforma se mantenga disponible y escalable, incluso en momentos de gran demanda como el “Black Friday” o el “Prime Day”.

En conjunto, tanto el frontend como el backend se coordinan para que el usuario final tenga una experiencia fluida: desde buscar un producto hasta recibir la confirmación de compra en su correo electrónico.

### 4.2. Redes Sociales

Según Paljug, las **redes sociales** pueden definirse como:  

> Las redes sociales son una forma de comunicación digital que permite a los usuarios formar redes y comunidades en línea para socializar, compartir información y publicar contenido creado por los propios usuarios.

Conociendo lo anterior, un ejemplo claro de red social es **Facebook**. Como parte del ejercicio, se desglosa a continuación y a grandes rasgos cómo interactúan los siguientes elementos en dicha plataforma:  

- **Front-end:**  

  En Facebook, el frontend corresponde a todo lo que el usuario ve y con lo que interactúa desde la aplicación o el navegador. Esto incluye el muro de publicaciones, los comentarios, los mensajes privados, las notificaciones, las historias y las transmisiones en vivo. Está diseñado para ser altamente interactivo, responsivo y atractivo visualmente, con el fin de mantener la atención del usuario. Para lograrlo, se emplean tecnologías como HTML, CSS y JavaScript, junto con frameworks modernos como React, que permiten actualizaciones en tiempo real y una experiencia fluida incluso cuando millones de personas están conectadas simultáneamente.

- **Back-end:**  

  El backend de Facebook es el responsable de la lógica y la gestión de datos detrás de la plataforma. Se encarga de almacenar y procesar las publicaciones, administrar las relaciones entre amigos, validar la autenticación de usuarios, manejar las recomendaciones de contenido mediante algoritmos de inteligencia artificial y garantizar la seguridad en el intercambio de información. Este backend utiliza lenguajes como PHP (con extensas optimizaciones internas), Python y C++, así como bases de datos distribuidas y sistemas de caché que permiten ofrecer contenido en fracciones de segundo a escala global.

En conjunto, tanto el frontend como el backend de Facebook se coordinan para brindar al usuario una experiencia en tiempo real: desde publicar una foto hasta recibir una reacción instantánea de sus amigos alrededor del mundo.


## 5. Retos en el Desarrollo Web
El desarrollo web está en continua evolución, con lo cual los proyectos deben tomar en cuenta los siguientes retos con el fin de desplegar el mejor producto posible: 


### 5.1. Escalabilidad
- Una aplicación puede iniciar con pocos usuarios, pero debe estar preparada para crecer y atender miles o incluso millones de conexiones simultáneas.
- Esto exige estrategias como balanceadores de carga, bases de datos distribuidas y arquitecturas de microservicios.
- Ejemplo: Amazon debe mantener operaciones fluidas incluso en eventos de alto tráfico como el Black Friday.

### 5.2. Seguridad
- La protección de los datos de los usuarios es fundamental.
- Se deben prevenir vulnerabilidades como:
  - **SQL Injection** (ataques a la base de datos)
  - **XSS (Cross-Site Scripting)**, que afecta al frontend inyectando código malicioso
  - **Robo de sesiones**, que puede comprometer cuentas de usuarios
- Es crucial aplicar cifrado en las comunicaciones (HTTPS) y en la gestión de contraseñas.

### 5.3. Experiencia de usuario (UX)
- Un sitio web debe ser rápido, intuitivo y accesible desde distintos dispositivos.
- Si una página tarda demasiado en cargar o su diseño no es responsivo, el usuario puede abandonarla rápidamente.
- La UX es clave en aplicaciones como Netflix o Spotify, donde la simplicidad y fluidez son parte de la propuesta de valor.

### 5.4. Mantenimiento y evolución
- Una aplicación web no es un producto estático, sino un servicio en constante cambio.
- Los equipos deben garantizar actualizaciones periódicas sin afectar la estabilidad del sistema.
- Buenas prácticas incluyen versionado, documentación y pruebas automatizadas.

### 5.5. Integración con servicios externos
- La mayoría de aplicaciones modernas dependen de APIs o servicios de terceros:
  - Pasarelas de pago (Stripe, PayPal)
  - Sistemas de autenticación (Google, Facebook, GitHub)
  - Mapas (Google Maps) o servicios de mensajería
- Integrarlos correctamente es esencial, pero puede representar un reto en términos de compatibilidad y seguridad.

## 6. Áreas laborales

### Front-end
Una de las áreas laborales en las que se puede desarrollar una persona interesada en el desarrollo de software es el front-end. Esta área como se ha mencionado anteriormente hace referencia a lo que el usuario observa. 

Muchas compañías desean brindar un producto con un UX/UI llamativo e interactivo que retenga a los usuarios, ya que esto está áltamente ligado con la experiencia del usuario.
Normalmente son contratados en compañías en donde se requiere que el ingeniero se dedique completamente al desarrollo de interacción entre la aplicación y el usuario.

### Back-end
Con respecto al back-end, la persona dedicada a desarrollar back-end en la industria se encarga de desarrollar y mantener sistemas que alimentan aplicaciones web.
Esta persona no diseña interfaz de usuario, sino que se asegura que la transmisión de datos se da correctamente y que el sistema funcione bajo las especificaciones deseadas del cliente.
Un desarrollador en back-end suele utilizar el lenguaje de programación utilizado en conjunto con los frameworks necesitados para desarrollar soporte a las acciones del servidor que interactúa con el cliente. 
Son necesitados en proyectos en donde se requiera de escalabilidad.

### Full-stack
Se encarga de realizar las labores del front-end y el back-end al mismo tiempo.
Son normalmente solicitados en puestos de trabajo relacionados a start-ups debido a que se puede contratar únicamente a una persona para el desarrollo de la aplicación web. 
Una persona que realice desarrollo de full-stack se puede encargar de generar cambios en la interfaz gráfica y asegurarse que se integre de manera correcta con el servidor.
Muchas agencias de consultoría utilizan full stack ya que deben poder brindar apoyo a miembros del equipo en front-end y back-end.
En compañías grandes suele no ser tan común el uso de full-stack ya que se buscan personas especializadas en diversos sectores del desarrollo web. 



## 7. Actividad sugerida: Comparacion de tecnologias
### Kahoot



## Referencias

[11] Asynclabs, “Vanilla JavaScript vs React: Choosing the Right Tool for Web Development,” 5-Sep-2023. [En línea]. Disponible: https://www.asynclabs.co/blog/software-development/vanilla-javascript-vs-react-choosing-the-right-tool-for-web-development

[4] CIS Informática, “Evolución de las páginas web,” [En línea]. Disponible: https://www.cisinformatica.cat/es/evolucion-de-las-paginas-web/

[16] Computools, “Examples of Global Websites Using Vue.js,” [En línea]. Disponible: https://computools.com/global-websites-using-vue-js

[27] Express.js. (s. f.). Express – Node.js web application framework. Disponible en https://expressjs.com/

[29] Fastify. (s. f.). Fastify Framework. Disponible en https://fastify.dev/

[22] GeeksforGeeks. (2024, abril 18). Comparison of FastAPI with Django and Flask. Disponible en https://www.geeksforgeeks.org/python/comparison-of-fastapi-with-django-and-flask/

[28] GeeksforGeeks. (2025, 23 de julio). ExpressJS vs NestJS - 7 Differences That You Should Know. Recuperado de https://www.geeksforgeeks.org/blogs/expressjs-vs-nestjs-5-differences-that-you-should-know/

[25] Go Project. (2019, 4 de octubre). Go for Web Development. Recuperado de https://go.dev/solutions/webdev

[26] Khouloud Haddad Amamou. (2024). Is PHP Still a Language Worth Learning as We Head Into 2025? Medium. Disponible en https://medium.com/@khouloud.haddad/is-php-still-a-language-worth-learning-as-we-head-into-2025-566c630cb699

[15] Pangea.ai, “Biggest Companies Keeping Angular Popular,” 18-Nov-2024. [En línea]. Disponible: https://pangea.ai/resources/biggest-companies-keeping-angular-popular

[12] Pulsion, “React vs. JavaScript: Which Framework Suits Your Mobile ...,” 10-Jul-2024. [En línea]. Disponible: https://www.pulsion.co.uk/blog/react-vs-javascript/

[23] Pratik T. (2025, 1 de marzo). Spring vs. Spring Boot: Understanding the Key Differences with Examples. Medium. Disponible en https://medium.com/@pratik.941/spring-vs-spring-boot-understanding-the-key-differences-with-examples-aff8f27d243d

[13] Monterail, “Top 15 Inspiring Companies Using Vue.js in 2024,” 13-Dec-2024. [En línea]. Disponible: https://www.monterail.com/blog/top-companies-using-vue-js

[21] Microsoft. (2025, julio 30). Descripción general de ASP.NET Core. Disponible en https://learn.microsoft.com/en-us/aspnet/core/overview?view=aspnetcore-9.0

[6] Mozilla Developer Network, "CSS: Styling the content," MDN Web Docs. [En línea]. Disponible: https://developer.mozilla.org/en-US/docs/Learn/web_development/Core/Styling_basics/What_is_CSS

[7] Mozilla Developer Network, "What is JavaScript?," MDN Web Docs. [En línea]. Disponible: https://developer.mozilla.org/en-US/docs/Learn/web_development/Core/Scripting/What_is_JavaScript

[5] Mozilla Developer Network, "What is HTML? Creating the content," MDN Web Docs, 24-Jun-2025. [En línea]. Disponible: https://developer.mozilla.org/en-US/docs/Learn/web_development/Getting_started/Your_first_website/Creating_the_content

[3] Wix, “La evolución de la web: de Web 1.0 a Web 3.0,” [En línea]. Disponible: https://es.wix.com/blog/evolucion-de-la-web

[17] M. Hayes and A. Downie, “What is e-commerce?”, Think · IBM, 29 Feb. 2024, updated 18 Apr. 2025. [En línea]. Disponible: https://www.ibm.com/think/topics/ecommerce

[18] K. Paljug, “Social media: Definition, importance, top websites, and apps,” Investopedia, 14 Sep. 2024. [En línea]. Disponible en: https://www.investopedia.com/terms/s/social-media.asp

[19] L. Brown, “Exploring the software behind Facebook, the world’s largest social media site,” Pingdom, 7 feb. 2023. [En línea]. Disponible en: https://www.pingdom.com/blog/the-software-behind-facebook/
 . [Accedido: 17 sep. 2025].

[30] Linz. (2024). Koa.js: A Clean and Modern Web Framework for Node.js. Medium. Disponible en https://medium.com/@linz07m/koa-js-a-clean-and-modern-web-framework-for-node-js-efa72ed9e233

[1] Owius, “Diferencias entre desarrolladores web frontend y backend: guía,” [En línea]. Disponible: https://owius.com/diferencias-entre-desarrolladores-web-frontend-y-backend-guia/

[24] Sophia Smith. (2024, 21 de junio). What Couldn’t You Do with Ruby on Rails? Medium. Disponible en https://medium.com/@sophiasmith791/what-couldnt-you-do-with-ruby-on-rails-1b26a6845e01

[31] Stack Overflow. (2025). 2025 Stack Overflow Developer Survey. Disponible en https://survey.stackoverflow.co/2025/developers

[8] Tadabase, "HTML, CSS, & JavaScript Explained with Analogies," Tadabase Blog, 12-Nov-2024. [En línea]. Disponible: https://tadabase.io/blog/html-css-javascript-explained

[14] Trio.dev, “Top 15 Real-World Websites Using Vue.js in 2025,” 2-May-2025. [En línea]. Disponible: https://trio.dev/websites-using-vue/

[20] Turing.com, “Top web development challenges,” Turing.com, 19 feb. 2025. [En línea]. Disponible en: https://www.turing.com/resources/top-web-development-challenges
 . [Accedido: 17 sep. 2025].

[32] Wales, M. (2020, 8 de diciembre). 3 Web Dev Careers Decoded: Front-End vs Back-End vs Full Stack. Udacity. Disponible en https://www.udacity.com/blog/2020/12/front-end-vs-back-end-vs-full-stack-web-developers.html

[9] Wikipedia, "CSS," [En línea]. Disponible: https://es.wikipedia.org/wiki/CSS

[10] Wikipedia, "HTML," Living Standard, WHATWG. [En línea]. Disponible: https://html.spec.whatwg.org/





