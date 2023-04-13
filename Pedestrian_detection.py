import cv2
import imutils
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
img = cv2.imread("ped.jpg")
img = imutils.resize(img, width = min(400, img.shape[1]))
(region,_) = hog.detectMultiScale(img, winStride = (4, 4), padding = (4, 4), scale = 1.05)
for (x, y, w, h) in region:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("Output", img)
    
