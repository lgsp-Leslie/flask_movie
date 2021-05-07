from flask import Blueprint, render_template

home = Blueprint('home', __name__,
                 template_folder='templates/',
                 static_folder='../static/home')


@home.route('/')
def index():
    return render_template('home_index.html')
