from django.apps import AppConfig

class ChatbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chatbot'

    def ready(self):
        """
        Inicializa el árbol de decisión cuando se carga la app para que las
        vistas puedan accederlo vía apps.get_app_config('chatbot').tree.
        """
        self.tree_error = ""
        try:
            from .tree_structure import DecisionTree
            self.tree = DecisionTree()
        except Exception as exc:
            # Evita fallos en el arranque de Django si falta alguna dependencia
            self.tree_error = str(exc)
            self.tree = None
