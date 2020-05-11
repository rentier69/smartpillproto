from gpiozero import Button, AngularServo
from time import sleep
from flask import Flask, render_template

app = Flask(__name__)

servo = AngularServo(17, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025,frame_width=0.03)
btn = Button(27)

@app.route("/")
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
       'title' : 'HELLO!',
       'time': timeString
       }
    return render_template('index.html', **templateData)

@app.route("/<deviceName>/<action>"")
def action(deviceName, action):
    if deviceName == 'servo':
        actuator == 'servo'

    if action == "on":
        servo.angle = 180
    if action == "off":
        servo.angle = 0

    return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
