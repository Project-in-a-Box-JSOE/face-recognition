"""
ECE196 Face Recognition Project

Purpose: This should help students get accustomed to designing their
         own functions instead of working with pre-designed ones.
         A simple file splitter can be implemented with only two 
         for loops.

Instructions: Create a script that splits all the files present in
              /images into the requested directories as stated in
              the project description (/data/...). A couple things
              have already imported for your usage, but you may
              import whatever else is needed.

              Walking through a directory can be done with os.walk or
              with other functions from the os module.

              For those who are unsure where to start, consider the
              following algorithm:

              0) Request the percentage split for Train/Val/Testing 
                 from User
              1) Enumerate all directories in /images
              2) For each directory in /images:
                2.1) Create a directory with the same name within 
                     /data/training; /data/testing; /data/validation
                2.2) Enumerate all images within /images/DIR
                2.3) For all enumerated files within /images/DIR:
                    2.2.1) Randomly split files into train/test/val dirs
                           (Ensure every directory gets at least one image)
"""

from os import listdir, walk, makedirs
from shutil import copyfile
import glob

# YOUR CODE HERE