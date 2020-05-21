import apriltag
import cv2
import math

img = cv2.imread('apriltags104.jpg',cv2.IMREAD_GRAYSCALE)
# five-meters105.jpg contains no targets
#img = cv2.imread('five-meters104.jpg',cv2.IMREAD_GRAYSCALE)
detector = apriltag.Detector()
result = detector.detect(img)
if result == []:
    print ("Empty arrary - no targets found")
else:
    print("Dimensions: Targets: ", len(result), "Elements: ", len(result[0])) 
    print("Results follow: ", result)
    tf = result[0].tag_family
    print(tf)
    tid = result[0].tag_id
    print(tid)
    cx0 = result[0].center[0]
    cy0 = result[0].center[1]
    print("center: x= ", cx0, " y= ", cy0)

    tf = result[1].tag_family
    print(tf)
    tid = result[1].tag_id
    print(tid)
    cx1 = result[1].center[0]
    cy1 = result[1].center[1]
    print("center: x= ", cx1, " y= ", cy1)

    # calculate and print dist between target centers
    d = (cx1-cx0)**2 + (cy1-cy0)**2
    d = math.sqrt(d)
    print("dist = ", d)
pass
