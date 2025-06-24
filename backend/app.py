from flask import Flask, request, jsonify
from flask_cors import CORS
from bson.json_util import dumps

from models.arbolMVias import ArbolMVias

app = Flask(__name__)
CORS(app)

arbol = ArbolMVias(4)


@app.route('/insertar', methods=['POST'])
def insertar():
    """
    Inserta un nuevo dato en el árbol M-vías.

    El usuario debe enviar un JSON con el campo 'dato'.
    Si no se proporciona el campo 'dato', se devuelve un error 400.
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'El campo "dato" es obligatorio.'}), 400

    arbol.insertar(data['dato'])

    return jsonify({'mensaje': f'Dato "{data["dato"]}" insertado correctamente.'}), 201


@app.route('/listar', methods=['GET'])
def listar():
    """
    Devuelve la estructura del árbol M-vías en formato JSON.

    La respuesta contiene los niveles del árbol en forma de lista.
    """
    return jsonify(arbol.obtener_niveles())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
