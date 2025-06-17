from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from models.arbolAVL import ArbolMVias

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/menusdb"
mongo = PyMongo(app)

# Crear un árbol M-vias global
M = 4  # Se define los enlaces
arbol = ArbolMVias(M)

@app.route('/menu', methods=['POST'])
def insertar_menu():
    data = request.get_json()
    nombre = data.get('nombre')
    if not nombre:
        return jsonify({"error": "Falta nombre"}), 400

    arbol.insertar(nombre)

    # Guardar en MongoDB como respaldo
    mongo.db.menus.insert_one({"nombre": nombre})

    return jsonify({"mensaje": "Menú insertado correctamente."})

@app.route('/menu', methods=['GET'])
def obtener_menu():
    estructura = arbol.to_dict()
    return jsonify(estructura)

@app.route('/menu_db', methods=['GET'])
def obtener_menus_mongo():
    menus = mongo.db.menus.find()
    return dumps(menus)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
