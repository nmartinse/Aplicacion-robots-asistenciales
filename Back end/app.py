from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # 3 barras porque es un path relativo. SI fuera absoluto, serían 4 barras
with app.app_context():
    db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Task %r' % self.id


@app.route('/', methods=['POST', 'GET']) ## Indica qué hacer cuando un usuario llegua a la pagina principal
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        
        except:
            return "Problem while insereting in the DB"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # Este método nos devuelve todos los elementos de la tabla de la base de datos
        return render_template('index.html', tasks=tasks) # El primer tasks es el que usaremos para representar las tareas en el index.html

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Error while deleting the task" + id

@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue when updating the task " + id
    else:
        return render_template('update.html', task=task)

@app.route('/Interfaz_tecnico.html', methods=['POST','GET'])   # Redireccion a Tecnico
def tecnico():
    return render_template('Interfaz_tecnico.html')

@app.route('/interfaz_encargado.html', methods=['POST','GET'])   # Redireccion a Encargado
def encargado():
    return render_template('interfaz_encargado.html')

@app.route('/interfaz_tareas.html', methods=['POST','GET'])   # Redireccion a formulario tareas
def tareas():
    return render_template('interfaz_tareas.html')

if __name__ == "__main__":
    app.run(debug=True)