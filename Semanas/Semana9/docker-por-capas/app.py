from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    saludo = os.getenv("SALUDO", "Hola, clase IE0417")
    return jsonify({"ok": True, "mensaje": saludo})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
