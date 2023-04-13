import tkinter as tk
import cv2
vid = cv2.VideoCapture()
def detect_face():
    face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    while(1):
        ret, img = vid.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(img,(x,y), (x + w, y + h), (255, 255, 10), 2)
            cv2.imshow("Face", img)
            if((cv2.waitKey(2)& 0xff)==ord('q')):
                break

def detect_eye():
    eye = cv2.CascadeClassifier('haarcascade_eye.xml')
    while(1):
        ret, img = vid.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        


def smile():
    smile = cv2.CascadeClassifier('haarcascade_smile.xml')
    while(1):
        ret, img = vid.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = smile.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 10))
            cv2.imshow("faces", img)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
top = tk.Tk()
top.config(bg = "LemonChiffon")

b1 = tk.Button(text = "Detect Face", command = detect_face)
b1.pack()

b2 = tk.Button(text = "Detect Eye", command = detect_eye)
b2.pack()

b3 = tk.Button(text = "Detect Full Body", command = detect_fullbody)
b3.pack()

b4 = tk.Button(text = "Detect Glasses", command = detect_glasses)
b4.pack()

b5 = tk.Button(text = "Detect left_eye", command = det_leye)
b5.pack()

b6 = tk.Button(text = "Detect Right_eye", command = det_reye)
b6.pack()

b7 = tk.Button(text = "Detect Smile", command = smile)
b7.pack()

b8 = tk.Button(text = "Detect Upperbody", command = upperbody)
b8.pack()

b9 = tk.Button(text = "Detect Lowerbody", command = lowerbody)
b9.pack()
top.mainloop()
