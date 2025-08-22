**ACRONIMOS DE CLASE:**

- SLA: Service Level Agreement
- E2E: End to End
- MVP: Minimun Viable Product 
- Elicitacion: Es la cantidad mínima de información o requerimientos mínimos enfocado en un proyecto.
- CIT: Continuous Integration Testing
- KPI: Key Performance Indicator
- MFA: Multiple Factor Autentication
- Eyes  ON/OFF: Se realiza con información la cual conozco/Información la cual desconozco.

Tipos de pruebas:
- Van por Tiers, Tier0, son las pruebas que se hace en el CI/CD, tier1, son cuando duran unas horas o asi, Tier2, duran mas tiempo se hacen en la noche.

DevOps
- Son las personas que se encargan de crear herramientas, contenedores las cuales que definen o dan soporte a los programadores para no romper el flujo de código



# Investigación — Microsoft: metodologías, herramientas y diseño a escala
 
## 1. Metodologías de desarrollo y diseño
 
### a) ¿Usan Agile, Scrum, Kanban, DevOps o enfoques propios?
 
**DevOps como cultura**  
Microsoft impulsa **DevOps** de forma transversal (personas + procesos + herramientas) y lo documenta públicamente con casos y guías.
 
**Agile/Scrum/Kanban**  
**Azure Boards** (parte de Azure DevOps) soporta prácticas **Agile** y **Scrum**, y también puede mapear **SAFe** para organizaciones grandes.
 
**Enfoques propios**
- **1ES (One Engineering System):** unifica prácticas, herramientas y estándares internos para elevar la excelencia de ingeniería.
- **SDL (Security Development Lifecycle):** integra seguridad “by design” dentro del ciclo DevOps (**DevSecOps**).
- **Release Flow (trunk-based):** estrategia de ramas simplificada para entregar servicios online de forma segura y continua.
 
---
 
### b) ¿Cómo escalan estas metodologías en proyectos con miles de desarrolladores?
 
**Proceso único y simple**  
Usan un flujo tipo **trunk-based** (“**Release Flow**”). Todo cambio entra por **pull request** con políticas estrictas (builds, revisores, tests).
 
**Plataforma común (1ES)**  
Mismos *templates*, pipelines, agentes y **Dev Boxes** para todos. Estandarizar reduce fricción y variación entre equipos.
 
**Gestión a varios niveles**  
De **portafolio → programas → equipos** con **Azure Boards** (épicas, features, historias). Planificación coordinada sin quitar autonomía local.
 
**Código a escala**  
**Monorepos/Git** optimizados (p. ej., herramientas como **Scalar**) para que repos gigantes sigan siendo usables.
 
