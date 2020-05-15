import sys
import time
import RPi.GPIO as GPIO
from gpiozero import LED
from time import sleep
redPin = 23
greenPin = 20
bluePin = 21
led23 = LED(23)
led24 = LED(24)

# def blink(pin):
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(pin, GPIO.OUT)
#     GPIO.output(pin, GPIO.HIGH)
#     
# def turnOff(pin):
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(pin, GPIO.OUT)
#     GPIO.output(pin, GPIO.LOW)
#     
# def redOn():
#     blink(redPin)
#     
# def redOff():
#     turnOff(redPin)
#     
# def greenOn():
#     blink(greenPin)
#     
# def greenOff():
#     turnOff(greenPin)
#     
# def blueOn():
#     blink(bluePin)
#     
# def blueOff():
#     turnOff(bluePin)
#     
# def main():
# 
#     while True:
#         cmd = input("-->")
#         if cmd == "red on":
#             redOn()
#         elif cmd == "red off":
#             redOff()
#         elif cmd == "green on":
#             greenOn()
#         elif cmd == "green off":
#             greenOff()
#         elif cmd == "blue on":
#             blueOn()
#         elif cmd == "blue off":
#             blueOff()
#         else:
#             print("Not valid command")
#     return
# main()
while True:
    led23.on()
    led24.on()
    sleep(1.25)
    led24.off()
    sleep(1.25)
