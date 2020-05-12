# blink program from "The Official Raspberry Pi Beginner's Guide

from gpiozero import LED
from time import sleep
import time
import threading

def led_on():
    led.on()
    
def led_off():
    led.off()
    


led = LED(15)
i = 0
on_t = 1.0  #time the led is on (s)
off_t = 1.0  # time the led is off (s)
i_time = time.time() #initial time
while True:
    i = i + 1
    t_now = time.time()
    if time.time() > (i_time + off_t):
        led.on()
    
#    print ("time ", t_now)
    threading.Timer(.9, led_on)
    threading.Timer(1.3, led_off)
#    led.on()
#    sleep(1)
#    led.off()
#    sleep(.3)