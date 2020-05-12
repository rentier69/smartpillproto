from RPi.GPIO as gpio
from time import sleep
from flask import Flask, render_template
import datetime
#Setup
servo = 18
gpio.setmode(gpio.BCM)
gpio.setup(servo, gpio.OUT)
#Startposition Servo
p = gpio.PWM(servo, 50)
p.start(2.5)
app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
       'title' : 'HELLO!',
       'time': timeString
       }
    return render_template('index.html', **templateData)

@app.route("/<action>")
def action(action):
    if action == "on":
        for x in range(25,125,1):
          xedit = x/10
          p.ChangeDutyCycle(xedit)
          time.sleep(0.02)

    if action == "off":
        for y in range(125,25,-1):
          yedit = y/10
          p.ChangeDutyCycle(yedit)
          time.sleep(0.02)
    templateData = {}
    return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
