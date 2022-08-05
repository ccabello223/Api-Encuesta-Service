import imp
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

from config import config

app = Flask(__name__)

#CORS(app)
CORS(app, resources={r"/encuestas/*": {"origins": "*"}})

conexion = MySQL(app)

@app.route('/encuestas', methods=['GET'])
def listar_encuesta():
    try:
        encuestas=[];
        datos = lista_encuestas();
        cantidad_encuesta = numero_encuesta();
        socialFav = red_socialfav();
        socialNoFav = red_socialNofav();

        for fila in datos:
            encuesta={'email':fila[0], 'edades':fila[1], 'sexo':fila[2], 'social_fav':fila[3],
             'time_on_fc':fila[4], 'time_on_ws':fila[5], 'time_on_tw':fila[6], 'time_on_ig':fila[7], 'time_on_tk':fila[8]}
            encuestas.append(encuesta)

        return jsonify({'encuestas':encuestas, 'cantidad_encuesta':cantidad_encuesta,
             'social_fav':socialFav, 'social_no_fav': socialNoFav})

    except Exception as ex:
        return jsonify({'mensaje':"Error"})


@app.route('/encuestas/<string:codigo>', methods=['GET'])
def rango_redSocial_edad(codigo):
    red_social_por = rango_edad(codigo);
    return jsonify({'rango_edad' : red_social_por})


@app.route('/encuestas/tiempo_promedio/<string:codigo>', methods=['GET'])
def tiemp_prome(codigo):
    tiemp_prome = round(suma_tiempo(codigo) / 60, 3);
    return jsonify({'tiempo_promedio' : tiemp_prome});


@app.route('/encuestas', methods=['POST'])
def registrar_encuestas():
    try:
        cursor = conexion.connection.cursor()
        sql = """ INSERT INTO ptecnica_cacs(email, edades, sexo, social_fav, time_on_fc, time_on_ws, time_on_tw, time_on_ig, time_on_tk)
        VALUES('{0}', '{1}', '{2}', '{3}', {4}, {5}, {6}, {7}, {8})
        """.format(request.json['email'], request.json['edades'], request.json['sexo'], request.json['social_fav'], request.json['time_on_fc'],
         request.json['time_on_ws'], request.json['time_on_tw'], request.json['time_on_ig'], request.json['time_on_tk'])

        cursor.execute(sql)
        conexion.connection.commit()
        return jsonify({'mensaje':"Encuesta registrada.", 'exito': True})
    except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})


def lista_encuestas():
    try:
        cursor = conexion.connection.cursor()
        sql="SELECT email, edades, sexo, social_fav, time_on_fc, time_on_ws, time_on_tw, time_on_ig, time_on_tk FROM ptecnica_cacs"
        cursor.execute(sql)
        datos = cursor.fetchall()
        if datos != None:
            return datos
        else:
            return None
    except Exception as ex:
        raise ex


def  numero_encuesta():
    try:
        cursor = conexion.connection.cursor();
        sql = "SELECT count(*) as resp FROM ptecnica_cacs";
        cursor.execute(sql);
        datos = cursor.fetchone();
        if datos != None:
            cantidad = datos[0];
            return cantidad
        else:
            return None
    except Exception as ex:
        raise ex


def suma_tiempo(red_social):
    try:
        cursor = conexion.connection.cursor();
        sql = "SELECT SUM({0}) as total FROM ptecnica_cacs".format(red_social)
        cursor.execute(sql);
        datos = cursor.fetchone();
        if datos != None:
            tiem_pro = datos[0];
            return tiem_pro
        else:
            return None
    except Exception as ex:
        raise ex


def red_socialfav():
    try:
        cursor = conexion.connection.cursor();
        sql = """SELECT social_fav FROM  ptecnica_cacs GROUP BY social_fav 
                    ORDER BY COUNT( social_fav ) DESC LIMIT 1""";
        cursor.execute(sql);
        datos = cursor.fetchone();
        if datos != None:
            socialFav = datos[0];
            return socialFav
        else:
            return None
    except Exception as ex:
        raise ex


def red_socialNofav():
    try:
        cursor = conexion.connection.cursor();
        sql = """SELECT social_fav FROM  ptecnica_cacs GROUP BY social_fav 
                    ORDER BY COUNT( social_fav ) ASC LIMIT 1""";
        cursor.execute(sql);
        datos = cursor.fetchone();
        if datos != None:
            socialNoFav = datos[0];
            return socialNoFav
        else:
            return None
    except Exception as ex:
        raise ex


def rango_edad(rango):
    try:
        cursor = conexion.connection.cursor();
        sql = """SELECT social_fav
            FROM  ptecnica_cacs where edades = '{0}'
            GROUP BY social_fav
            ORDER BY COUNT( social_fav ) DESC LIMIT 1""".format(rango)
        cursor.execute(sql);
        datos = cursor.fetchone();
        if datos != None:
            socialNoFav = datos[0];
            return socialNoFav
        else:
            return None
    except Exception as ex:
        raise ex


def pagina_no_encontrada(error):
    return "<h1>La página no existe...</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run();