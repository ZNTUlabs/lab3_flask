from flask import Flask
app = Flask(__name__)

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
arr = [7,8,18,16,15,13,12,11]

@app.route('/')
def hello_world():
    for i in arr:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, True)
        time.sleep(0.3)
    for i in arr:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, False)
        time.sleep(0.3)
    return 'Hello, World!'
