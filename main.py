from flask import Flask
from motor_driver import Motor
from flask import render_template, request
from time import sleep

import RPi.GPIO as GPIO

import time

motor = Motor(17,22,27,2,3,4)

app = Flask(__name__)


# m11=18

# m12=23

# m21=24

# m22=25


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

# GPIO.setup(m11, GPIO.OUT)

# GPIO.setup(m12, GPIO.OUT)

# GPIO.setup(m21, GPIO.OUT)

# GPIO.setup(m22, GPIO.OUT)

# GPIO.output(m11 , 0)

# GPIO.output(m12 , 0)

# GPIO.output(m21, 0)

# GPIO.output(m22, 0)

print "DOne"


a=1

@app.route("/")

def index():

    return render_template('index.html')


@app.route('/left_side')

def left_side():

    data1="LEFT"
    print "LEFT"
    motor.move(0.6,-0.4,0.2)
    sleep(0.5)
    motor.stop(0.1)

    # GPIO.output(m11 , 0)

    # GPIO.output(m12 , 0)

    # GPIO.output(m21 , 1)

    # GPIO.output(m22 , 0)

    return 'true'


@app.route('/right_side')

def right_side():

    data1="RIGHT"
    print "RIGHT"
    motor.move(0.6,0.4,0.2)
    sleep(0.5)
    motor.stop(0.1)

    #    GPIO.output(m11 , 1)

    #    GPIO.output(m12 , 0)

    #    GPIO.output(m21 , 0)

    #    GPIO.output(m22 , 0)

    return 'true'


@app.route('/up_side')

def up_side():

    data1="FORWARD"
    print "FORWARD"
    motor.move(0.6,0,0.2)
    sleep(0.5)
    motor.stop(0.1)
    #    GPIO.output(m11 , 1)

    #    GPIO.output(m12 , 0)

    #    GPIO.output(m21 , 1)

    #    GPIO.output(m22 , 0)

    return 'true'


@app.route('/down_side')

def down_side():

    data1="BACK"
    print "BACK"
    motor.move(-0.6,0,0.2)
    sleep(0.5)
    motor.stop(0.1)
    #    GPIO.output(m11 , 0)

    #    GPIO.output(m12 , 1)

    #    GPIO.output(m21 , 0)

    #    GPIO.output(m22 , 1)

    return 'true'


#@app.route('/stop')

def stop():

    data1="STOP"
    motor.stop(0.1)
#    GPIO.output(m11 , 0)

#    GPIO.output(m12 , 0)

#    GPIO.output(m21 , 0)

#    GPIO.output(m22 , 0)

    return  'true'


if __name__ == "__main__":
    print "Start"

    app.run(host='0.0.0.0',port=5010)

 
