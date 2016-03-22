from flask import Blueprint, render_template
from app import db, login_manager, pubnub
from flask.ext.login import login_required

mod_experiments = Blueprint('experiments', __name__)

@mod_experiments.route('/experiments', methods=['GET'])
@login_required
def list_experiments():
	return render_template('experiments/experiments_m.html',
                           title='Your Experiments')