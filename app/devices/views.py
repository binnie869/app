from flask import Blueprint, render_template, request
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
	username = current_user.get_id()
	print(username)
	existing_device = db.devices.find_one({'name' :
                                           request.form['name']})
	if existing_device:
		device_list = []
		devices = db.devices.find({'username': current_user.get_id()})
		for device in devices:
			device_list.append((device['name'], device['type'], \
					device['sensors'], device['actuators'], device['setup']))
		return render_template('devices/devices_m.html',
	                          title='Your Devices', my_devices=device_list)
	else:
		new_device = {'username' : username, 'name' : request.form['name'], 'type' : request.form['type'], 'setup' : request.form['setup'], 'actuators' : [], 'sensors' : []}
		db.devices.insert_one(new_device)
		device_list = []
		devices = db.devices.find({'username': current_user.get_id()})
		for device in devices:
			device_list.append((device['name'], device['type'], \
					device['sensors'], device['actuators'], device['setup']))
		return render_template('devices/devices_m.html',
	                           title='Your Devices', my_devices=device_list)


@mod_devices.route('/modify_device', methods=['POST'])
@login_required
def modify_device():
	pass

@mod_devices.route('/delete_device', methods=['POST'])
@login_required
def delete_device():
	pass
