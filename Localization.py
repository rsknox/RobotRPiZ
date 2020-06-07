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

# insert parameters and constants
xcpx = 0
ycpx = 0

def extract_center(result, i):
    # result (input): apriltag detection list/array
    # i (input): the ith detected tag
    # xcpx (output): x center coord (in px) of tag
    # ycpx (output): y center coord (in px) of tag
    xcpx = result[i].center[0]
    ycpx = result[i].center[1]
    print("from def ", xcpx, "  ", ycpx)
    return xcpx, ycpx

# insert code to capture an image every second
photo = 'apriltags1004.jpg'
#print("IMAGE: ", photo)
#t0 = time.time()
#print("start image read: ", t0)
img = cv2.imread(photo,cv2.IMREAD_GRAYSCALE)
#print("image size: ",img.shape)

#t1 = time.time()

detector = apriltag.Detector()
#t2 = time.time()

result = detector.detect(img)
if result == []:
    print ("Empty arrary - no targets found")
else:
    for i in range(len(result)):
        # look for targets on robot(s) as of this writing apriltag #499
        if result[i].tag_id == 5:
            # call def to extract center x,y pixels (def extract_center)
#            extract_center(result, i, xcpx, ycpx)
            xcpx, ycpx = extract_center(result, i)
            print("tag id= ", i, "  target center: ", xcpx, "  ", ycpx)
            # call def to extract top left and lower left corner x,y pixels (def extract_corner)
            # call def to calculate range to robot (def calc_range)
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