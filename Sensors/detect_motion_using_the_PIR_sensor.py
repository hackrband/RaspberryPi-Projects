import RPi.GPIO as GPIO
import time
from rpi_ws281x import PixelStrip, Color

LED_PIN = 12
LED_COUNT = 64
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 30
LED_INVERT = False
LED_CHANNEL = 0

def colorWipe(strip, color):
  for i in range(strip.numPixels()):
    strip.setPixelColor(i, color)
  strip.show()

motion_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_pin, GPIO.IN)

def wheel(pos):
  if pos < 85:
    return Color(pos * 3, 255 - pos * 3, 0)
  elif pos < 170:
    pos -= 85
    return Color(255 - pos * 3, 0, 255 - pos * 3)
  else:
    pos -= 170
    return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms = 20, iterations = 1):
  for j in range(256 * iterations):
    for i in range(strip.numPixels()):
      strip.setPixelColor(i, wheel((i + j) & 255))
    strip.show()
    time.sleep(wait_ms / 1000.0)

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ,
LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

strip.begin()

while True:
  if (GPIO.input(motion_pin) == 0):
    colorWipe(strip, Color(0, 0, 0))
  elif (GPIO.input(motion_pin) == 1):
    rainbow(strip)
  time.sleep(0.1)

