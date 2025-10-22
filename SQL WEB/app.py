from flask import Flask, render_template
from database import obter_clientes

app = Flask(__name__)

@app.route('/')
def index():
    clientes = obter_clientes()
    return render_template('index.html', clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
