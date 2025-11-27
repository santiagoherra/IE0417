# chatbot/decision_tree.py

from .node import BaseNode, MenuNode, DocumentNode, ListNode, DynamicNode
from .services import obtener_asistencias_semestre_actual

class DecisionTree:
    def __init__(self):
        self.nodes = {}
        self._load_nodes()

    def add(self, node: BaseNode):
        self.nodes[node.node_id] = node

    def get(self, node_id):
        return self.nodes.get(node_id, self.nodes["root"])

    def _load_nodes(self):

        # ----- ROOT (Menú principal)-----
        self.add(MenuNode(
            "root",
            "Hola 👋, soy el asistente de EIEInfo. ¿Qué buscás?",
            options={ 
                "planes": {
                    "text": "Planes de estudio",
                    "next_node": "planes"
                },
                "asistencias": {
                    "text": "Asistencias disponibles",
                    "next_node": "asistencias"
                },
                "proyectos":{
                    "text": "Proyectos eléctricos",
                    "next_node": "proy_electricos"
                },
                "practica":{
                    "text": "Práctica laboral",
                    "next_node": "prac_laboral"
                },
                "graduacion":{
                    "text": "Trámites de graduación",
                    "next_node": "tramites_graduacion"
                },
                "laboratorios":{
                    "text": "Laboratorios",
                    "next_node": "laboratorios"
                },
            }
        ))

        # ----- PLANES -----
        self.add(MenuNode(
            "planes",
            "Selecciona un plan:",
            options={
                "plan_bach": "Plan Bachillerato",
                "plan_lic": "Plan Licenciatura",
                "plan_emp": "Énfasis electromagnetismo",
                "root": "Volver al menú principal",
            }
        ))

        self.add(DocumentNode(
            "plan_bach",
            "Aquí tenés el plan de Bachillerato:",
            "docs/planes/bachillerato.pdf",
            options={"root": "Volver al menú principal"}
        ))

        self.add(DocumentNode(
            "plan_lic",
            "Aquí tenés el plan de Licenciatura:",
            "docs/planes/licenciatura.pdf",
            options={"root": "Volver al menú principal"}
        ))

        self.add(DocumentNode(
            "plan_emp",
            "Plan del énfasis en electromagnetismo:",
            "docs/planes/enfasis_electromagnetismo.pdf",
            options={"root": "Volver al menú principal"}
        ))

        # ----- ASISTENCIAS -----
        self.add(MenuNode(
            "asistencias",
            "Selecciona el tipo de asistencia:",
            options={
                "asis_curso": "Asistencias por curso",
                "asis_general": "Asistencias generales",
                "asistencias_activas": {
                    "text": "Asistencias activas (ciclo actual)",
                    "next_node": "asistencias_activas"
                },
                "root": "Volver al menú principal",
            }
        ))

        self.add(ListNode(
            "asis_curso",
            "Asistencias por curso:",
            items=[
                "IE0405 – Programación I",
                "IE0210 – Circuitos eléctricos",
                "IE0309 – Comunicaciones",
            ],
            options={"root": "Volver al menú principal"}
        ))

        self.add(ListNode(
            "asis_general",
            "Asistencias generales:",
            items=[
                "Tutoría electrónica básica",
                "Tutoría matemáticas",
            ],
            options={"root": "Volver al menú principal"}
        ))

        self.add(DynamicNode(
            node_id="asistencias_activas",
            text="Asistencias disponibles este semestre:",
            callback=obtener_asistencias_semestre_actual,
            options={
                "root": "Volver al menú principal"
            }
        ))

        # ----- PROYECTOS ELÉCTRICOS -----
        self.add(MenuNode(
            "proy_electricos",
            "Proyectos eléctricos disponibles:",
            options={
                "proy_baja_tension": "Proyectos de baja tensión",
                "proy_potencia": "Proyectos de potencia",
                "proy_investigacion": "Proyectos de investigación",
                "root": "Volver al menú principal",
            }
        ))

        self.add(ListNode(
            "proy_baja_tension",
            "Ejemplos de proyectos de baja tensión:",
            items=[
                "Residencial inteligente",
                "Automatización de iluminación",
                "Monitoreo energético doméstico",
            ],
            options={"root": "Volver al menú principal", "proy_electricos": "Volver a proyectos"}
        ))

        self.add(ListNode(
            "proy_potencia",
            "Ejemplos de proyectos de potencia:",
            items=[
                "Estudios de calidad de energía",
                "Análisis de protecciones",
                "Modelado de sistemas de transmisión",
            ],
            options={"root": "Volver al menú principal", "proy_electricos": "Volver a proyectos"}
        ))

        self.add(ListNode(
            "proy_investigacion",
            "Líneas de investigación eléctrica:",
            items=[
                "Energías renovables y almacenamiento",
                "Electromovilidad",
                "Microredes y smart grids",
            ],
            options={"root": "Volver al menú principal", "proy_electricos": "Volver a proyectos"}
        ))

        # ----- PRÁCTICA LABORAL -----
        self.add(MenuNode(
            "prac_laboral",
            "Información sobre práctica laboral:",
            options={
                "prac_requisitos": "Requisitos y elegibilidad",
                "prac_documentos": "Documentación necesaria",
                "prac_contacto": "Contacto y horarios",
                "root": "Volver al menú principal",
            }
        ))

        self.add(ListNode(
            "prac_requisitos",
            "Requisitos comunes para la práctica laboral:",
            items=[
                "Haber aprobado cursos básicos de la malla",
                "Contar con seguro estudiantil vigente",
                "Inscribirse en el período establecido por la escuela",
            ],
            options={"root": "Volver al menú principal", "prac_laboral": "Volver a práctica"}
        ))

        self.add(ListNode(
            "prac_documentos",
            "Documentos a presentar:",
            items=[
                "Carta de presentación firmada",
                "Hoja de vida actualizada",
                "Formulario de inscripción al curso de práctica",
            ],
            options={"root": "Volver al menú principal", "prac_laboral": "Volver a práctica"}
        ))

        self.add(ListNode(
            "prac_contacto",
            "Canales de contacto sugeridos:",
            items=[
                "Coordinador de práctica laboral",
                "Correo de coordinación estudiantil",
                "Plataforma institucional para prácticas",
            ],
            options={"root": "Volver al menú principal", "prac_laboral": "Volver a práctica"}
        ))

        # ----- TRÁMITES DE GRADUACIÓN -----
        self.add(MenuNode(
            "tramites_graduacion",
            "Trámites de graduación:",
            options={
                "grad_requisitos": "Requisitos académicos",
                "grad_documentos": "Documentos a presentar",
                "grad_fechas": "Fechas y plazos",
                "root": "Volver al menú principal",
            }
        ))

        self.add(ListNode(
            "grad_requisitos",
            "Requisitos académicos típicos:",
            items=[
                "Aprobar todos los cursos del plan",
                "Completar horas de práctica o TCU",
                "No tener sanciones académicas pendientes",
            ],
            options={"root": "Volver al menú principal", "tramites_graduacion": "Volver a trámites"}
        ))

        self.add(ListNode(
            "grad_documentos",
            "Documentos solicitados:",
            items=[
                "Solicitud formal de graduación",
                "Certificación de notas",
                "Recibos de pago correspondientes",
            ],
            options={"root": "Volver al menú principal", "tramites_graduacion": "Volver a trámites"}
        ))

        self.add(ListNode(
            "grad_fechas",
            "Fechas y plazos frecuentes:",
            items=[
                "Periodo de solicitud: semanas 1-4 del semestre",
                "Revisión de expediente: semanas 5-7",
                "Defensa o entrega final: semanas 12-14",
            ],
            options={"root": "Volver al menú principal", "tramites_graduacion": "Volver a trámites"}
        ))

        # ----- LABORATORIOS -----
        self.add(MenuNode(
            "laboratorios",
            "Información de laboratorios:",
            options={
                "lab_horarios": "Horarios y reserva",
                "lab_normas": "Normas de seguridad",
                "lab_contacto": "Contacto del coordinador",
                "root": "Volver al menú principal",
            }
        ))

        self.add(ListNode(
            "lab_horarios",
            "Horarios y reserva:",
            items=[
                "Reserva previa mediante el sistema institucional",
                "Disponibilidad sujeta a cursos en ejecución",
                "Consultar aforos máximos por laboratorio",
            ],
            options={"root": "Volver al menú principal", "laboratorios": "Volver a laboratorios"}
        ))

        self.add(ListNode(
            "lab_normas",
            "Normas de seguridad básicas:",
            items=[
                "Uso obligatorio de equipo de protección personal",
                "Reportar cualquier incidente al asistente de laboratorio",
                "Mantener limpios y ordenados los puestos de trabajo",
            ],
            options={"root": "Volver al menú principal", "laboratorios": "Volver a laboratorios"}
        ))

        self.add(ListNode(
            "lab_contacto",
            "Contacto sugerido:",
            items=[
                "Coordinador general de laboratorios",
                "Correo de soporte técnico",
                "Asistente de laboratorio según curso",
            ],
            options={"root": "Volver al menú principal", "laboratorios": "Volver a laboratorios"}
        ))
