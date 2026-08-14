import RPi.GPIO as GPIO
import time

buzzer_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

for i in range(10):
  GPIO.output(buzzer_pin, GPIO.HIGH)
  time.sleep(0.1)
  GPIO.output(buzzer_pin, GPIO.LOW)
  time.sleep(0.1)

GPIO.cleanup()

# Fire alarm
