import time
import RPi.GPIO as GPIO
from rpi_ws281x import *
import argparse

GPIO.setmode(GPIO.BCM)
TRIG = 16
ECHO = 26

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

LED_COUNT = 64
LED_PIN = 12
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 10
LED_INVERTED = False
LED_CHANNEL= 0

def getDistance():
  GPIO.output(TRIG, False)
  time.sleep(0.1)
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)
  
  while GPIO.input(ECHO) == 0:
    pulse_start = time.time()
  while GPIO.input(ECHO) == 1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance, 2)
  return distance

def loopColor(strip, color):
  for color in colors:
    for i in range(strip.numPixels()):
      strip.setPixelColor(i, color)
      strip.show()
      time.sleep(0.01)

def wipe(strip, color, wait_ms = 50):
  for i in range(strip.numPixels()):
    strip.setPixelColor(i, color)
  strip.show()

def wheel(pos):
  if pos < 85:
    return Color(pos * 3, 255 - pos * 3, 0)
  elif pos < 170:
    pos -= 85
    return Color(255 - pos * 3, 0, pos * 3)
  else:
    pos -= 170
    return Color(0, pos * 3, 255 - pos * 3)

def rainbowCycle(strip, wait_ms = 20, iterations = 5):
  for j in range(256 * iterations):
    for i in range(256 * iterations):
      strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
    strip.show()
    time.sleep(wait_ms / 1000)

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERTED, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

while True:

  distance = getDistance()
  print("Distance: %s" % distance)

  if(distance <= 10):
    colors = [Color(255, 0, 0)]
    loopColor(strip, colors)

  elif(distance <= 50 and distance > 10):
    colors = [Color(0, 255, 0)]
    loopColor(strip, colors)

