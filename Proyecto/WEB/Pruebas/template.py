from flask import Flask, render_template

app = Flask(__name__)

personas = [
    {
        "Nombre": "manolo",
        "Apellido": "El del Bombo",
        "Descripcion": "buen tipo",
    },
    {
        "Nombre": "Rosa",
        "Apellido": "Melano",
        "Descripcion": "...",
    },
    {
        "Nombre": "Rosa",
        "Apellido": "Melano",
        "Descripcion": "...",
    }
]
@app.route("/")
def home():
    return render_template('example.html', personas = personas) 