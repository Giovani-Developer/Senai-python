from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200))
    concluida = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<tasks {self.titulo}>'

# Criação do banco e verificação se tarefa já existe
with app.app_context():
    db.create_all()
    if not Task.query.filter_by(titulo="Estudar db").first():
        nova_tarefa = Task(titulo="Estudar db", descricao="Aprender a modelar um database", concluida=True)
        db.session.add(nova_tarefa)
        db.session.commit()

@app.route('/')
def index():
    tarefas = Task.query.all()
    return render_template('index.html', tarefas=tarefas)

if __name__ == '__main__':
    app.run(debug=True)
