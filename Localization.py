# 7 Jun 2020; 1350
# Localization - routine to capture an image every second from a camera
# at a fixed location, detect the apriltag of each robot in the arena,
# estimate each robots position (x,y in arena coordinates) and transmit
# to the controller
#

import apriltag
import cv2
import math
import time
import glob
import os
import sys
import signal
import logging

logging.basicConfig(filename='logLocal.log', level=logging.INFO, format='%(asctime)s %(message)s')

def signal_handler(sig, frame):
    print('ctrl-c detected')
    logging.info('ctrl-c detected')
    sys.exit(0)
    
# insert parameters and constants
xcpx = 0  # x(px) center of robot tag
ycpx = 0  # y(px) center of robot tag
ytlpx = 0  # y coor of top left px of robot tag
yllpx = 0  # y coor of lower left px of robot tag

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

# insert code to capture an image every second
signal.signal(signal.SIGINT, signal_handler)

# after capturing image and writing to file, this code picks up most recent file
list_files = glob.glob('*.jpg')
latest_file = max(list_files, key=os.path.getctime)
print ("newest image file: ", latest_file)
logging.info('Newest image file: {a}'.format (a=latest_file))

photo = 'apriltags1004.jpg'
#print("IMAGE: ", photo)
t0 = time.time()
#print("start image read: ", t0)
logging.info('Start image read: {a}'.format (a=t0))
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
# t3 = time.time()
# print("start image read: ", t0)
# print("start image detect: ", t1, "  elapsed time: ", (t1-t0))
# print("start result: ", t2, "  elapsed time: ", (t2-t1))
# print("complete: ", t3, "  elapsed time: ", (t3-t2))