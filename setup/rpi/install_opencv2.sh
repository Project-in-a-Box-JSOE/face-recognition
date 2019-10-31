#!/usr/bin/env bash

# Script to install OpenCV on Raspberry Pi 3
# Author: Simon Fong, Brian Henriquez

# Init Update
sudo apt-get -y update

# Developer tools used in build process
sudo apt-get install build-essential cmake pkg-config git -y

# Image I/O libraries
sudo apt-get install libjpeg-dev libtiff-dev libjasper-dev libpng-dev -y

# Video I/O libraries
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev -y

# GUI libraries
sudo apt-get install libgtk2.0-dev -y

# Threaded, not sure
sudo apt-get install libtbb2 libtbb-dev -y
   
# Cameras I/O
sudo apt-get install libdc1394-22-dev -y
   
# Python and Numpy
sudo apt-get install python-dev python-numpy -y
sudo apt-get install libqt4-test libqtgui4 liblapack-dev libatlas-base-dev -y

# Use Python3!
pip3 install keras opencv-contrib-python flask flask_cors

# Acquire data files for opencv
prevDir=$PWD
cascadeName="haarcascade_frontalface_default.xml"
opencvGit="https://github.com/opencv/opencv/blob/master/data/haarcascades/${cascadeName}?raw=true"
cvHaarPath=$(python3 -c "import cv2; import sys; sys.exit(cv2.data.haarcascades)" 2>&1)
cd "$cvHaarPath"
wget "$opencvGit" -q -O "$cascadeName"
echo "Make sure to use Python 3 and the cv2.data.haarcascades variable to design your program..."

# Return to prev directory
cd "$prevDir"
