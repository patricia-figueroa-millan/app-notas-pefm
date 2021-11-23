from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    objeto = {"nombre": "Patricia", 
              "apellido": "Figueroa"
              }
    nombre = "Patricia"
    lista_nombres = ["Patricia", "Flor", "Raquel"]
    return render_template("index.html", variable = lista_nombres )

@app.route("/about")
def about():
    return "Estas en la vista about"

@app.route("/crearnota", methods=['POST'])
def crearnota():
    campotitulo = request.form["campotitulo"]
    campocuerpo = request.form["campocuerpo"]
    print(campotitulo)
    print(campocuerpo)
    return render_template("index.html", titulo = campotitulo, cuerpo = campocuerpo )
    #return "Nota creada" + " " + campotitulo + " " + campocuerpo

if __name__ == "__main__":
    app.run()
