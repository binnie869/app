from flask import Blueprint, render_template
from flask.ext.login import login_required

# Define the blueprint: 'dashboard'
mod_dashboard = Blueprint('dashboard', __name__)

@mod_dashboard.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard/dashboard_m.html',
                           title='Your Dashboard')
