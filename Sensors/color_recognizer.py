import time
import smbus
import Adafruit_TCS34725
from rpi_ws281x import PixelStrip, Color

LED_COUNT = 64
LED_PIN = 12
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 10
LED_INVERT = False
LED_CHANNEL = 0

def abnormal_data_processing(vol):
    if vol < 0:
        vol = 0
    if vol > 255:
        vol = 255
    return vol

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

while True:
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

    tcs = Adafruit_TCS34725.TCS34725()
    tcs.set_interrupt(False)

    r, g, b, c = tcs.get_raw_data()

    r = abnormal_data_processing(r)
    g = abnormal_data_processing(g)
    b = abnormal_data_processing(b)

    print('Color: red={0} green={1} blue={2}'.format(r, g, b))

    tcs.set_interrupt(True)
    tcs.disable()

    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(int(r), int(g), int(b)))
    strip.show()

    time.sleep(1)


