from pulsesensor import Pulsesensor
from MCP3008 import MCP3008
import time

p = Pulsesensor()
flag = 0
touch_time=0
touch_time1=0
time_print = 0
a=MCP3008()

try:
    while True:
        Signal=a.read()
        time.sleep(0.2)
        touch_time += 200
        touch_time1 += 200
        time_print += 200

        if Signal < 10 and touch_time > 2000 and flag == 0:
            flag = 1
            print('have touch!')
            time.sleep(4)
            p.startAsyncBPM()

        if Signal > 850 and touch_time1 > 2000 and flag == 1:
            flag = 0
            print('have not touch!')
            p.stopAsyncBPM()

        if Signal > 10 and Signal < 850:
            touch_time=touch_time1=0

        if time_print>1000 and flag==1:
            time_print=0
            bpm = p.BPM

            if bpm > 0:
                print("BPM: %d" % bpm)

except:
    p.stopAsyncBPM()
