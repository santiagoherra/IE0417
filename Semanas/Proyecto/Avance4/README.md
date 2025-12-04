# 📘 Informe Final – Chatbot Basado en Flujos de Decisión para el Soporte Informativo en EIE Info

### **Semana 4 - Validación, Evaluación Crítica y Cierre del Proyecto**
II-2025

**Proyecto:** Chatbot Basado en Flujos de Decisión para el Soporte Informativo en EIE Info
**Estudiantes:**

* Josué María Jiménez Ramírez — C13987
* Santiago Herra Castro — C13721

---

# Cómo probar el Chatbot

Para probar el charbot debe seguir los siguientes pasos: 

## Paso 1. Descargar repositorio y dirigirse a la rama correcta 
Abra la terminar de Linux/WSL y ejecute los siguientes comandos: 

```bash
# Clonar repositorio
git clone https://git.ucr.ac.cr/eieinfo/EIEInfo.git

# Digirse al directorio del repositorio descargado
cd EIEInfo

# Cambiar a la rama del chatbot
git switch "feature/chatbot"

```

## Paso 2. Crear imagen y levantar contenedor



```bash
# Dirigirse a directorio de contenedor
cd docker

sudo su
apt update
apt install -y ca-certificates curl gnupg apt-transport-https lsb-release

curl -fsSL https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]')/gpg | gpg --dearmor -o /usr/share/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker.gpg] \
https://download.docker.com/linux/$(lsb_release -is | tr '[:upper:]' '[:lower:]') \
$(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list

apt update
apt install -y docker-ce docker-ce-cli containerd.io \
               docker-buildx-plugin docker-compose-plugin

# Habilitar y arrancar servicio
systemctl enable --now docker
exit  # Volver al usuario normal

# Compilar imágenes personalizadas (django, nginx, mariadb)
$ sudo docker compose build

# Iniciar en modo interactivo (logs en consola)
$ sudo docker compose up

```

## Paso 3. Ejecución del chatbot

En el directorio EIEInfo ejecute el siguiente comando para abrir el directorio en VSCode: 

```bash
# Dirigirse al directorio madre
cd EIEInfo

# Abrir directorio en VSCode
code .
```
### Paso 3.1
Descargue la siguiente extensión en su VSCode: 

![Extensión de Remote Explorer](images/Remote_Explorer_Extension.png)

Ahora con la extensión instalada diríjase al nuevo ícono correspondiente y abra el contenedor. Luego abra la consola del contenedor, esta será de utilidad para ejecutar unos comandos más adelante.

### Paso 3.2

Instalación y Configuración del Chatbot en Django
Pasos para Ejecutar la Aplicación del Chatbot
1. Copiar la Carpeta del Chatbot
Copie la carpeta llamada chatbot en la carpeta src/server/ del proyecto Django.

La estructura debería quedar así:

```text
src/
├── server/
│   ├── chatbot/          ← Carpeta copiada aquí
│   ├── eieinfo/
│   ├── manage.py
│   └── ...
```

2. Configurar settings.py
En el módulo eieinfo, específicamente en el archivo settings.py, agregue la siguiente configuración en la sección INSTALLED_APPS:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ... otras apps ...
    'chatbot.apps.ChatbotConfig',  # ← Agregar esta línea
]
```

Nota importante: Verifique que el nombre de la clase en el archivo apps.py de la carpeta chatbot sea exactamente ChatbotConfig.

3. Configurar URLs
En el archivo urls.py del módulo principal (generalmente eieinfo/urls.py), agregue la ruta para la comunicación frontend-backend:

```python
urlpatterns = [
    repath(r'^chatbot/', include('chatbot.urls')),
    # Puede agregar más rutas según sea necesario
]
```


4. Incluir en las Plantillas HTML
En cada página HTML donde desee mostrar el chatbot, agregue el siguiente código en la sección donde quiera que aparezca:

```html
<!-- En la ubicación deseada para el chatbot -->
    {% include 'chatbot/index.html' %}
```

5. Verificar la Configuración
Antes de ejecutar el servidor, verifique que:

- La estructura de carpetas sea correcta

- Todas las configuraciones estén guardadas correctamente

- Las dependencias del chatbot estén instaladas en el entorno virtual

6. Ejecutar el Servidor
Abra la terminal del contenedor y siga estos pasos para ejecutar la aplicación:
```bash
# Navegar al directorio del proyecto
cd src/server

# Ejecutar las migraciones
python manage.py migrations.sh


