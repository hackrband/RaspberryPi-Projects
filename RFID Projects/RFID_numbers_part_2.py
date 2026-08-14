import socket
import time
import signal
from pirc522 import RFID
import pygame
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

pygame.mixer.init()

CARD_KEY = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
NUMBERS = [
  ('1', 1),
  ('2', 2),
  ('3', 3),
  ('4', 4),
  ('5', 5),
  ('6', 6),
  ('7', 7),
  ('8', 8),
  ('9', 9)
]

run = True
rdr = RFID()
util = rdr.util()
util.debug = False

def end_read(signal, frame):
  global run
  print("\nCtr+C captured, ending reading.")
  run = False
  rdr.cleanup()
    
signal.signal(signal.SIGINT, end_read)
print("\nStarting up...")
time.sleep(2)
print("Waiting for RFID card...")

while run:
  rdr.wait_for_tag()
  (error, data) = rdr.request()
  
  if not error:
    print("[-] Card Detected: " + format(data, "02x"))
  (error, uid) = rdr.anticoll()

  if not error:
    print("[-] Card read UID: " + str(uid[0]) + "," +
str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3]))
      
    util.set_tag(uid)
    util.auth(rdr.auth_b, CARD_KEY)
    util.read_out(4)
    (error, data) = rdr.read(4)
      
    if data is None:
      print("Fail to read data from card!")
      continue
        
    if data[0:4] != [78, 85, 77, 0]:
      print("Card is written with wrong data cannot be identified!")
      continue
        
      number_id = data[4]
        
      for number in NUMBERS:
        if number[1] == number_id:
          number_name = number[0]
          break
      print("Found number!")
      print("Number value: {0}".format(number_name))
        
      try:
        print(number_name)
        pygame.mixer.music.load("/home/pi/Videos/music/%s.mp3" % number_name)
        pygame.mixer.music.play()
      except socket.error:
        time.sleep(1)
        continue
