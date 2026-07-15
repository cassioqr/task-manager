from flask import render_template, request, redirect
from app import app
from .database import db
from .models import Task

@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

# Criar tasks
@app.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]

        task = Task(
            title=title,
            description=description
        )

        db.session.add(task)
        db.session.commit()

        return redirect("/")

    return render_template("create.html")

# Deletar tasks
@app.route("/delete/<int:id>")
def delete(id):

    task = Task.query.get(id)

    db.session.delete(task)
    db.session.commit()

    return redirect("/")

# Editar tasks
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    task = Task.query.get_or_404(id)

    if request.method == "POST":

        task.title = request.form["title"]
        task.description = request.form["description"]

        db.session.commit()

        return redirect("/")

    return render_template("edit.html", task=task)