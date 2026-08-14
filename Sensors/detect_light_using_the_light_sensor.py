import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import smbus
import time

if (GPIO.RPI_REVISION == 1):
  bus = smbus.SMBus(0)
else:
  bus = smbus.SMBus(1)

buzzer_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

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
    time.sleep(1)
    self.clear()
    time.sleep(0.1)
    self.turn_off()

class LightSensor():
  def __init__(self):
    self.DEVICE = 0x5c
    self.POWER_OFF = 0x00
    self.POWER_ON = 0x01
    self.RESET = 0x07
    self.CONTINUOS_LOW_RES_MODE = 0x13
    self.CONTINUOS_HIGH_RES_MODE_1 = 0x10
    self.CONTINUOS_HIGH_RES_MODE_2 = 0x11
    self.ONE_TIME_HIGH_RES_MODE_1 = 0x20
    self.ONE_TIME_HIGH_RES_MODE_2 = 0x21
    self.ONE_TIME_LOW_RES_MODE = 0x23
  
  def convertToNumber(self, data):
    return ((data[1] + (256 * data[0])) / 1.2)
  
  def readLight(self):
    data = bus.read_i2c_block_data(self.DEVICE, self.ONE_TIME_HIGH_RES_MODE_1)
    return self.convertToNumber(data)

def buzz():
  GPIO.output(buzzer_pin, GPIO.HIGH)
  time.sleep(0.5)
  GPIO.output(buzzer_pin, GPIO.LOW)

sensor = LightSensor()
lcd_screen = LCDModule()
low_light = 40

while True:
  sensor_data = sensor.readLight()
  lcd_screen.write_lcd(text = "Light level \n%slx" % sensor_data)
  print("Light Level: " + str(sensor_data) + " lx")
  if (sensor_data > 40):
    buzz()
  time.sleep(0.5)




