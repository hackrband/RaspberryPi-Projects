import os
import time
os.system("fswebcam -r 1280x720 --no-banner /home/pi/Videos/image.jpg")
time.sleep(1)
os.system("ffmpeg -t 10 -f v4l2 -framerate 60 -video_size 1280x720 -i /dev/video0 /home/pi/Videos/output.avi")

