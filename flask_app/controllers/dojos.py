from flask_app import app
from flask import render_template , session , redirect , request
from flask_app.models.dojo import Dojo
from flask_app.models import ninja


@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():

    dojos=Dojo.get_all()

    return render_template("index.html" , alldojos = dojos)

@app.route('/dojo/create' , methods=['POST'])
def dojo_create():
    Dojo.create(request.form)

    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data={
        'id':id
    }
    return render_template('show.html' , dojo = Dojo.get_one(data) )


@app.route('/ninjas')
def ninjas():
    return render_template("new.html" , dojos =Dojo.get_all())


@app.route('/create/ninja' , methods=['POST'])
def ninja_create():
    ninja.Ninja.create(request.form)
    return redirect('/')