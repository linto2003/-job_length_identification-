# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 23:02:16 2023

@author: linto
"""

import cv2
from object_detector import HomogeneousBgDetector
import numpy as np

detector = HomogeneousBgDetector()

img = cv2.imread("book_aruco.jpg")

# Assuming the diameter of the coin is 2.5 cm
coin_diameter_cm = 2.5

# Detect objects using the homogeneous background detector
contours = detector.detect_objects(img)

for cnt in contours:
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect
    
    # Calculate the pixel-to-millimeter ratio using the coin reference
    pixel_mm_ratio = 2.5/137
    
    object_width_mm = w * pixel_mm_ratio
    object_height_mm = h * pixel_mm_ratio
    
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    
    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -2)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Width {} mm".format(round(object_width_mm, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 200, 0), 2)
    cv2.putText(img, "Height {} mm".format(round(object_height_mm, 1)), (int(x - 100), int(y + 20)), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 200, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