**Automatización y calidad**  
**CI/CD** obligatorio, pruebas (unitarias/**E2E**), análisis estático, *feature flags*, *canary/blue-green* y *rollbacks* rápidos.
 
**Seguridad y trazabilidad**  
Prácticas de **SDL**, **MFA**, control de secretos y auditoría para saber **qué** cambió, **quién** y **cuándo**.
 
**Observabilidad**  
Métricas, logs, alertas y **SLO/SLA** para detectar y revertir problemas sin frenar el flujo.
 
> **Idea central:** estandarizan **proceso + herramientas + gobierno** y automatizan todo lo repetible. Así miles de devs pueden mover cambios pequeños, seguros y continuos **sin caos**.


### Pregunta 2: Principios de Arquitectura de Software en Microsoft
#### Principios clave
En Microsoft se aplican varios principios de arquitectura de software modernos.  
Por ejemplo, se utiliza la arquitectura de microservicios en plataformas como Azure y Office 365, lo que permite que cada servicio, como correo, almacenamiento o colaboración, funcione y se escale de manera independiente.  

Además, Microsoft hace un fuerte uso de las APIs, un buen ejemplo es la Microsoft Graph API, que permite conectar servicios como Outlook, Teams y OneDrive con aplicaciones externas. Esto fomenta la integración y la personalización para los usuarios y desarrolladores.  

Otro principio clave es la modularidad. Sus productos están diseñados para funcionar tanto de manera individual como integrada. Un ejemplo es la suite de Office, donde Word, Excel o PowerPoint pueden usarse por separado, pero también se comunican entre sí de forma eficiente.  

Finalmente, Microsoft impulsa el enfoque cloud-native, especialmente con Azure, lo que significa que sus aplicaciones están pensadas para la nube desde el inicio, aprovechando contenedores, Kubernetes y servicios escalables para garantizar disponibilidad y rendimiento.  

#### Impacto en productos concretos

- Outlook y Office 365 integran correo, almacenamiento y colaboración en tiempo real gracias a APIs y modularidad.  
- Azure aprovecha la nube y los microservicios para dar escalabilidad a aplicaciones críticas de empresas.  
- Windows 10 y 11 incorporan un diseño modular que permite actualizar componentes por separado, mejorando la seguridad y estabilidad.  
- En Microsoft Teams, el uso de microservicios garantiza que, aunque falle un módulo como las videollamadas, el resto de la plataforma siga funcionando.  

#### Conclusión

En conclusión, estos principios de diseño permiten a Microsoft ofrecer productos escalables, seguros e integrados, que se adaptan a las necesidades tanto de usuarios individuales como de grandes empresas.

## 3. Herramientas y ecosistemas internos
 
### a) ¿Frameworks/herramientas que luego fueron estándar de la industria?
 
Algunos sí se convierten en **estándares (formales o de facto)** —**Dapr, KEDA, LSP, ONNX**—; otros son **frameworks/herramientas ampliamente adoptadas** —**Orleans, TypeScript**—; y otros acabaron **integrados “upstream”** —**Scalar/VFS for Git**—. No todos siguen el mismo camino, pero varios trascienden su origen interno y marcan industria.
 
| Proyecto | Tipo | Descripción breve |
|---|---|---|
| **TypeScript** | Lenguaje / herramienta | Superset tipado de JS creado por Microsoft; hoy ampliamente adoptado. |
| **LSP (Language Server Protocol)** | Protocolo / estándar | Estandariza funciones de lenguaje en editores/IDEs (originado por Microsoft con Red Hat/Codenvy). |
| **ONNX** | Formato / estándar abierto | Interoperabilidad de modelos de IA (Microsoft + Meta); adoptado por la industria. |
| **Orleans** | Framework | *Virtual actor framework* nacido en Microsoft Research; usado en sistemas a gran escala (p. ej., Halo). |
| **Dapr** | Runtime de microservicios | APIs portables para *building blocks*; proyecto **CNCF Graduated (2024)**. |
| **KEDA** | Herramienta (autoscaling) | *Autoscaling event-driven* para Kubernetes; **CNCF Graduated (2023)**; integrado con AKS. |
| **VFS for Git / Scalar** | Herramientas Git | Tecnologías para Git a escala creadas por Microsoft; parte de Git moderno (optimizaciones para monorepos). |

#### b. Cómo diseñan software para millones de usuarios concurrentes

Microsoft aplica varios principios de **escalabilidad y resiliencia** para soportar grandes volúmenes de usuarios:

1. **Arquitectura de microservicios**  
   Cada componente del sistema, como correo, chat o videollamadas, funciona de manera independiente. Esto permite escalar únicamente los servicios más demandados sin afectar al resto de la aplicación.

2. **Uso de la nube y servicios distribuidos**  
   Plataformas como **Azure** permiten distribuir la carga entre múltiples regiones y centros de datos. Servicios como **Azure Kubernetes Service (AKS)** facilitan el despliegue de contenedores de manera eficiente y escalable.

3. **Caché y bases de datos distribuidas**  
   Se utilizan cachés y bases de datos replicadas para reducir la latencia, manejar grandes volúmenes de consultas simultáneas y garantizar alta disponibilidad.

4. **Monitorización y resiliencia**  
   Herramientas como **Application Insights** y **Azure Monitor** permiten detectar problemas en tiempo real. Si un microservicio falla, el resto del sistema sigue funcionando.

5. **Optimización de APIs y protocolos**  
   Microsoft diseña APIs eficientes y utiliza protocolos como HTTP/2 y gRPC para permitir que millones de usuarios interactúen al mismo tiempo sin saturar los servicios.

**En conjunto**, estos enfoques permiten que las aplicaciones de Microsoft sean **escalables, confiables y eficientes**, incluso con millones de usuarios concurrentes.

### Pregunta 4: 

a. Cómo se organiza el trabajo de los ingenieros?

- One Engineering System (1ES): es la iniciativa transversal que estandariza herramientas y prácticas (Azure DevOps/GitHub), y embebe ingenieros dentro de otros equipos por semanas o meses para impulsar cambios culturales y de proceso desde adentro. También ejecuta “engagements” cortos para lograr quick wins y dejar plantillas de buenas prácticas. 

- Crews por foco (F-crew y C-crew): muchos equipos dividen el trabajo entre un Feature crew (futuro/roadmap) y un Customer crew (ahora/operación), con rotaciones semanales para compartir contexto y evitar distracciones de “live site” en quienes están construyendo features. 

- “Unified/Combined Engineering” (dev+test): desde ~2014 Microsoft fusionó los roles clásicos de dev y test (SDE/SDET) en Software Engineer, responsabilizando a todos por calidad y automatización. Hay relatos públicos de Azure/Office sobre el cambio. 
Triadas/equipos multifunción: históricamente se trabajó con Dev–Test–PM en “feature crews”; hoy se mantiene el espíritu multidisciplinario (ingeniería, programa/producto, diseño, datos), con variaciones según grupo. 

b. ¿Qué valores destacan en el diseño de software (simplicidad, escalabilidad, rendimiento, seguridad)? 

- Confiabilidad y seguridad (“Trustworthy Computing”): Desde 2002, bajo la dirección de Bill Gates, Microsoft consolidó la seguridad, confiabilidad y disponibilidad como prioridad absoluta en su desarrollo de software. Este enfoque, denominado “Trustworthy Computing”, estableció que la seguridad debía incorporarse desde el diseño, con arquitecturas resilientes, codificación segura, y un compromiso institucional total. Gates afirmó que, cuando se trate de elegir entre añadir características o resolver problemas de seguridad, se debe priorizar siempre la seguridad. 
- Diseño centrado en el usuario y coherente: En su transformación digital interna, Microsoft impulsó una ingeniería moderna basada en tres pilares: ser visionarios, adoptar un diseño coherente y centrado en el usuario, y trabajar como el primero en probar su propia tecnología (Customer Zero).

### Pregunta 5: Impacto en la industria de Microsoft

Microsoft ha generado varias herramientas y prácticas que se han adoptado globalmente en la industria del software.  

Entre las más importantes se encuentran **.NET y .NET Core**, plataformas de desarrollo que se utilizan en todo el mundo para crear aplicaciones web, de escritorio y móviles. También **TypeScript**, un lenguaje creado por Microsoft para mejorar JavaScript, que ahora se usa ampliamente en proyectos grandes y escalables.  

Los entornos de desarrollo **Visual Studio y Visual Studio Code** se han convertido en estándar global debido a su integración con múltiples lenguajes y su extensibilidad. Por otro lado, la **Microsoft Graph API** permite integrar servicios como Outlook, Teams y OneDrive con aplicaciones externas, fomentando conectividad y personalización.  

Además, las metodologías de **DevOps y CI/CD** promovidas a través de **Azure DevOps** son referencia global en prácticas de integración y despliegue continuo. Finalmente, la adopción de arquitecturas **cloud-native y microservicios**, impulsadas por Microsoft, ha influido en cómo muchas empresas construyen aplicaciones escalables y resilientes.  

En resumen, Microsoft no solo desarrolla productos, sino que sus herramientas y metodologías **establecen estándares globales**, influyendo en la forma en que se diseña, desarrolla y gestiona software alrededor del mundo.
