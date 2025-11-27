from datetime import datetime

def obtener_asistencias_semestre_actual():
    """
    Retorna una lista de asistencias que están activas (en concurso)
    durante el semestre actual, formateadas para desplegar en el chatbot.
    """

    try:
        # Importar de forma diferida para evitar fallos cuando la app no esté disponible
        from asistencias.models import Asistencia

        # Determinar ciclo actual
        año = datetime.now().year
        mes = datetime.now().month

        if mes <= 6:
            ciclo_actual = f"{año}-I"
        else:
            ciclo_actual = f"{año}-II"

        # Consulta ORM
        asistencias_qs = (
            Asistencia.objects
            .filter(activa=True, ciclo=ciclo_actual)
            .values(
                "id",
                "descripcion",
                "descripcion_corta",
                "funcionario",
                "horas",
                "tipo",
                "ciclo",
            )
        )

        # Convertir a formato JSON-compatible
        asistencias = []

        for a in asistencias_qs:
            asistencias.append({
                "id": a["id"],
                "titulo": a["descripcion"],
                "descripcion": a["descripcion_corta"],
                "profesor": a["funcionario"],
                "horas": a["horas"],
                "tipo": a["tipo"],  # el chatbot puede mostrar texto simple, no el display
                "ciclo": a["ciclo"],
            })

        return asistencias

    except Exception:
        # Evita que el chatbot se caiga por errores en la BD
        return []
