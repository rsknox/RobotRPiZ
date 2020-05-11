# blink program from "The Official Raspberry Pi Beginner's Guide

from gpiozero import LED
from time import sleep

led = LED(15)
i = 0
while True:
    i = i + 1
    print ("top ", i)
    led.on()
    sleep(1)
    led.off()
    sleep(.3)