from unittest import mock

from django.apps import apps
from django.test import RequestFactory, SimpleTestCase

from . import views
from .node import DynamicNode
from .tree_structure import DecisionTree


class DecisionTreeTests(SimpleTestCase):
    def setUp(self):
        self.tree = DecisionTree()

    def test_root_exists_and_is_menu(self):
        root = self.tree.get("root")
        data = root.to_dict()
        self.assertEqual(data["node_id"], "root")
        self.assertEqual(data["type"], "menu")
        self.assertIn("planes", data["options"])

    def test_unknown_node_falls_back_to_root(self):
        node = self.tree.get("does-not-exist")
        self.assertEqual(node.node_id, "root")

    def test_document_node_contains_link(self):
        node = self.tree.get("plan_lic")
        data = node.to_dict()
        self.assertEqual(data["type"], "document")
        self.assertTrue(data["document"].endswith("licenciatura.pdf"))

    def test_dynamic_node_uses_callback(self):
        fake_callback = mock.Mock(return_value=[{"titulo": "Demo"}])
        dyn = DynamicNode("dyn", "texto", callback=fake_callback, options={"root": "volver"})
        data = dyn.to_dict()
        fake_callback.assert_called_once()
        self.assertEqual(data["type"], "dynamic")
        self.assertEqual(data["items"][0]["titulo"], "Demo")


class ChatbotQueryViewTests(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.tree = DecisionTree()
        apps.get_app_config("chatbot").tree = self.tree

    def test_returns_requested_node(self):
        request = self.factory.get("/chatbot/query", {"node": "root"})
        response = views.chatbot_query(request)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertFalse(data.get("error", False))
        self.assertEqual(data["node_id"], "root")

    def test_fallback_to_root_on_invalid_node(self):
        request = self.factory.get("/chatbot/query", {"node": "invalid"})
        response = views.chatbot_query(request)
        data = response.json()
        self.assertEqual(data["node_id"], "root")

    def test_error_when_tree_missing(self):
        apps.get_app_config("chatbot").tree = None
        request = self.factory.get("/chatbot/query")
        response = views.chatbot_query(request)
        data = response.json()
        self.assertTrue(data.get("error"))
        self.assertIn("Árbol", data.get("message", ""))
