from flask import Flask, jsonify
app = Flask(__name__)

from flask_cors import CORS
cors = CORS(app, resources={r"/*": {"origins": "*"}})

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
arr = [7,8,18,16,15,13,12,11]
for pin in arr:
	GPIO.setup(pin, GPIO.OUT)


@app.route('/')
def index():
    return "Hello, it's programm to use Raspberry outputs pins!"


@app.route('/pin/on/<int:pin_id>')
def pin_on(pin_id):
    # 
	if pin_id in arr:
		GPIO.output(pin_id, True)
		return 'Pin ID=%d was turn ON' % pin_id
	else:
		return 'Pin wrong ID=%d for pin' % pin_id


@app.route('/pin/off/<int:pin_id>')
def pin_off(pin_id):
    # 
	if pin_id in arr:
		GPIO.output(pin_id, False)
		return 'Pin ID=%d was turn OFF' % pin_id
	else:
		return 'Pin wrong ID=%d for pin' % pin_id


@app.route('/pin/on/all')
def all_pin_on():
    # 
	for pin in arr:
		GPIO.output(pin, True)
	return "All pins was turn ON"


@app.route('/pin/off/all')
def all_pin_off():
    # 
	for pin in arr:
		GPIO.output(pin, False)
	return "All pins was turn OFF"

#  API

@app.route('/api/pin/on/<int:pin_id>')
def api_pin_on(pin_id):
    # 
	if pin_id in arr:
		GPIO.output(pin_id, True)
		return jsonify(data='Pin ID=%d was turn ON' % pin_id)
	else:
		return jsonify(data='Pin wrong ID=%d for pin' % pin_id)


@app.route('/api/pin/off/<int:pin_id>')
def api_pin_off(pin_id):
    # 
	if pin_id in arr:
		GPIO.output(pin_id, False)
		return jsonify(data='Pin ID=%d was turn OFF' % pin_id)
	else:
		return jsonify(data='Pin wrong ID=%d for pin' % pin_id)


@app.route('/api/pin/on/all')
def api_all_pin_on():
    # 
	for pin in arr:
		GPIO.output(pin, True)
	return jsonify(data="All pins was turn ON")


@app.route('/api/pin/off/all')
def api_all_pin_off():
    # 
	for pin in arr:
		GPIO.output(pin, False)
	return jsonify(data="All pins was turn OFF")