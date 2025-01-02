from flask import Blueprint, render_template, request, redirect, url_for
from .models import Todo, db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    todos = Todo.query.all()
    return render_template("home.html", todos=todos)

@main_bp.route("/add", methods=["GET", "POST"])
def add_todo():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description")
        due_date = request.form.get("due_date") 
        new_todo = Todo(
            title=title, 
            description=description, 
            completed=False, 
            due_date=due_date if due_date else None 
        )
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template("add_todo.html")


@main_bp.route("/edit/<int:todo_id>", methods=["GET", "POST"])
def edit_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if request.method == "POST":
        todo.title = request.form["title"]
        todo.description = request.form["description"]
        todo.completed = request.form["completed"] == "True"
        due_date = request.form.get("due_date")
        todo.due_date = due_date if due_date else None  
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template("edit_todo.html", todo=todo)



@main_bp.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("main.home"))
