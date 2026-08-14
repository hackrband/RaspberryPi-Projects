import time
import datetime
from Adafruit_LED_Backpack import SevenSegment

segment = SevenSegment.SevenSegment(address=0x70)
segment.begin()

while True:
  now = datetime.datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second
  segment.clear()
  segment.set_digit(0, int(hour / 10))
  segment.set_digit(1, hour % 10)
  segment.set_digit(2, int(minute / 10))
  segment.set_digit(3, minute % 10)
  segment.set_colon(second % 2)
  segment.write_display()
  time.sleep(0.25)
  
