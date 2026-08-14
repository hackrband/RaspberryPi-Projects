import time
from rpi_ws281x import PixelStrip, Color

LED_COUNT = 64
LED_PIN = 12
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 30
LED_INVERTED = False
LED_CHANNEL = 0

def colorWipe(strip, color, wait_ms = 50):
  for i in range(strip.numPixels()):
    strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms / 1000.0)

def theaterChase(strip, color, wait_ms = 50, literations = 10):
  for j in range(literations):
    for  q in range(3):
      for i in range(0, strip.numPixels(), 3):
        strip.setPixelColor(i + q, color)
      strip.show()
      time.sleep(wait_ms / 1000.0)
      for i in range(0, strip.numPixels(), 3):
        strip.setPixelColor(i + q, 0)

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

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERTED, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

print('Color wipe animations.')
colorWipe(strip, Color(255, 0, 0))  # Red wipe
colorWipe(strip, Color(0, 255, 0))  # Green wipe
colorWipe(strip, Color(0, 0, 255))  # Blue wipe

print('Theater chase animations.')
theaterChase(strip, Color(127, 127, 127))  # White theater chase
theaterChase(strip, Color(127, 0, 0))  # Red theater chase
theaterChase(strip, Color(0, 0, 127))  # Blue theater chase

print('Rainbow animations.')
rainbow(strip)

print('Wipe LEDs')
colorWipe(strip, Color(0, 0, 0), 10)

