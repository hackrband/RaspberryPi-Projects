import time
import spidev
from rpi_ws281x import PixelStrip, Color
import RPi.GPIO as GPIO

spi = spidev.SpiDev()
spi.open(0, 1)
spi.max_speed_hz = 1000000

buzzer_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

LED_COUNT = 64
LED_PIN = 12
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_INVERT = False
LED_BRIGHTNESS = 10
LED_CHANNEL = 0

def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def all_led(val):
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(int(val), 0, 0))
    strip.show()

def alarm(sec, val):
    all_led(val)
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(sec)
    all_led(0)
    GPIO.output(buzzer_pin, GPIO.LOW)
    time.sleep(sec)

strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

gas_channel = 7
delay = 0.15

try:
    while True:
        gas_value = ReadChannel(gas_channel)
        print(gas_value)
        time.sleep(delay)
        if gas_value < 500:
            all_led(0)
            GPIO.output(buzzer_pin, GPIO.LOW)
        elif 500 <= gas_value < 650:
            alarm(0.7, 120)
        elif 650 <= gas_value < 800:
            alarm(0.4, 180)
        else:
            alarm(0.1, 255)
except KeyboardInterrupt:
    all_led(0)
    GPIO.output(buzzer_pin, GPIO.LOW)
    GPIO.cleanup()


