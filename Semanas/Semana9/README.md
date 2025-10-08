# Laboratorio Docker: de cero a capas (con Flask)

**Universidad de Costa Rica – Escuela de Ingeniería Eléctrica**  
**Curso:** IE0417 – Diseño de Software para Ingeniería  
**Docente:** Rafael Esteban Badilla Alvarado  
**Estudiante:** Santiago Herra Castro  

---

## Objetivos del laboratorio

- Entender la diferencia entre **imagen** y **contenedor**.  
- Observar cómo funcionan las **capas de una imagen Docker** y cómo el **caché** acelera los builds.  
- Construir una imagen por capas con un **Dockerfile bien estructurado**.  
- Controlar el contexto del build con **.dockerignore**.  
- Ejecutar contenedores, exponer puertos, pasar variables de entorno y montar volúmenes.  
- Diferenciar entre **CMD** y **ENTRYPOINT**.  
- Añadir un **HEALTHCHECK**.  
- Usar **Docker Compose** y crear un ejemplo **multi-stage**.

---

## Prerrequisitos

- Docker y Docker Compose instalados.  
  ```bash
  docker --version
  docker compose version
  Editor de texto (VS Code, nano, etc.)
  curl instalado para probar endpoints.

📁 Estructura del proyecto
docker-por-capas/
├── app.py
├── requirements.txt
├── Dockerfile
├── Dockerfile.dev
├── .dockerignore
├── compose.yaml
└── Figuras