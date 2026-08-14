import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD

sound_pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(sound_pin, GPIO.IN)

class LCDModule():
  def __init__(self):
    self.address = 0x21
    self.lcd_columns = 16
    self.lcd_rows = 2
    self.lcd = LCD.Adafruit_CharLCDBackpack(address = self.address)
  def turn_off(self):
    self.lcd.set_backlight(1)
  def turn_on(self):
    self.lcd.set_backlight(0)
  def clear(self):
    self.lcd.clear()
  def write_lcd(self, text):
    self.turn_on()
    time.sleep(0.1)
    self.lcd.message(text)
    time.sleep(3)
    self.clear()
    time.sleep(0.1)
    self.turn_off()
lcd_screen = LCDModule()

while True:
  if(GPIO.input(sound_pin) == True):
    lcd_screen.write_lcd(text = "Sound Detected")
    time.sleep(0.1)
  else:
    lcd_screen.clear()
    lcd_screen.turn_off()

