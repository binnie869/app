from flask import Blueprint, render_template

# Define the blueprint: 'app'
mod_app = Blueprint('app', __name__)

# Set the route and accepted methods
@mod_app.route('/')
@mod_app.route('/index')
def index():
    return render_template('index_m.html', title='Welcome to Hydrobase')
