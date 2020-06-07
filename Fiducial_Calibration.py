# 7 Jun 2020; 1640
# Fiducial calibration - routine to build a list/array of fiducial tag
# tag characteristics
# Eventually I will incorporate this calibration routine into the beginning
# of the Localization routine, but for now will use seperate file for
# development

import apriltag
import cv2
import math
import time

# insert parameters and constants
xcpx = 0  # x(px) center of fiducial tag
ycpx = 0  # y(px) center of fiducial tag
ytlpx = 0  # y coor of top left px of robot tag
yllpx = 0  # y coor of lower left px of robot tag
fid_list = []
f_subi_list = [0,0,0,0,0,0]

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
#        if result[i].tag_id == 5:
            # call def to extract center x,y pixels
        xcpx, ycpx = extract_center(result, i)
        print("index= ", i, " tag id= ", result[i].tag_id, "  target center: ", xcpx, "  ", ycpx, '\n')
        f_subi_list = [0,0,0,0,0,0]
        f_subi_list[0] =result[i].tag_id
        f_subi_list[1] = xcpx
        f_subi_list[2] = ycpx
        f_subi_list[3] = 4000
        f_subi_list[4] = 1500
        f_subi_list[5] = -10
        print('\n',"f_sibi_list ", f_subi_list, '\n')
#         fid_list.append(result[i].tag_id)
#         fid_list.append(xcpx)
#         fid_list.append(ycpx)
#         fid_list.append(4000)
#         fid_list.append(1500)
#         fid_list.append(-10 )       
        
        fid_list.insert(0,f_subi_list)
        print('\n',"fid_list ", fid_list,'\n')
            # call def to extract top left and lower left corner y pixels
            # only need the y-coord as calculating the height of the tag
#             ytlpx, yllpx = extract_corner(result, i)
#             print("left corners: ", ytlpx, "  ", yllpx)
#             obj_hgt = int(yllpx - ytlpx)
#             print("robot target object height: ", obj_hgt)
#                         
#             # call def to calculate range to robot (def calc_range)
#             r_range = calc_range(obj_hgt)
#             print("Robot range: ", r_range)
#             # call def to estimate robot azimuth angle (def calc_az_angle)
#             # call def to calculate robot x,y location in arena coordinates (def calc_rposn)
# #         else:
# #             pass
                


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