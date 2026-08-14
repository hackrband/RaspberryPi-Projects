import time
from pirc522 import RFID

rdr = RFID()
util = rdr.util()
util.debug = True

while True:
  rdr.wait_for_tag()
  (error, data) = rdr.request()
  if not error:
    print("\nDetected")
    (error, uid) = rdr.anticoll()
    if not error:
      card_data = str(uid[0]) + "," + str(uid[1])    + "," + str(uid[2]) + "," + str(uid[3])
      print("Card read UID: " + card_data)

      util.set_tag(uid)
      util.auth(rdr.auth_b, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
      util.read_out(4)
      util.read_out(6)
      util.auth(rdr.auth_a, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
      util.do_auth(util.block_addr(2, 1))
      rdr.write(9, [0x01, 0x23, 0x45, 0x67, 0x89, 0x98, 0x76,
0x54, 0x32, 0x10, 0x69, 0x27, 0x46, 0x66, 0x66, 0x64])
      util.rewrite(9, [None, None, 0xAB, 0xCD, 0xEF])
      util.read_out(9)
      util.dump()
      util.deauth()
      time.sleep(1)


