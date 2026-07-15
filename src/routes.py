from flask import render_template, request, redirect
from app import app
from .database import db
from .models import Task

@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

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

@app.route("/delete/<int:id>")
def delete(id):

    task = Task.query.get(id)

    db.session.delete(task)
    db.session.commit()

    return redirect("/")