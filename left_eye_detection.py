import cv2
vid = cv2.VideoCapture(0)
leye = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
while(1):
    ret, img = vid.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eye_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')

    faces = leye.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 10))
        cv2.imshow("faces", img)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
        
vid.release()
