from flask import Flask, render_template
import urllib
from urllib import parse

app = Flask(__name__)

@app.route('/')
def index():
    edad = 21
    return render_template('index.html', edad = edad)


#Nota: las rutas son sensibles a mayusculas
@app.route('/Contacto')
def contacto():
    total = 1000
    return """<h1>Bienvenido a la pagina de contactos</h1>"""


@app.route('/Proyectos/<nombre>/<edad>') #/Proyectos/<string:nombre>/<int:edad> O /Proyectos/<nombre>/<edad> Es igual
def proeyectos(nombre, edad = None):
    total = 1000
    return render_template('proyectos.html', nombre = nombre, edad = edad)


@app.route('/loops')
def loops():
    lista = ['frutas', 'verduras', 'Lipmpieza', 'Abarrotes']
    return render_template('loops.html', lista = lista)

@app.route('/mapa/<latitud>/<longitud>')
def mapa(latitud, longitud):
    latitud2 = urllib.parse.unquote(latitud)
    longitud2 = urllib.parse.unquote(longitud)
    return render_template('mapa.html', latitud = latitud2, longitud = longitud2)

@app.route('/mapa/<latitud>/<longitud>/<zoom>/<sizemap>/<message>')
def mapa_configurado(latitud, longitud, zoom, sizemap, message):
    latitud2 = urllib.parse.unquote(latitud)
    longitud2 = urllib.parse.unquote(longitud)
    zoom2 = urllib.parse.unquote(zoom)
    sizemap2 = urllib.parse.unquote(sizemap)
    message2 = urllib.parse.unquote(message)
    return render_template('mapa.html', latitud = latitud2, longitud = longitud2, zoom=zoom2, sizemap=sizemap2, message=message2)

@app.route('/mapa/<latitud>/<longitud>/<message>')
def mapa_con_mensaje(latitud, longitud, message):
    latitud2 = urllib.parse.unquote(latitud)
    longitud2 = urllib.parse.unquote(longitud)
    message2 = urllib.parse.unquote(message)
    return render_template('mapa.html', latitud = latitud2, longitud = longitud2, message=message2)

