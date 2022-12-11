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
    priority = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Task %r' % self.id


@app.route('/', methods=['POST', 'GET']) ## Indica qué hacer cuando un usuario llega a la pagina principal
def index():
    return render_template('index.html') # Renderizar index.html

@app.route('/index.html', methods=['POST', 'GET'])
def index_alt():
    return render_template('index.html') # Renderizar index.html

# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)

#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return "Error while deleting the task" + id

# @app.route('/update/<int:id>', methods=['POST','GET'])
# def update(id):
#     task = Todo.query.get_or_404(id)
#     if request.method == 'POST':
#         task.content = request.form['content']
        
#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return "There was an issue when updating the task " + id
#     else:
#         return render_template('update.html', task=task)

@app.route('/Interfaz_tecnico.html', methods=['POST','GET'])   # Redireccion a Tecnico
def tecnico():
    return render_template('Interfaz_tecnico.html')

@app.route('/interfaz_encargado.html', methods=['POST','GET'])   # Redireccion a Encargado
def encargado():
    tareas = Todo.query.order_by(Todo.content).all() # para presentar las tareas por orden alfabetico
    return render_template('tareas_encargado.html', tareas = tareas)

@app.route('/interfaz_tareas.html', methods=['POST','GET'])   # Redireccion a formulario creacion tareas
def tareas():
    # if request.method == "POST":
    #     tarea_nombre = request.form['nombre']
    #     new_tarea = Todo(content=tarea_nombre)

    #     try:
    #         db.session.add(new_tarea)
    #         db.session.commit()
    #         return redirect('/')
            
    # else:
        return render_template('interfaz_tareas.html')

@app.route('/asig_tareas/<int:id>', methods=['POST','GET'])   # Redireccion a formulario asignacion tareas
def asig_tareas(id):
    tarea = Todo.query.get_or_404(id)

    if request.method == 'POST':
         task.content = request.form['content']
    else:
        return render_template('tareas_encargado.html', tarea=tarea)

if __name__ == "__main__":
    app.run(debug=True)