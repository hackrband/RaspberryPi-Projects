import time
import RPi.GPIO as GPIO
from rpi_ws281x import PixelStrip, Color
import random

LED_COUNT = 64
LED_PIN = 12
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 50
LED_INVERTED = False
LED_CHANNEL = 0
touch_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(touch_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def colorWipe(strip, color):
  for i in range(strip.numPixels()):
    strip.setPixelColor(i, color)
  strip.show()

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERTED, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

color_sequence = [Color(255, 0, 0), Color(0, 255, 0), Color(0, 0, 255)]

while True:
  random_color = random.choice(color_sequence)
  if (GPIO.input(touch_pin)):
    colorWipe(strip, random_color)
  time.sleep(0.1)
