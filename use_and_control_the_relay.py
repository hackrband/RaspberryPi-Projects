import RPi.GPIO as GPIO
import time

relay_pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

for i in range(10):
  GPIO.output(relay_pin, GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(relay_pin, GPIO.LOW)
  time.sleep(0.6)

GPIO.cleanup()

# Turn signal
