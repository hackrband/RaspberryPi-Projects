import time
import RPi.GPIO as GPIO

pin_a = [18, 23, 24, 25, 26]
pin_b = [26, 25, 24, 23, 18]

GPIO.setmode(GPIO.BCM)

for i in pin_a:
  GPIO.setup(i, GPIO.OUT)

while True:
  for i in pin_a:
    GPIO.output(i, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(i, GPIO.LOW)
    time.sleep(0.5)
      
  for i in pin_a:
    GPIO.output(i, GPIO.HIGH)
    time.sleep(0.1)
      
  for i in pin_b:
    GPIO.output(i, GPIO.LOW)
    time.sleep(0.1)
      
  for i in pin_a:
    GPIO.output(i, GPIO.HIGH)
  time.sleep(2)
    
  for i in pin_b:
    GPIO.output(i, GPIO.LOW)
  time.sleep(2)

