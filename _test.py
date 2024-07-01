import numpy as np
import cv2

img2 = cv2.imread("sample.jpg")
lower = np.array([90, 50, 50])
upper = np.array([130, 255, 255])

img = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(img, lower, upper)
mask_contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
if len(mask_contours) != 0:
    for mask_contour in mask_contours:
        if cv2.contourArea(mask_contour) > 500:
            x, y, w, h = cv2.boundingRect(mask_contour)
            cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 3) #drawing rectangle

cv2.imshow("mask image", mask) # Displaying mask image

cv2.imshow("window", img2) # Displaying webcam image

cv2.waitKey(0)

