import time
import speech_recognition as sr
from gtts import gTTS
import smbus
import RPi.GPIO as GPIO
import pygame
import os

try:
    rev = GPIO.RPI_REVISION if hasattr(GPIO, "RPI_REVISION") else None
except Exception:
    rev = None

if rev == 1:
    bus = smbus.SMBus(0)
else:
    bus = smbus.SMBus(1)

class LightSensor():
    def __init__(self, addr=0x5c):
        self.DEVICE = addr
        self.POWER_DOWN = 0x00
        self.POWER_ON = 0x01
        self.RESET = 0x07
        self.CONTINUOUS_LOW_RES_MODE = 0x13
        self.CONTINUOUS_HIGH_RES_MODE_1 = 0x10
        self.CONTINUOUS_HIGH_RES_MODE_2 = 0x11
        self.ONE_TIME_HIGH_RES_MODE_1 = 0x20
        self.ONE_TIME_HIGH_RES_MODE_2 = 0x21
        self.ONE_TIME_LOW_RES_MODE = 0x23

    def convertToNumber(self, data):
        if not data or len(data) < 2:
            raise RuntimeError("Invalid data from sensor")
        raw = (data[0] << 8) | data[1]
        return raw / 1.2

    def readLight(self):
        try:
            bus.write_byte(self.DEVICE, self.ONE_TIME_HIGH_RES_MODE_1)
            time.sleep(0.18)
            data = bus.read_i2c_block_data(self.DEVICE, 0x00, 2)
            lux = self.convertToNumber(data)
            return "The room light level is {0:.1f} lux".format(lux)
        except Exception as e:
            raise RuntimeError("Failed to read light sensor: {}".format(e))

def play_mp3(path):
    if not pygame.get_init():
        pygame.init()
    if not pygame.mixer.get_init():
        try:
            pygame.mixer.init()
        except Exception:
            pass
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

r = sr.Recognizer()
sensor = LightSensor()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Please speak:")
    audio = r.listen(source)

try:
    said_text = r.recognize_google(audio)
    print("You said: %s" % said_text)
    if "light" in said_text.lower():
        print("[-] Getting light level in the room ...")
        light_sentence = sensor.readLight()
        print("[-] The light is: %s" % light_sentence)
        tts = gTTS(light_sentence)
        tmpfile = "light.mp3"
        tts.save(tmpfile)
        play_mp3(tmpfile)
        try:
            os.remove(tmpfile)
        except OSError:
            pass

except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Speech recognition request failed: %s" % e)
except RuntimeError as e:
    print("Sensor error: %s" % e)



