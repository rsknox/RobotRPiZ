from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.start_preview()

sleep(5)
for i in range(5):
    j = i+600
    sleep(3)
    camera.capture('apriltags%s.jpg' %j)

# camera.start_recording('video_a.h264')
# sleep(6)
# camera.stop_recording()
camera.stop_preview()
