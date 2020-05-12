# blink routine with threaded timer

from gpiozero import LED
from time import sleep
import time

led = LED(15)
led.off()
def led_on():
    led.on()
    print("led on")
    
def led_off():
    led.off()
    print("led off")

led_on_state = False
d_start = time.time()
d1 = .1 # lenth of time the LED is off
d2 = .5  # length of time the LED is on
while True:
    if not led_on_state and time.time() > (d_start + d1):
        led.on()
        led_on_state = True
    else:
        if led_on_state and time.time() > (d_start + d2 + d1):
            led.off()
            led_on_state = False
            d_start = time.time()
            
