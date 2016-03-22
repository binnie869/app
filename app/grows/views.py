from flask import Blueprint, render_template
from app import db, login_manager, pubnub
from flask.ext.login import login_required

mod_grows = Blueprint('grows', __name__)

@mod_grows.route('/grows', methods=['GET'])
@login_required
def list_grows():
	return render_template('grows/grows_m.html',
                           title='Your Grows')