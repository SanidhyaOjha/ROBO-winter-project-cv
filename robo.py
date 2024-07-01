import numpy as np
import cv2

cap  = cv2.VideoCapture(0)
prevCircle = None

dist = lambda x1,y1,x2,y2 : (x1-x2)**2 + (y1-y2)**2

while True:
    ret, frame = cap.read()
    width  = int(cap.get(3))
    height = int(cap.get(4))

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurFrame = cv2.GaussianBlur(grayFrame, (17,17), 8)

    circles = cv2.HoughCircles(blurFrame, cv2.HOUGH_GRADIENT, 1.5, 2, param1= 30, param2= 100, minRadius= 10, maxRadius= 400)
    # if circles is not None:
    #     circles = np.intp(circles)
    #     for circle in circles:

    #         cx = circle.ravel()[0]
    #         cy = circle.ravel()[1]
    #         cr = circle.ravel()[2]
    #         # print(type(cx))
    #         cv2.circle(frame, (cx,cy), cr, (0,0,0), 5)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0,]:
            if chosen is None: 
                chosen =i
            if prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
                    chosen = i
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (0,100,100) , 3)
        prevCircle= chosen

    # print(circles)

    cv2.imshow('framee', frame)

    if cv2.waitKey(1)== ord('q'):
        break


cap.release()
cv2.destroyAllWindows()











