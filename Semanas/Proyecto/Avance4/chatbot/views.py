# chatbot/views.py

import json

from django.http import JsonResponse
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .tree_structure import DecisionTree


@csrf_exempt
@require_http_methods(["GET", "POST"])
def chatbot_query(request):
    try:
        config = apps.get_app_config('chatbot')
        tree = config.tree
        if tree is None:
            try:
                config.tree = DecisionTree()
                tree = config.tree
            except Exception as exc:
                msg = config.tree_error or str(exc) or "Árbol no inicializado."
                return JsonResponse({"error": True, "message": msg})
    except Exception as e:
        return JsonResponse({"error": True, "message": "Árbol no inicializado."})

    node_id = request.GET.get("node")
    if not node_id and request.method == "POST":
        try:
            payload = json.loads(request.body.decode() or "{}")
        except Exception:
            payload = {}
        node_id = payload.get("node") or request.POST.get("node")
    node_id = node_id or "root"

    try:
        node = tree.get(node_id)
        return JsonResponse(node.to_dict())
    except Exception as e:
        return JsonResponse({"error": True, "message": "Error al procesar el nodo."})
