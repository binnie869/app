from flask import Blueprint, render_template
from app import db, login_manager, pubnub
from flask.ext.login import login_required, current_user
from app.auth.models import User

mod_devices = Blueprint('devices', __name__)

@mod_devices.route('/devices', methods=['GET'])
@login_required
def list_devices():
	device_list = []
	devices = db.devices.find({'username': current_user.get_id()})
	for device in devices:
		device_list.append((device['name'], device['type'], \
				device['sensors'], device['actuators'], device['setup']))
	return render_template('devices/devices_m.html',
                           title='Your Devices', my_devices=device_list)

@mod_devices.route('/add_device', methods=['POST'])
@login_required
def add_device():
	pass

@mod_devices.route('/modify_device', methods=['POST'])
@login_required
def modify_device():
	pass

@mod_devices.route('/delete_device', methods=['POST'])
@login_required
def delete_device():
	pass
