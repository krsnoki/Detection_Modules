import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')
img = cv2.imread("body.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("grayscale", gray)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)  

for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 10))
        cv2.imshow("faces", img)
