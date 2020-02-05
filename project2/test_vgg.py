"""
ECE196 Face Recognition Project
Author: W Chen

Use this as a template to:
1. load saved weights for vgg16
2. load test set
3. compute accuracy for test set
"""

import numpy as np
import glob
import os
import cv2
from sys import platform
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.utils import to_categorical

""" MODIFY THESE VALUES AS NEEDED """
TEST_DIR = # TODO
MODEL_PATH = # TODO
BATCH_SIZE = 16
NUM_CLASSES = # TODO

# Do not touch these values!
IMG_H, IMG_W, NUM_CHANNELS = 224, 224, 3
MEAN_PIXEL = np.array([104., 117., 123.]).reshape((1, 1, 3))

def load_data(src_path):
    # under train/val/test dirs, each class is a folder with numerical numbers
    # X: number_images * height * width * channels
    # Y: number_images * 1
    class_path_list = sorted(glob.glob(os.path.join(src_path, '*')))
    image_path_list = []
    for class_path in class_path_list:
        image_path_list += sorted(glob.glob(os.path.join(class_path, '*jpg')))
    random.shuffle(image_path_list)
    num_images = len(image_path_list)
    print('-- This set has {} images.'.format(num_images))
    X = np.zeros((num_images, IMG_H, IMG_W, NUM_CHANNELS))
    Y = np.zeros((num_images, 1))
    # read images and labels
    for i in range(num_images):
        image_path = image_path_list[i]
        if platform == "win32":
            label = int(image_path.plot('\\')[-2]) # TODO: Test this on Windows
        else:
            label = int(image_path.split('/')[-2])
        image = cv2.imread(image_path, 1)
        image = cv2.resize(image, (IMG_H, IMG_W)) - MEAN_PIXEL
        X[i, :, :, :] = image
        Y[i, :] = label
    Y = to_categorical(Y, NUM_CLASSES)
    return X, Y


def main():
    # TODO: load model

    # compute test accuracy
    print('Load test data:')
    X_test, Y_test = load_data(TEST_DIR)

    # TODO: get accuracy

    return


if __name__ == '__main__':
    main()
