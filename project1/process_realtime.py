"""
ECE196 Face Recognition Project
Author: W Chen

Adapted from:
http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

Use this code as a template to process images in real time using the same techniques as the last challenge.
You need to display a (320 x 240) grayscale video feed with a random box in the center of the image. Once
you have presented a functional video feed, make a copy of this file and adjust the file to detect faces using
a larger feed resolution (640 x 480).

You need not use the faceRectangle function if you don't wish to do so.
"""

# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

def faceRectangle(imageArr):
    ''' Use this function in order to detect faces using the Haar Cascade
        and draw a rectangle around them. (Or just the random rect) '''
    # TODO: YOUR CODE HERE
    pass

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=camera.resolution)

# allow the camera to warmup
time.sleep(0.1)

# initialize the Haar cascade
hCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    # create a grey alternate image for use with the cascade
    imageGrey = cv2.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Insert a rectangle into the frame using either the Haar Cascade or manually...
    # TODO: YOUR CODE HERE

    # show the frame
    cv2.imshow("Video Feed", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
