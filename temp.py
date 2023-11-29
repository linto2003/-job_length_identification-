import cv2
from object_detector import HomogeneousBgDetector
import numpy as np


parameters = cv2.aruco.DetectorParameters()
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)

detector = HomogeneousBgDetector()
detector_aruco = cv2.aruco.ArucoDetector(aruco_dict, parameters)

img = cv2.imread("job.jpg")


corners, _, _ = detector_aruco.detectMarkers(img)

int_corners = np.int0(corners)
print(int_corners)

cv2.polylines(img, int_corners,True,(0,255,0),5)

aruco_perimeter = cv2.arcLength(corners[0],True)

pixel_mm_ratio = aruco_perimeter/400



contours = detector.detect_objects(img)

for cnt in contours:
    
       
    rect = cv2.minAreaRect(cnt)
    
    (x,y),(w,h), angle = rect
    
   
    
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    
    o_w = w / pixel_mm_ratio
    o_h = h / pixel_mm_ratio
    
    cv2.circle(img,(int(x),int(y)),5,(0,0,255),-2)
    cv2.polylines(img,[box],True,(255,0,0),2)
    cv2.putText(img,"Width {} mm".format(round(o_w, 1)),(int(x-100),int(y - 20)),cv2.FONT_HERSHEY_SIMPLEX,1,(100,200,0),2)
    cv2.putText(img,"Height {} mm".format(round(o_h, 1)),(int(x-100),int(y + 20)),cv2.FONT_HERSHEY_SIMPLEX,1,(100,200,0),2)
    
    
cv2.imshow("Image",img)
cv2.waitKey(0)