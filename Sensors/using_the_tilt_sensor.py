import RPi.GPIO as GPIO
import time

tilt_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(tilt_pin, GPIO.IN)

while True:
  if GPIO.input(tilt_pin):
    print("<--")
  else:
    print("-->")
  time.sleep(1)

GPIO.cleanup()
