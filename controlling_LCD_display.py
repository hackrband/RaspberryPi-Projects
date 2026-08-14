import time
import Adafruit_CharLCD as LCD

LCD_colomns = 16
LCD_rows = 2
lcd = LCD.Adafruit_CharLCDBackpack(address = 0x21)
lcd.set_backlight(0)

while True:
  user_input = input()

  if user_input == "Quit":
    break
  
  lcd.clear()
  lcd.message(user_input)
  time.sleep(0.1)

lcd.clear()
lcd.set_backlight(1)


