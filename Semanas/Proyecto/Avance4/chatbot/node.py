# chatbot/nodes/base.py
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

class BaseNode(ABC):
    """Clase abstracta para todos los nodos del chatbot."""

    def __init__(self, node_id, text, options=None, next_node_id: Optional[str] = None):
        self.node_id = node_id
        self.text = text
        self.options = self._normalize_options(options or {}) # Normaliza las opciones
        self.next_node_id = next_node_id or "" # Próximo nodo 

    """Permitir que las opciones sean strings o dicts"""
    def _normalize_options(self, options):
        normalized = {}

        for key, value in options.items():
            if isinstance(value, str):
                normalized[key] = {"text":value, "next_node":""}
            else: 
                normalized[key] = {
                    "text": value.get("text", ""),
                    "next_node": value.get("next_node", "")
                }
        
        return normalized


    @abstractmethod
    def to_dict(self):
        """Cada nodo debe convertir su contenido en dict."""
        return {
            "node_id": self.node_id,
            "text": self.text,
            "options": self.options,
            "next_node" : self.next_node_id
        }


class MenuNode(BaseNode):
    """Nodo simple con texto y opciones de navegación."""
    """
    Nota: no necesita next_node_id porque los que deben tenerlo 
    son las opciones del menú, no el menú per se
    """

    def to_dict(self):
        return {
            "type": "menu",
            "node_id": self.node_id,
            "text": self.text,
            "options": self.options,
            "next_node" : self.next_node_id
        }
    

class DocumentNode(BaseNode):
    """Nodo que entrega un archivo PDF al usuario."""

    def __init__(self, node_id, text, document_path, options=None):
        super().__init__(node_id, text, options)
        self.document_path = document_path

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "document"
        data["document"] = self.document_path
        return data
    

class ListNode(BaseNode):
    """Nodo que muestra una lista de items."""

    def __init__(self, node_id, text, items, options=None):
        super().__init__(node_id, text, options)
        self.items = items

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "list"
        data["items"] = self.items
        return data
    
class DynamicNode(BaseNode):
    """Nodo que ejecuta lógica dinámica (consultas ORM u otros servicios)."""

    def __init__(self, node_id, text, callback, options=None):
        super().__init__(node_id, text, options)
        self.callback = callback  # función que obtiene información dinámica

    def to_dict(self):
        dynamic_data = self.callback()  # ejecuta consulta
        data = super().to_dict()
        data["type"] = "dynamic"
        data["items"] = dynamic_data
        return data