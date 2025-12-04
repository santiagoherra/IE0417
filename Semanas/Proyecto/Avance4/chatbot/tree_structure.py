# chatbot/decision_tree.py

from .node import BaseNode, MenuNode, DocumentNode, ListNode, DynamicNode
from .services import obtener_asistencias_semestre_actual_estudiantes, obtener_asistencias_semestre_actual_laboratorio, obtener_proyectos_semestre_actual

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
                "administrativos":{
                    "text": "Tramites administrativos",
                    "next_node": "tramites_administrativos"
                },
            }
        ))

        # ----- PLANES -----
        self.add(MenuNode(
            "planes",
            "Selecciona un plan:",
            options={
                "plan_electronica": "Electronica y Telecomunicaciones - Bachillerato y Licenciatura",
                "plan_potencia": "Sistemas de potencia - Bachillerato y Licenciatura",
                "plan_compus": "Computadoras y Redes - Bachillerato",
                "root": "Volver al menú principal",
            }
        ))

        self.add(DocumentNode(
            "plan_electronica",
            "Aquí tenés el plan de estudios de Electronica y Telecomunicaciones:",
            "../docs/planes/electronica_bachillerato.pdf",
            options={"root": "Volver al menú principal"}
        ))

        self.add(DocumentNode(
            "plan_potencia",
            "Aquí tenés el plan de estudios de sistemas de potencia:",
            "../docs/planes/potencia_bachillerato.pdf",
            options={"root": "Volver al menú principal"}
        ))

        self.add(DocumentNode(
            "plan_compus",
            "Aqui tenes el plan de estudios de Computadoras y Redes:",
            "../docs/planes/computadoras_bachillerato.pdf",
            options={"root": "Volver al menú principal"}
        ))

        # ----- ASISTENCIAS -----
        self.add(MenuNode(
            "asistencias",
            "Selecciona el tipo de asistencia:",
            options={
                "asis_estudiantes": "Asistencias de estudiantes",
                "asis_lab": "Asistencias de laboratorio",
                "root": "Volver al menú principal",
            }
        ))

        self.add(DynamicNode(
            node_id="asis_estudiantes",
            text = "Asistencias de estudiantes activas:",
            callback = obtener_asistencias_semestre_actual_estudiantes,
            options={"root": "Volver al menú principal"}
        ))

        self.add(DynamicNode(
            node_id="asis_lab",
            text = "Asistencias de laboratorio activas:",
            callback = obtener_asistencias_semestre_actual_laboratorio,
            options={"root": "Volver al menú principal"}
        ))

        # ----- PROYECTOS ELÉCTRICOS -----

        self.add(DynamicNode(
            node_id="proy_electricos",
            text = "Proyectos eléctricos disponibles:",
            callback = obtener_proyectos_semestre_actual,
            options={"root": "Volver al menú principal"}
        ))

        # ----- PRÁCTICA LABORAL -----
        self.add(MenuNode(
            "prac_laboral",
            "Información sobre práctica laboral:",
            options={
                "prac_requisitos": "Requisitos y elegibilidad",
                "prac_contacto": "Contacto y horarios",
                #"prac_disponibles" : "Practicas disponibles",
                "root": "Volver al menú principal",
            }
        ))

        self.add(MenuNode(
            "prac_requisitos",
            "Documentos sobre requisitos y elegibilidad:",
            options={
                "doc_procedimiento" : "Documento de procedimiento para realizar la practica profesional",
                "doc_reglamento" : "Reglamento de prácticas profesionales",
                "root": "Volver al menú principal",
            }
        ))

        self.add(DocumentNode(
            "doc_procedimiento",
            "Aquí tenés el documento de procedimiento para realizar la práctica profesional:",
            "../docs/practica/procedimiento_practica_profesional.pdf",
            options={"root": "Volver al menú principal", "prac_requisitos": "Volver a requisitos"}
        ))

        self.add(DocumentNode(
            "doc_reglamento",
            "Aquí tenés el reglamento de prácticas profesionales:",
            "../docs/practica/reglamento_practicas_profesionales.pdf",
            options={"root": "Volver al menú principal", "prac_requisitos": "Volver a requisitos"}
        ))

        self.add(ListNode(
            "prac_contacto",
            "Canales de contacto y horarios:",
            items=[
                "Correo de la coordinación de prácticas: practicaprofesional.eie@ucr.ac.cr",
            ],
            options={"root": "Volver al menú principal", "prac_laboral": "Volver a práctica"}
        ))

        #self.add(DynamicNode(
        #    node_id="prac_disponibles",
        #    text = "Prácticas laborales disponibles:",
        #    callback = obtener_practicas_laborales_disponibles,
        #    options={"root": "Volver al menú principal", "prac_laboral": "Volver a práctica"}
        #))

        # ----- TRÁMITES DE GRADUACIÓN -----
        self.add(MenuNode(
            "tramites_graduacion",
            "Trámites de graduación:",
            options={
                "grad_requisitos": "Requisitos académicos",
                "grad_documentos": "Documentos a presentar",
                "doc_grad" : "Documento guía de trámites",
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
                "No deber materiales en la bodega"
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
                "Copia de cédula de identidad",
                "Copia de la hoja de delincuencia"
            ],
            options={"root": "Volver al menú principal", "tramites_graduacion": "Volver a trámites"}
        ))

        self.add(DocumentNode(
            "doc_grad",
            "Aquí tenés el documento guía de trámites de graduación:",
            "../docs/graduacion/guia_tramites_graduacion.pdf",
            options={"root": "Volver al menú principal", "tramites_graduacion": "Volver a trámites"}
        ))

        # ----- TRAMITES ADMINISTRATIVOS -----
        self.add(MenuNode(
            "tramites_administrativos",
            "Tramites administrativos comunes:",
            options={
                "cambio_enfasis": "Documento para cambio de enfasis",
                "prorroga_tfg": "Documento para prórroga de TFG",
                "inclusion_excepcion" : "Documento para inclusión por excepción",
                "root": "Volver al menú principal",
            }
        ))

        self.add(DocumentNode(
            "cambio_enfasis",
            "Aquí tenés el documento para cambio de énfasis:",
            "../docs/administrativos/cambio_enfasis.pdf",
            options={"root": "Volver al menú principal", "administrativos": "Volver a trámites administrativos"}
        ))

        self.add(DocumentNode(
            "prorroga_tfg",
            "Aquí tenés el documento para prórroga de TFG:",
            "../docs/administrativos/prorroga_tfg.pdf",
            options={"root": "Volver al menú principal", "administrativos": "Volver a trámites administrativos"}
        ))

        self.add(DocumentNode(
            "inclusion_excepcion",
            "Aquí tenés el documento para inclusión por excepción:",
            "../docs/administrativos/inclusion_excepcion.pdf",
            options={"root": "Volver al menú principal", "administrativos": "Volver a trámites administrativos"}
        ))

