# 7 Jun 2020; 1350
# Localization - routine to capture an image every second from a camera
# at a fixed location, detect the apriltag of each robot in the arena,
# estimate each robots position (x,y in arena coordinates) and transmit
# to the controller

from picamera import PiCamera
from time import sleep
import datetime
import apriltag
import cv2
import math
import time
import glob
import os
import sys
import signal
import logging
import schedule
import csv



def signal_handler(sig, frame):
    print('ctrl-c detected')
    logging.info('ctrl-c detected')
    sys.exit(0)

def i_capture(name):
    file_name = "/home/pi/RPi-Ardunio/" + name + datetime.datetime.now().strftime("%Y%m%d-%H%M%S.jpg")
    camera.capture(file_name)
    print('\n', file_name)
    logging.info('File name: {a}'.format (a=file_name))

def extract_center(result, i):
    # result (input): apriltag detection list/array
    # i (input): the ith detected tag
    # xcpx (output): x center coord (in px) of tag
    # ycpx (output): y center coord (in px) of tag
    xcpx = result[i].center[0]
    ycpx = result[i].center[1]
#    print("from def ", xcpx, "  ", ycpx)
    return xcpx, ycpx

def extract_corner(result, i):
    # result (input): apriltag detection list/array
    # i (input): the ith detected tag
    # ytlpx (output): y-coord (in px) of top left corner of tag
    # yllpx (output): y-coord (in px) of lower left corner of tag
    ytlpx = result[i].corners[0,1]
    yllpx = result[i].corners[3,1]
    return ytlpx, yllpx

def calc_range(obj_hgt):
    # set up constants:
    focal_len = 3.6  # camera focal length in mm
    real_hgt = 43  # robot target height in mm
    image_hgt = 1024  # image height in px
    sensor_hgt = 2.74  # sensor height in mm
    # obj_hgt (input) in px
    # r_range is output in mm
    r_range = (focal_len * real_hgt * image_hgt)/(obj_hgt * sensor_hgt)
    return r_range

