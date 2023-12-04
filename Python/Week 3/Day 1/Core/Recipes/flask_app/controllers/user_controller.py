from flask_app import app
from flask import redirect,request,session,render_template,flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route("/dashboard")
def dash():

    if "user_id" not in session:
        return redirect("/")
    data = {"id": session["user_id"]}
    recipes=Recipe.get_all()
    loggedin_user = User.get_by_id(data)
    return render_template("dashboard.html", loggedin_user=loggedin_user,recipes=recipes)


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route("/users/login", methods=["POST"])
def user_login():
    data = {"email": request.form["email"]}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("invalid credentials", "log")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("invalid credentials", "log")
        return redirect("/")

    session["user_id"] = user_in_db.id
    return redirect("/dashboard")

@app.route("/users/register", methods=["POST"])
def user_register():

    if not User.validate(request.form):
        return redirect("/")
    pw_hashed = bcrypt.generate_password_hash(request.form["password"])
    data = {**request.form, "password": pw_hashed}
    user_id = User.create_user(data)
    session["user_id"] = user_id
    return redirect("/dashboard")



@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")