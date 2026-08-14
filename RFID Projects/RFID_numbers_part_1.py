import signal
import time
from pirc522 import RFID
import sys

try:
  input = raw_input
except NameError:
  pass

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
  print("\nCtrl+C captured. ending reading.")
  run = False
  rdr.cleanup()
  print("Starting")
  print("Waiting for RFID Input...")

while run:
  rdr.wait_for_tag()
  (error, data) = rdr.request()
  if not error:
    print("Card Detected: " + format(data, "02x"))
  (error, uid) = rdr.anticoll()
  if not error:
    print("Card read UID: " + str(uid[0]) + "," + str(uid[1]) +
"," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3]))
    print("Writing data...")
    print("\nPick a number to input into the RFID Card.")
    number_choice = None
    
    while number_choice is None:
      print("\nInput 'L' for a list of avalible numbers or simply input a desired number.")
      choice = input(">> ")
      
      if choice.lower() == 'l':
        for i, b in enumerate(NUMBERS):
          number_name, number_id = b
          print('\n{0:>6}\t{1}'.format(i+1, number_name))
      else:
        try:
          number_choice = int(choice) - 1
        except ValueError:
          print("Unrecognized option.")
          continue
          if not (0 <= number_choice <= len(NUMBERS)):
            print("Unavalible value: Block number must be within 0 to {0}.".format(len(NUMBERS)))
            continue
    number_name, number_id = NUMBERS[number_choice]
    print("You chose: {0}".format(number_name))
    choice = input("Are you happy with your choice? Y/N: ")
    if choice.lower() == "n":
      print("Aborted.")
      sys.exit(0)
    else:
      print("Do not remove card from RC522...")
      util.set_tag(uid)
      util.auth(rdr.auth_b, CARD_KEY)
      util.rewrite(4, [None, None, 0x69, 0x24, 0x40])
    
      data = bytearray(16)
      data[0:4] = b'NUM'
      data[4] = number_id & 0xFF
      util.rewrite(4, data)
      print("Data transfer successful.")
      run = False
