from flask import Flask, jsonify ,request
from flask_cors import CORS
from controllers.personas import Persona

app = Flask(__name__)
CORS(app)

@app.route('/participantes')
def getALL():
    return (persona.list())

@app.route('/participantes' , methods =['POST'])
def postONE():
    body = request.json
    return (persona.create(body))

app.run(port=5000,debug=True)