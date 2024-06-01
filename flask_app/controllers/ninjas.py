from flask_app import app
from flask import redirect , render_template , request
from flask_app.models import dojo , ninja


@app.route('/ninjas')
def ninjas():
    return render_template("new.html" , dojos =dojo.Dojo.get_all())


@app.route('/create/ninja' , methods=['POST'])
def ninja_create():
    ninja.Ninja.create(request.form)
    return redirect('/')