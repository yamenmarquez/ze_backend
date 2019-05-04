# routes.py

# from flask import render_template

from app import app

from flask import request

import RPi.GPIO as GPIO
from time import sleep

@app.route('/refill')
def refill():
    
    volume_to_fill = request.args.get('volume', type=int)
    relay_pin = 18
    condition = True

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.output(relay_pin, 1)

    try:
        while condition == True:
            GPIO.output(relay_pin, 0)
            sleep(volume_to_fill)
            GPIO.output(relay_pin, 1)
            condition = False
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()

    return "Refilled by Zero empaques"

