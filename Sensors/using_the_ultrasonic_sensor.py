import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import time

GPIO.setmode(GPIO.BCM)
TRIG = 16
ECHO = 26
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

class LCDModule:
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

print("~~DMIP~~")
GPIO.output(TRIG, False)
print("~~WFSTS~~")
time.sleep(1) 
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

lcd_screen.write_lcd(text = "Distance: \n%scm" % distance)
time.sleep(5)
lcd_screen.clear()
lcd_screen.turn_off()
GPIO.cleanup()
