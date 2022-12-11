from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # 3 barras porque es un path relativo. Si fuera absoluto, serían 4 barras
with app.app_context():
    db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    priority = db.Column(db.Integer, default=0)         # Nueva tabla

    def __repr__(self):
        return '<Task %r' % self.id


@app.route('/', methods=['POST', 'GET']) ## Indica qué hacer cuando un usuario llega a la pagina principal
def index():
    return render_template('index.html') # Renderizar index.html

@app.route('/index.html', methods=['POST', 'GET'])
def index_alt():
    return render_template('index.html') # Renderizar index.html

#---------------------------------------------------------------------------------------------------------#

@app.route('/Interfaz_tecnico.html', methods=['POST','GET'])     # Redireccion a Tecnico
def tecnico():
    if request.method == 'POST':
        task_content = "Prueba de texto"
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/Interfaz_tecnico.html')
        
        except:
            return "Problem while insereting in the DB"
    else:
        tasks = Todo.query.order_by(Todo.id).all() # Este método nos devuelve todos los elementos de la tabla de la base de datos
        return render_template('Interfaz_tecnico.html', tasks=tasks) # Presentar las tareas


@app.route('/delete')
def delete():
    tasks = Todo.query.order_by(Todo.id).all() # Todas las tareas
    id= tasks[-1].id                           # La ultima tarea
    
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/Interfaz_tecnico.html')
    except:
        return "Error while deleting the task" + id

@app.route('/update/<int:id>', methods=['POST','GET'])      # Redireccion a formulario tareas
def tareas(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':

        try:
            db.session.commit()
            return redirect('/Interfaz_tecnico.html')
        except:
            return "There was an issue when updating the task " + id
    else:
        return render_template('interfaz_tareas.html', task=task)
    


@app.route('/interfaz_encargado.html', methods=['POST','GET'])   # Redireccion a Encargado
def encargado():
    tasks = Todo.query.order_by(Todo.id).all() # tareas ordenadas por id
    return render_template('interfaz_encargado.html', tasks=tasks)

@app.route('/asignar/<int:id>', methods=['POST','GET'])      # Redireccion a formulario asignar tareas
def asignar(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':

        try:
            db.session.commit()
            return redirect('/interfaz_encargado.html')
        except:
            return "There was an issue when updating the task " + id
    else:
        return render_template('asignar_tarea.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)