# Ejecutar el servidor de desarrollo
python manage.py runserver 0.0.0.0:8005
```

7. Acceder al Chatbot
Una vez que el servidor esté ejecutándose correctamente:

El backend de la API estará disponible en: http://localhost:8000/chatbot/query

Las páginas que incluyan el chatbot mostrarán la interfaz de usuario correspondiente.


# 1. Pruebas Formales

## 1.1 Matriz de Pruebas

| ID    | Caso de Prueba                   | Pasos Ejecutados                                                                                                                     | Resultado Esperado                                                         | Resultado Obtenido                                                         | Estado   |
| ----- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------- |
| CP-01 | Carga del nodo raíz              | 1. Abrir widget<br>2. Enviar solicitud a `root`                                                                                      | El menú principal se renderiza correctamente                               | El menú principal cargó de la manera esperada.                             | Aprobado |
| CP-02 | Navegación hacia Planes          | 1. Seleccionar la opción de planes<br>2. Seleccionar uno de los planes                                                               | Se envía y despliega el plan de estudio correcto                           | Se envía y despliega el plan de estudio correcto                           | Aprobado |
| CP-03 | Consulta dinámica de asistencias | 1. Seleccionar la opción "Asistencias disponibles"<br>2. Se despliegan los tipos de asistencia<br>3. Seleccionar una de las opciones | Se realiza una consulta ORM y se despliega la información de la asistencia | Se realiza una consulta ORM y se despliega la información de la asistencia | Aprobado |
| CP-04 | Consultar proyectos eléctricos   | 1. Seleccionar la opción “Proyectos Eléctricos”<br>            | Se despliega correctamente la lista de proyectos eléctricos disponibles    | La lista de proyectos eléctricos se desplegó correctamente                 | Aprobado |
| CP-05 | Trámites de práctica laboral     | 1. Seleccionar “Práctica Laboral”<br>2. Seleccioanr opción                              | Se despliegan correctamente los trámites y requisitos de práctica laboral  | Los trámites y requisitos se desplegaron correctamente                     | Aprobado |
| CP-06 | Trámites de graduación           | 1. Seleccionar “Trámites de Graduación”<br>2. Seleccionar una opción de información                         | Se despliega correctamente la información de los trámites de graduación    | La información de los trámites de graduación se desplegó correctamente     | Aprobado |


---

## 1.2 Correcciones Finales Realizadas
Durante la fase final se aplicaron varias correcciones de calidad y seguridad para estabilizar el módulo y facilitar su despliegue:

- **Ajuste en validación de nodos:** Se añadieron comprobaciones más estrictas durante la construcción y la consulta del árbol para evitar referencias a nodos inexistentes o mal formados. Esto incluye fallback seguros al nodo `root` cuando la entrada no es válida.

- **Manejo seguro de documentos públicos:** Se revisó la forma en que los `DocumentNode` exponen rutas a PDFs. Si bien los documentos siguen siendo accesibles públicamente, se normalizó la ruta y se implementaron prácticas para prevenir path traversal y enlaces rotos en producción.

- **Normalización y consistencia de textos:** Se estandarizaron cadenas y se añadió sanitización básica para evitar problemas de encoding o caracteres especiales que rompan la presentación en el widget.

- **Optimización del endpoint `/chatbot/query/`:** Se redujo la sobrecarga de la vista evitando reconstrucciones repetidas del árbol y minimizando el trabajo en cada petición (now cached in `ChatbotConfig`). También se mejoró el manejo de errores para que el cliente reciba mensajes amigables sin exponer trazas internas.

- **Pruebas unitarias ampliadas:** Se agregaron casos de prueba para `DynamicNode` y para el comportamiento de fallback al solicitar nodos inexistentes.


# 2. Evaluación Crítica del Impacto

## 2.1 Problema que Resuelve

El chatbot reduce la necesidad de navegar por múltiples menús, elimina el requisito de autenticación para acceder a información pública y centraliza en un solo punto el acceso a planes de estudio, asistencias, proyectos y trámites. Esto mejora la accesibilidad general del portal EIEInfo porque evita que el usuario dependa de la estructura interna del sitio, disminuye la carga cognitiva asociada a localizar contenido específico y elimina barreras de entrada para público externo o estudiantes sin credenciales activas. Además, al presentar la información mediante un flujo guiado, se asegura que incluso usuarios sin familiaridad con el portal puedan obtener datos relevantes de forma rápida, consistente y sin riesgo de perderse entre secciones o enlaces internos. En conjunto, estos elementos hacen que la interacción con EIEInfo sea más eficiente, directa y alineada con prácticas modernas de autoservicio informativo.

---

## 2.2 Mejoras Respecto al Estado Inicial de Semana 1

* Acceso inmediato a información pública.

* Reducción significativa del tiempo de búsqueda.

* Interacción guiada mediante árbol de decisiones.

* Eliminación de barreras de autenticación para contenido no sensible.

* Integración modular respetando la arquitectura Django existente.

---

## 2.3 Indicadores de Impacto

* Reducción de pasos para obtener información (de 4–6 clics → 1–2).

* Acceso universal para estudiantes, egresados y público externo.

* Estandarización del contenido a través del árbol.

* Carga cognitiva reducida al evitar búsquedas manuales.
 
---

## 2.4 Mantenibilidad y Escalabilidad

El diseño prioriza la claridad y la extensibilidad. Los siguientes puntos detallan las decisiones que facilitan mantenimiento y crecimiento:

- **Inicialización y cacheo del árbol:** El árbol de decisiones se inicializa en `ChatbotConfig.ready()` y se mantiene en memoria como referencia compartida (`self.tree`). Esto evita costos de reconstrucción y permite respuestas rápidas, pero implica que cambios en el árbol por código requieren reinicio del proceso o un mecanismo de recarga explícito.

- **Desacoplamiento mediante callbacks:** Las consultas dinámicas (p. ej. `DynamicNode`) delegan la obtención de datos a funciones en `services.py`. Esto permite testear y reemplazar la lógica de acceso a datos sin cambiar la estructura del árbol.

- **Extensibilidad de nodos:** Añadir un nuevo tipo de nodo es directo: heredar de `BaseNode` y añadir la lógica de serialización en `to_dict()`. Las instancias se registran en `DecisionTree._load_nodes()` o mediante un mecanismo de carga dinámico si se implementa.

- **Compatibilidad con ORM existente:** La solución utiliza el ORM de Django para recuperar datos (p. ej. `Asistencia`). No se requieren migraciones adicionales en la base de datos para el módulo chatbot, salvo que se quiera almacenar métricas o historiales.

- **Consideraciones de escalado:** Para un alto volumen de tráfico, recomiendan:
    - Implementar paginación en `services.py` para las consultas que devuelven listas grandes.
    - Añadir caching a nivel de respuesta (ej. Redis) para resultados de `DynamicNode` que no cambian con frecuencia.
    - Añadir endpoints de gestión para recargar/editar el árbol en caliente sin reiniciar el servicio.


---

# 3. Propuesta de Evolución

## 3.1 Mejoras recomendadas

1. Panel administrativo completo para editar el árbol sin tocar código.

2. Análisis de métricas de uso (nodos más consultados, tiempos, rutas).

3. Soporte para búsqueda semántica en contenidos públicos.

---

## 3.2 Roadmap Propuesto

### Corto plazo (1–2 semanas)

* Refinar árbol y limpiar rutas internas.

* Ajustar validaciones y logs.

### Mediano plazo (1 mes)

* Implementar panel administrativo.

* Normalizar la estructura de todos los documentos públicos.

### Largo plazo (2–3 meses)

* Integrar métricas y panel analítico.

* Evaluar versión híbrida con integración de LLM para preguntas abiertas.
---

## 3.3 Aspectos No Logrados en Esta Entrega

* Panel administrativo visual para construcción de flujos.

* Métricas automáticas del uso del chatbot.

* Integración con componentes UI/UX avanzados (animaciones, búsqueda).

---

# 4. Evidencias de Funcionamiento

Puede consultar un video demostrativo en el siguiente enlace:  [Demo EIE Chatbot](https://youtu.be/swNCgBg1Yp4)


# 5. Conclusiones Finales
El desarrollo del chatbot demostró que una solución basada en flujos de decisión es efectiva para centralizar y estandarizar el acceso a información pública en entornos académicos.

- **Resultados observados:** el widget reduce significativamente el número de pasos necesarios para encontrar información clave (planes de estudio, asistencias, trámites), lo que mejora la experiencia de usuario y baja la carga de soporte en canales tradicionales.

- **Fortalezas arquitectónicas:** la separación entre presentación, serialización de nodos y servicios de datos facilita mantenimiento y pruebas. El patrón de nodos polimórficos permite añadir nuevas formas de respuesta (documentos, listas, datos dinámicos) con cambios mínimos.

- **Limitaciones prácticas:** algunas integraciones dinámicas dependen de la existencia de modelos y datos externos (por ejemplo, la app `asistencias`). En entornos de prueba, es necesario contar con datos de muestra o respuestas simuladas para validar el flujo completo.

- **Recomendaciones para producción:**
    1. Añadir control de versiones para el árbol o un endpoint administrativo para editar nodos en caliente.
    2. Implementar caching y paginación para queries que devuelven grandes colecciones.
    3. Revisar políticas de CSRF y CORS si el widget se sirve desde dominios distintos.

En resumen, el proyecto entrega una base sólida, probada y modular sobre la cual se pueden incluir mejoras iterativas (panel administrativo, analítica de uso y soporte semántico con una LLM) sin necesidad de reescrituras profundas.

---
