from flask import jsonify,request 
from db.db import cnx

class Persona ():
    global cur
    cur = cnx.cursor()
    
    def list():
        lista=[]
        cur.execute("SELECT * FROM participantes")
        row = cur.fetchall()
        columns = [i[0] for i in cur.description]
        for row in row:
            registro = zip (columns,row)
            json = dict(registro)
            lista.append(json)
        return jsonify(lista)
        cnx.close

    def create (body):
        data = (body['cedula'],body['nombre'],body['actividades'],body['estrato'],body['foto'])
        sql = "INSERT INTO participantes(cedula,nombre,actividades,estrato,foto) VALUES (%s,%s,%s,%s,%s)"
        cur.execute (sql,data)
        cnx.commit()
        return {'estado':'insertado'},200