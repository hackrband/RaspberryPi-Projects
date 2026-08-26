import time
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD

ir_pin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(ir_pin, GPIO.IN)

class LCDModule():
    def __init__(self):
        self.address = 0x21
        self.lcd_columns = 16
        self.lcd_rows = 2
        self.lcd = LCD.Adafruit_CharLCDBackpack(address=self.address)

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
        time.sleep(0.05)

lcd_screen = LCDModule()
delay = 0.15

try:
    while True:
        if GPIO.input(ir_pin) == 1:
            lcd_screen.write_lcd("Detected:\nblack")
            time.sleep(0.05)
        if GPIO.input(ir_pin) == 0:
            lcd_screen.write_lcd("Detected:\nno black")
            time.sleep(0.05)
except KeyboardInterrupt:
    lcd_screen.clear()
    lcd_screen.turn_off()
    GPIO.cleanup()




