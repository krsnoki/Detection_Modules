import cv2
import imutils
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
vid = cv2.VideoCapture('vid.mp4')
ret, image = vid.read()
if ret:
    image = imutils.resize(image, width = max(600, image.shape[1]))
    (region,_) = hog.detectMultiScale(image, winStride = (4, 4), padding = (4, 4), scale = 1.05)
    for (x, y, w, h) in region:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow("Output", image)
        if((cv2.waitKey(25)and 0xff)==ord('q')):
            break;
        else:
            break;
vid.release()

    
