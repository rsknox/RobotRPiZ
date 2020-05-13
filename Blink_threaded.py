# blink routine with threaded timer

from gpiozero import LED
from time import sleep
import time
import logging
logging.basicConfig(filename='blink.log', level=logging.INFO)


led15 = LED(15)
led18 = LED(18)
led15.off()
led18.off()
def led_on():
    led.on()
    print("led on")
    
def led_off():
    led.off()
    print("led off")

led15_on_state = False
d15_start = time.time()
d151 = 1.0 # lenth of time the LED is off
d152 = 1.0  # length of time the LED is on

led18_on_state = False
d18_start = time.time()
d181 = .6 # lenth of time the LED is off
d182 = .1  # length of time the LED is on
t = int(round(time.time()*1.000))
logging.info("Start at {a}".format (a=t))
while True:
#     if not led15_on_state and time.time() > (d15_start + d151):
#         led15.on()
#         led15_on_state = True
#     else:
#         if led15_on_state and time.time() > (d15_start + d152 + d151):
#             led15.off()
#             led15_on_state = False
#             d15_start = time.time()
#             
#     if not led18_on_state and time.time() > (d18_start + d181):
#         led18.on()
#         led18_on_state = True
#     else:
#         if led18_on_state and time.time() > (d18_start + d182 + d181):
#             led18.off()
#             led18_on_state = False
#             d18_start = time.time()

    t = int(round(time.time()*1.000))
#    logging.info("Top of Loop --- {a}".format (a=t))

    

    if not led15_on_state and time.time() > (d15_start + d151):
        led15.on()
        led15_on_state = True
        t = int(round(time.time()*1.000))
        logging.info("Point A {a}".format (a=t))

    if led15_on_state and time.time() > (d15_start + d152 + d151):
        led15.off()
        led15_on_state = False
        d15_start = time.time()
        t = int(round(time.time()*1.000))
        logging.info("Point B {a}".format (a=t))
        
            
    if not led18_on_state and time.time() > (d18_start + d181):
        led18.on()
        led18_on_state = True
        t = int(round(time.time()*1.000))
        logging.info("Point C {a}".format (a=t))
        
        
    if led18_on_state and time.time() > (d18_start + d182 + d181):
        led18.off()
        led18_on_state = False
        d18_start = time.time()
        t = int(round(time.time()*1.000))
        logging.info("Point D {a}".format (a=t))    
