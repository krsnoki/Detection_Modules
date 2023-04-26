# Detection_Modules
OpenCV based detection modules. 
Author: Kalyani Prashant Kolte

  OpenCV
---------------
(opensource computer Vision Library)
open source - freely available
Ithelps us for image processing
This Library is developed and released by Intel Corporation in 1999.
4.5.1 version is the most stable version in the market
made using c++

=================================================
  Application Area:
-----------------------

--> 2D and 3D feature toolkit
--> Facial Recognition
--> Gesture Recogition
--> HCI--> Human Computer Interaction
--> Mobile Robotics
--> Motion Understanding
--> Object Detection
--> Segmentation
--> SFM
--> Argumented Reality

OpenCV uses Statistical Machine Libraries
Statistical means a numeric values, that numbers are helpful to identify the reallife things.


Image is made up of pixels.

for reading image method is imread()
for showing image method used is imshow()

if you want to determine the height of image:
height = im1.shape[0]
to determine the width of image
width = im1.shape[0]
for channel values, i.e. whenever you are going to trace a image or store image it will store ccording to bit rate.
bits stored in one point of the image, whether it is 16, 32 bit channels. there are different type of channels.


Image Processing:
-------------------------
you performs different operations on image: as crop, resize, blackand white.
when you take any image captured from mobile camera:
it is a colour image
its value is between 0 - 255

we cannot process it directly:
to process it we have to convert it into grayscale image
then grayscale image is to be convert into the black and white:
black and white act as a 
'0' for black
'1' for white

converting image into grayscale:

variable = cv2.imread("imgname", cv2.IMREAD GRAYSCALE)

resizing of image:
---------------------
variable = cv2.resize(var_in_which_image_is_stored, (size you want in breadth, height))

how to save the image in python:
cv2.imwrite("imagename.extension", img_variable);


  Eroding:
-------------

kernal : is an array composed of only one, it is worked out with numpy.
numpy:
	there is a data on which we have to apply statistics.
how to create kernal: 
var = np.ones((5,5), np.uint8)

1. read the image
2. cv2.erode(image, ker)

BLUR:

why to blur image:
---------------------------
noise:
removing the unwanted content is noise reduction.
1. to remove noise from image and only you want to determine object
2. also used to remove any object.
3. to hide some data in image

blur :-> making unclear, changing intensity.

types of blur
 --->gaussian blur = 
 --->median blur = removes noise from the edges.
 --->bilateral blur = improves intensity of image


Applying border to an image:
---------------------------------
function is :
cv2.copyMakeBorder(image, topside, bottomside, leftside, rightside pixels, type of border)

----------------
  Histogram
----------------
	It is a kind of graph which shows, intensity/frequency of occurance.
Graphical representation of the image.

how to plot the histogram:
1) first we will find the ocurrance of values of 0 to 255 in image
1) from matplotlib import pyplot as plt
2) variable = cv2.calcHist([src_img], [channel value], value_mask_on_image, [bin_count_for full scale], [range of colors - 0 - 256])
3) plotting command ---> plt.plot(variable)


to convert image from one color space tto another color space value.

HSV hue saturation value
Gray


segmentation:

important concept for image segmentation is thresholding.
grey--> 0 to 255 range.
image is composed of rows and columns. every row and column has its value and that value is between the range of 0 to 255.

 why it is used:
-----------------
it is used in segmentation and object detection.

algorithm:
threshold key value;
if  key > pixel
pixel = 0
if key < pixel
pixel = 255

setting a value of row and columns as 0 or 255. 
if value of row or column is below given value then it will set as 0
and if the value of row and column is greater than given value then it will set as 255.

  types of thresholding:
----------------------------
Inverse thresholding
	it performs revese operation, that below value will become:255 and upper value will become 0
Truncate Thresholding
	above value will be set to threshold value and below value will remain as it is.
tozero thresholding
	bo=elow value will be set to zero
adaptive threshold

syntax for threshold funnction:


Q. create proper interface tkinter window
1. browse
1. button binary
2. all types of threshold 



to capture the video from live video and store it in your machine.
cv2.VideoCapture() can help
if you want to capture and save the image from yhe live camera.

Q.  1. start video
      2. capture image/show after capturing

 Working with face detection:
-----------------------------------

import cv2
face_cascade-cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread("face.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("images", gray)

faces = fcae_cascade.detectMultiscale(gray, 1.3, 5)  // 1.3 is threshold value. we normalized the image. it also resize the image internally, hence we call it as a scale factor,  5 is number of faces

for (x,y,w,h) in faces:
	cv2.rectangle(img, (x, y ), (x + w, y + h), (255, 255, 10), 2)
	cv2.imshow("faces", img)

what else we have to detect:
1. face
2. eyess
3. lefteye, righteye
4. fullbody
5. smile
6. upperbody
7.lowerbody

to workout with this you have to install imutils
to detect pedestrian:
use HOG model -->Histogram Oriented 
detection of human body walking on a street 
HOG model looks for the common area where pixels matches.
once it gets the blcak pixel. if it finds more black pixels it continues searching.
it carries on the searching for the same value on different different location.
