import os
import time
os.system("arecord --device=hw:1,0 --format S16_LE -c 2 -r 48000 -d 10 /home/pi/Videos/test.wav")
time.sleep(1)
os.system("aplay --device=plughw:0,0 /home/pi/Videos/test.wav")

