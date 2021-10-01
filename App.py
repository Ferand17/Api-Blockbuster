from Conection import Conection
from flask import Flask
from flask import jsonify

app = Flask(__name__)
db = Conection()

@app.route('/', methods=['GET'])
def inicio():
    response = """
                    <h1>Practica Unica 201700858</h1>
                    <br>
                    <h3>Nombre: Elder Andrade</h3>
                    <br>
                    <h3>Carnet: 201700858</h3>
                    <br>
                    <h3>LAB MIA A+</h3>
                    """
    return response

@app.route('/consulta1', methods=['GET'])
def consulta1():
    db.execute("""
            
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta2', methods=['GET'])
def consulta2():
    db.execute("""
        select * from public.temporal limit 100;
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta3', methods=['GET'])
def consulta3():
    db.execute("""

                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta4', methods=['GET'])
def consulta4():
    db.execute("""

                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta5', methods=['GET'])
def consulta5():
    db.execute("""

                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta6', methods=['GET'])
def consulta6():
    db.execute("""

                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta7', methods=['GET'])
def consulta7():
    db.execute("""

                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta8', methods=['GET'])
def consulta8():
    db.execute("""

                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta9', methods=['GET'])
def consulta9():
    db.execute("""

                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/consulta10', methods=['GET'])
def consulta10():
    db.execute("""

                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/eliminarTemporal', methods=['DELETE'])
def eliminarTemporal():
    db.execute("""
    
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/eliminarModelo', methods=['DELETE'])
def eliminarModelo():
    db.execute("""

                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/cargarTemporal', methods=['POST'])
def cargarTemporal():
    db.execute("""
                
                """)
    response = db.getSalida()
    return jsonify(response)

@app.route('/cargarModelo', methods=['POST'])
def cargarModelo():
    db.execute("""
        
                """)
    response = db.getSalida()
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='localhost',port=3000,debug=False)