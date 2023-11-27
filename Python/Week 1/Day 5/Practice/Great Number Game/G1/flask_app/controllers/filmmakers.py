from flask_app import app
from flask import redirect, render_template,request
from flask_app.models.filmmaker_model import Filmmaker

@app.route('/')
def index():
    return redirect('/filmmakers')

@app.route('/filmmakers')
def filmmakers():
    all_filmmakers=Filmmakers.get_all()
    return render_template('filmmakers.html',all_filmmakers-all_filmmakers)

@app.route('/create/filmmakers', methods=['POST'])
def create_filmmakers():
    data = {
        "name": request.form['name']
    }
    Filmmaker.save(data)
    return redirect('/filmmakers')

@app.route('/filmmakers/<int:id>')
def show_filmmakers():
    filmmakers=Filmmakers.get_by_id(data)
    return render_template('show_filmmakers.html',filmmakers-all_filmmakers)