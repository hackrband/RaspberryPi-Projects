import RPi.GPIO as GPIO
import time
import dht11
import Adafruit_CharLCD as LCD

instance = dht11.DHT11(pin = 4)
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

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
    time.sleep(5)
    self.clear()
    time.sleep(0.1)
    self.turn_off()
  
lcd_screen = LCDModule()
result = instance.read()

if result.is_valid():
  lcd_screen.write_lcd(text=('Temp = {0:0.1f}*c\nHumd = {1:0.1f}% \n'.format(result.temperature, result.humidity)))

else:
  print("Failed to get reading. Try again.")

