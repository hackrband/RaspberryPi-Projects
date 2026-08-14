import RPi.GPIO as GPIO
import time

vibration_pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(vibration_pin, GPIO.OUT)

for i in range(10):
  GPIO.output(vibration_pin, GPIO.HIGH)
  time.sleep(0.15)
  GPIO.output(vibration_pin, GPIO.LOW)
  time.sleep(0.05)

GPIO.cleanup()
