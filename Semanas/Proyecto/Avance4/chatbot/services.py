from datetime import datetime


def obtener_proyectos_semestre_actual():
    """
    Retorna una lista de proyectos que están en concurso
    (asociados al ciclo actual), formateados para desplegar en el chatbot.
    """

    try:
        from proyectos.models import Proyecto, ProyectoCiclo
        from administrativos.models import Ciclo

        # Obtener ciclo actual

        # Filtrar ProyectoCiclo por el ciclo actual
        proyectos_qs = (
            Proyecto.objects
            .filter(
                ciclo = Ciclo.ObtenerCicloActual()
            )
            .values(
                "id",
                "sigla",
                "nombre",
                "descripcion_corta",
                "tipo",
                "fecha_inicio",
                "fecha_expiracion",
            )
        )

        proyectos = []

        for p in proyectos_qs:
            vigente = (
                p["fecha_inicio"] is not None and
                p["fecha_expiracion"] is not None and
                datetime.now().date() >= p["fecha_inicio"] and
                datetime.now().date() <= p["fecha_expiracion"]
            )
            linea = (
                f"{p['sigla']} - {p['nombre']}\n"
                f"{p['descripcion_corta']}\n"
                f"Tipo: {p['tipo']} · Vigente: {'Sí' if vigente else 'No'}\n"
                f"Inicio: {p['fecha_inicio']} · Fin: {p['fecha_expiracion']}"
            )
            proyectos.append(linea)

        return proyectos

    except Exception:
        return []
    

def obtener_asistencias_semestre_actual_estudiantes():
    """
    Retorna una lista de asistencias EN CONCURSO para el ciclo actual,
    formateadas para uso en el chatbot o APIs JS.
    """

    try:
        from estudiantes.models import Asistencia
        from administrativos.models import Ciclo

        # Obtener ciclo actual
        ciclo_actual = Ciclo.ObtenerCicloActual()

        # Filtrar asistencias en concurso para este ciclo
        asistencias_qs = (
            Asistencia.objects
            .filter(
                ciclo = ciclo_actual,
                estado = 1, # 'En concurso'
                tipo = 0 # 'Estudiante'
            )
            .select_related("funcionario", "estudiante")
        )

        asistencias = []

        for a in asistencias_qs:
            # Detectar la clase real (polymorphic)
            tipo_real = a.__class__.__name__
            # Formato legible en una sola línea para el chatbot
            linea = f"{a.descripcion_corta}\n{tipo_real}\nHoras: {a.horas}\nCiclo: {a.ciclo}\n\nProfesor: {a.funcionario}"
            asistencias.append(linea)

        return asistencias

    except Exception as e:
    # Log opcional
        print("Error obteniendo asistencias:", e)
        return []
    
def obtener_asistencias_semestre_actual_laboratorio():
    """
    Retorna una lista de asistencias EN CONCURSO para el ciclo actual,
    formateadas para uso en el chatbot o APIs JS.
    """

    try:
        from estudiantes.models import Asistencia
        from administrativos.models import Ciclo

        # Obtener ciclo actual
        ciclo_actual = Ciclo.ObtenerCicloActual()

        # Filtrar asistencias en concurso para este ciclo
        asistencias_qs = (
            Asistencia.objects
            .filter(
                ciclo = ciclo_actual,
                estado = 1, # 'En concurso'
                tipo = 1 # 'Laboratorio'
            )
            .select_related("funcionario", "estudiante")
        )

        asistencias = []

        for a in asistencias_qs:
            # Detectar la clase real (polymorphic)
            tipo_real = a.__class__.__name__
            linea = f"{a.descripcion_corta}\n{tipo_real}\nHoras: {a.horas}\nCiclo: {a.ciclo}\n\nProfesor: {a.funcionario}"
            asistencias.append(linea)

        return asistencias

    except Exception as e:
    # Log opcional
        print("Error obteniendo asistencias:", e)
        return []
