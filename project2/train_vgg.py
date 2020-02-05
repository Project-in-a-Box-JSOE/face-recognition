"""
ECE196 Face Recognition Project
Author: W Chen

Use this as a template to:
1. load weights for vgg16
2. load images
3. finetune network
4. save weights
"""

from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras import optimizers
from tensorflow.keras.layers import Dropout, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from sys import platform
import numpy as np
import glob
import os
import cv2
import random

""" MODIFY THESE VALUES AS NECESSARY """
TRAIN_DIR =  # TODO
VAL_DIR =  # TODO
NUM_EPOCHS = 5  # TODO
BATCH_SIZE = 16
NUM_CLASSES = 20  # TODO

# Do not modify these values
IMG_H, IMG_W, NUM_CHANNELS = 224, 224, 3
MEAN_PIXEL = np.array([104., 117., 123.]).reshape((1, 1, 3))

def load_model():
    # TODO: use VGG16 to load lower layers of vgg16 network and declare it as base_model
    # TODO: use 'imagenet' for weights, include_top=False, (IMG_H, IMG_W, NUM_CHANNELS) for input_shape

    print('Model weights loaded.')
    base_out = ...

    # TODO: add a flatten layer, a dense layer with 256 units, a dropout layer with 0.5 rate,
    # TODO: and another dense layer for output. The final layer should have the same number of units as classes

    model = Model(inputs=..., outputs=...)
    print('Built model')
    model.summary()

    # TODO: compile the model, use SGD(lr=1e-4,momentum=0.9) for optimizer, 'categorical_crossentropy' for loss,
    # TODO: and ['accuracy'] for metrics

    print('Compiled model')
    return model


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
    # Create model
    model = load_model()
    print('VGG16 created\n')

    # Read training and validation data and train the model for n epochs
    print('Load train data:')
    X_train, Y_train = load_data(TRAIN_DIR)
    print('Load val data:')
    X_val, Y_val = load_data(VAL_DIR)

    # TODO: Train model


    # TODO: Save model weights

    print('Model weights saved.')
    return


if __name__ == '__main__':
    main()
