# http://helloraspberrypi.blogspot.com/2015/01/raspberry-pi-arduino-i2c-communication.html

#have to run 'sudo apt-get install python-smbus'
#in Terminal to install smbus
import smbus
import time
import os

# display system info
print (os.uname())

bus = smbus.SMBus(1)

# I2C address of Arduino Slave
i2c_address = 0x07
i2c_cmd_write = 0x01
i2c_cmd_read = 0x02

def ConvertStringToBytes(src):
    converted = []
    for b in src:
        converted.append(ord(b))
    return converted

# send welcome message at start-up
bytesToSend = ConvertStringToBytes("Hello Nano")
bus.write_i2c_block_data(i2c_address, i2c_cmd_write, bytesToSend)

# loop to send message
exit = False
while not exit:
    r = input('Enter degrees; "q" to quit"')
    print(r)
    
    bytesToSend = ConvertStringToBytes(r)
    bus.write_i2c_block_data(i2c_address, i2c_cmd_write, bytesToSend)
    
    # delay 0.1 second
    # with delay will cause error of:
    # IOError: [Error 5] Input/output error
    time.sleep(0.1)
    
    data = ""
    numOfByte = bus.read_byte(i2c_address)
    print (numOfByte)
    
    for i in range(0, numOfByte):
        data += chr(bus.read_byte(i2c_address));
    print (data)
    
    if r=='q':
        exit=True