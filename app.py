from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Holaaaaaaa, soy Angie!'

@app.route('/index')
def hola_adso():
    return '¡Que viva Vélez!'

@app.route('/index2')
def hola_adso2():
    return '¡Hi!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000) 