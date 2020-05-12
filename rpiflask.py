
import RPi.GPIO as gpio
import time

servo = 18
gpio.setmode(gpio.BCM)
gpio.setup(servo, gpio.OUT)

p = gpio.PWM(servo, 50)
p.start(2.5)
try:
  while True:
    for x in range(25,125,1):
      xedit = x/10
      p.ChangeDutyCycle(xedit)
      time.sleep(0.02)

    for y in range(125,25,-1):
      yedit = y/10
      p.ChangeDutyCycle(yedit)
      time.sleep(0.02)

except KeyboardInterrupt:
  p.stop()
