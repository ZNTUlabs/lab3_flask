from flask import Flask
app = Flask(__name__)

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