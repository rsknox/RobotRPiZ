import apriltag
import cv2
import math
import time
photo = 'apriltags600.jpg'
print("IMAGE: ", photo)
t0 = time.time()
print("start image read: ", t0)
img = cv2.imread(photo,cv2.IMREAD_GRAYSCALE)
print("image size: ",img.shape)
# five-meters105.jpg contains no targets
#img = cv2.imread('five-meters104.jpg',cv2.IMREAD_GRAYSCALE)
t1 = time.time()

detector = apriltag.Detector()
t2 = time.time()

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
t3 = time.time()
print("start image read: ", t0)
print("start image detect: ", t1, "  elapsed time: ", (t1-t0))
print("start result: ", t2, "  elapsed time: ", (t2-t1))
print("complete: ", t3, "  elapsed time: ", (t3-t2))