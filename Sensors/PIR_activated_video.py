import RPi.GPIO as GPIO
import time
import os

motion_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_pin, GPIO.IN)

while True:
    if (GPIO.input(motion_pin) == 0):
        print("Nothing moves ...")
    elif (GPIO.input(motion_pin) == 1):
        print("Motion detected! Taking 30s video ...")
        ts = int(time.time())
        os.system("ffmpeg -t 30 -f v4l2 -framerate 60 -video_size 1280x720 -i /dev/video0 /home/pi/Videos/%s.avi" % ts)
    time.sleep(0.1)

