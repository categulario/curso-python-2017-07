# Hola mundo en flask: hello.py
# Se importa la clase Flask del paquete flask
from flask import Flask

# Creamos una instancia de la clase Flask, inicializada con el nombre del archivo
app = Flask(__name__)

# Aquí se define la primera ruta
@app.route("/") # Esto es un decorador, es muy importante
def hello(): # El nombre de la función se va a guardar como "endpoint" en el router
    return "Hello World!" # El valor de retorno de la función es lo que se muestra en el navegador
