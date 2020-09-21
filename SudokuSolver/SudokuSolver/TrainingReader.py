from __future__ import print_function
import numpy as np
import sys
import keras
from keras import backend as bck
from keras.datasets import mnist

class TrainingReader:
    def __init__(self):
        self.num_classes = 10
        self.size_rows = 28
        self.size_cols = 28
        self.input_shape = ()
        self.x_test = []
        self.x_train = []
        self.y_test = []
        self.y_train = []

    def adjust_images(self, x_train, x_test):
        # Channels adjustment
        if bck.image_data_format() == 'channels_first':
            x_train = x_train.reshape(x_train.shape[0], 1, self.size_rows, self.size_cols)
            x_test = x_test.reshape(x_test.shape[0], 1, self.size_rows, self.size_cols)
            self.input_shape = (1, self.size_rows, self.size_cols)
        else:
            x_train = x_train.reshape(x_train.shape[0], self.size_rows, self.size_cols, 1)
            x_test = x_test.reshape(x_test.shape[0], self.size_rows, self.size_cols, 1)
            self.input_shape = (self.size_rows, self.size_cols, 1)
        # Type adjustment
        x_train = x_train.astype('float32') / 255
        x_test = x_test.astype('float32') / 255
        return x_train, x_test

    def create_labels(self, y_original):
        y_new = keras.utils.to_categorical(y_original, self.num_classes)
        return y_new

    def read_mnist(self):
        try:
            (x_train, y_train), (x_test, y_test) = mnist.load_data()
            self.x_train, self.x_test = self.adjust_images(x_train, x_test)
            self.y_train = self.create_labels(y_train)
            self.y_test = self.create_labels(y_test)
            print("MNIST dataset was read correctly!")
        except:
            print("Unexpected error in TrainingReader: ", sys.exc_info()[0])
            raise
            



