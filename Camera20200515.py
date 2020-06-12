from picamera import PiCamera
from time import sleep
import datetime
import sys
import threading
import time

def i_capture():
    file_name = "/home/pi/RPi-Ardunio/apriltags" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S.jpg")
#    file_name = "/home/pi/RPi-Ardunio/apriltags" + file_name
#camera.capture('/home/pi/RPi-Ardunio/apriltags%s.jpg' %j)
    camera.capture(file_name)
    print('\n', file_name)
    

camera = PiCamera()
camera.resolution = (1280, 1024)
camera.start_preview()



sleep(2)
# file_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S.jpg")
# print (file_name)
# file_name = "/home/pi/RPi-Ardunio/apriltags" + file_name
# print('\n', file_name)
# #camera.capture('/home/pi/RPi-Ardunio/apriltags%s.jpg' %j)
# camera.capture(file_name)

msec = int(round(time.time() * 1000))
print('\n', 'time now: ', msec)
next_i = msec + 1000
print('\n', 'next image: ', next_i)
for i in range(10):
    sleep(.5)
    now = int(round(time.time() * 1000))
    if now >= next_i:
        i_capture()
        print('\n', 'now = ', now)
        next_i = now +1000
        

# for i in range(5):
#     j = i+2000
#     sleep(1)
#     file_name = datetime.now().strtime("/home/pi/RPi-Ardunio/apriltags%Y%m%d-%H%M%S.jpg")
# #    camera.capture('/home/pi/RPi-Ardunio/apriltags%s.jpg' %j)
#     camera.capture(filename)

# camera.start_recording('video_a.h264')
# sleep(6)
# camera.stop_recording()
camera.stop_preview()
sys.exit()