"""
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
   Initialization and Setup
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""

logging.basicConfig(filename='log_Localization.log', level=logging.INFO, format='%(asctime)s %(message)s')
signal.signal(signal.SIGINT, signal_handler)
schedule.every(1.0).seconds.do(i_capture)

# insert parameters and constants

camera = PiCamera()
camera.resolution = (1280, 1024)
# CSV file parameters
gnd_t = "gndTrth.csv"
titles = []
targets = []

xcpx = 0  # x(px) center of robot tag
ycpx = 0  # y(px) center of robot tag
ytlpx = 0  # y coor of top left px of robot tag
yllpx = 0  # y coor of lower left px of robot tag

# after capturing image and writing to file, this code picks up most recent file
list_files = glob.glob('/home/pi/RPi-Ardunio/*.jpg')
latest_file = max(list_files, key=os.path.getctime)
print ("newest image file: ", latest_file)
logging.info('Newest image file: {a}'.format (a=latest_file))

"""
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
   Calibration
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""
logging.info('Calibration start')
# read ground truth file with fiducial target parameters
with open(gnd_t, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    titles = next(csvreader)
    
    for target in csvreader:
        targets.append(target)
print('\n', "len of csv file: ", len(targets))
print('\n', targets)
print('\n', "tag 1 measured dist: ", targets[2][4])

camera.start_preview(fullscreen=False, window=(100,100,512,384))
sleep(2)  # give camera time to stablize
i_capture('calibration')
list_files = glob.glob('/home/pi/RPi-Ardunio/*.jpg')
cal_image = max(list_files, key=os.path.getctime)
print ("calibration image file: ", cal_image)
logging.info('Calibration image file: {a}'.format (a=cal_image))
img = cv2.imread(cal_image,cv2.IMREAD_GRAYSCALE)

detector = apriltag.Detector()

result = detector.detect(img)
if result == []:
    print ("Empty arrary - no targets found")
    logging.info('Empty array')
else:
    for i in range(len(result)):
        # look for targets on robot(s) as of this writing apriltag #499
        if result[i].tag_id != 499:
            # call def to extract center x,y pixels
            xcpx, ycpx = extract_center(result, i)
#            print("tag id= ", i, "  target center: ", xcpx, "  ", ycpx)
           
            # call def to extract top left and lower left corner y pixels
            # only need the y-coord as calculating the height of the tag
            ytlpx, yllpx = extract_corner(result, i)
            print("left corners: ", ytlpx, "  ", yllpx)
            obj_hgt = int(yllpx - ytlpx)
            print("robot target object height: ", obj_hgt)
            logging.info('Robot target object height: {a}'.format (a=obj_hgt))
                        
            # call def to calculate range to robot (def calc_range)
            r_range = calc_range(obj_hgt)
            print("Robot range: ", r_range)
            # call def to estimate robot azimuth angle (def calc_az_angle)
            # call def to calculate robot x,y location in arena coordinates (def calc_rposn)
        else:
            pass

i = input("Press 'a' for another image; 'c' to continue: ")
camera.stop_preview()

"""
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
    MAIN LOOP
+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
"""
#while True:
"""    
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
   Image Capture
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""

photo = 'apriltags1004.jpg'
#print("IMAGE: ", photo)
t0 = time.time()
#print("start image read: ", t0)
logging.info('Start image read')
img = cv2.imread(photo,cv2.IMREAD_GRAYSCALE)
img = cv2.imread(latest_file,cv2.IMREAD_GRAYSCALE)
#print("image size: ",img.shape)

#t1 = time.time()

detector = apriltag.Detector()
#t2 = time.time()

result = detector.detect(img)
if result == []:
    print ("Empty arrary - no targets found")
    logging.info('Empty array')
else:
    for i in range(len(result)):
        # look for targets on robot(s) as of this writing apriltag #499
        if result[i].tag_id == 5:
            # call def to extract center x,y pixels
            xcpx, ycpx = extract_center(result, i)
#            print("tag id= ", i, "  target center: ", xcpx, "  ", ycpx)
           
            # call def to extract top left and lower left corner y pixels
            # only need the y-coord as calculating the height of the tag
            ytlpx, yllpx = extract_corner(result, i)
            print("left corners: ", ytlpx, "  ", yllpx)
            obj_hgt = int(yllpx - ytlpx)
            print("robot target object height: ", obj_hgt)
            logging.info('Robot target object height: {a}'.format (a=obj_hgt))
                        
            # call def to calculate range to robot (def calc_range)
            r_range = calc_range(obj_hgt)
            print("Robot range: ", r_range)
            # call def to estimate robot azimuth angle (def calc_az_angle)
            # call def to calculate robot x,y location in arena coordinates (def calc_rposn)
        else:
            pass

"""
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
   Detect Robot(s) Targets
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""

#     print("Dimensions: Targets: ", len(result), "Elements: ", len(result[0])) 
#     print("Results follow:\n", result)
#     tf = result[0].tag_family
#     print(tf)
#     tid = result[0].tag_id
#     print(tid)
#     cx0 = result[0].center[0]
#     cy0 = result[0].center[1]
#     print("center: x= ", cx0, " y= ", cy0)
# 
#     tf = result[1].tag_family
#     print(tf)
#     tid = result[1].tag_id
#     print(tid)
#     cx1 = result[1].center[0]
#     cy1 = result[1].center[1]
#     print("center: x= ", cx1, " y= ", cy1)
# 
#     # calculate and print dist between target centers
#     d = (cx1-cx0)**2 + (cy1-cy0)**2
#     d = math.sqrt(d)
#     print("dist = ", d)
pass

"""
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
   Calculate Robot(s) Position
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""


"""
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
   Transmit Robot(s) Position to Controller
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
"""