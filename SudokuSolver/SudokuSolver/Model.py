from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import Sequential
import sys

class Model:
   # def __init__(self, model):
    #    self.input_shape = input_shape
    #    self.model = model
    #    self.num_classes = num_classes
        
    #def add_input_layer(self, filters, kernel, input_shape, function):
    #    self.model.add(Conv2D(filters=filters, kernel_size=kernel,activation=function, padding="same", 
    #                     input_shape=self.input_shape))
        
    #def add_single_conv_layer(self, filters, kernel, function):
    #    self.model.add(Conv2D(filters=filters, kernel_size=kernel,activation=function, padding="same"))
        
    #def add_double_conv_layer(self, filters, kernel, function):
    #    self.model.add(Conv2D(filters=filters, kernel_size=kernel,activation=function, padding="same"))
    #    self.model.add(Conv2D(filters=filters, kernel_size=kernel,activation=function, padding="same"))       
            
    #def add_triple_conv_layer(self, filters, kernel, function):
    #    self.model.add(Conv2D(filters=filters, kernel_size=kernel,activation=function, padding="same"))
    #    self.model.add(Conv2D(filters=filters, kernel_size=kernel,activation=function, padding="same"))
    #    self.model.add(Conv2D(filters=filters, kernel_size=kernel,activation=function, padding="same"))
        
    #def add_max_pooling(self, size, strides):
    #    self.model.add(MaxPooling2D(pool_size=size, strides=strides))
        
    #def add_dropout(self, drop):
    #    self.model.add(Dropout(drop))
        
    #def final_layers(self, density, function):
    #    self.model.add(Flatten())
    #    self.model.add(Dense(density, activation=function))
    #    self.model.add(Dense(density, activation=function))
    #    self.model.add(Dense(num_classes, activation='softmax'))

    def create_model(self): # VGG-16
        try:
            model = Sequential()
            model.add(Conv2D(filters=32, kernel_size=(3, 3),activation='relu', input_shape=(28,28,1)))
            # model.add(Conv2D(32, (3, 3), activation='relu')) - shoter way of the above code
            # MaxPooling2D pools the max value from the frame (sliding window) of 2 x 2 size
            model.add(MaxPooling2D(pool_size=(2, 2)))
            model.add(Dropout(0.20)) # Implements the drop out with the probability of 0.20
            model.add(Conv2D(64, (3, 3), activation='relu',padding='same'))
            model.add(MaxPooling2D(pool_size=(2, 2)))
            model.add(Dropout(0.25))
            model.add(Conv2D(128,(3, 3), activation='relu',padding='same'))
            model.add(MaxPooling2D(pool_size=(2, 2)))
            model.add(Dropout(0.30))
            model.add(Conv2D(256,(3, 3), activation='relu',padding='same'))
            #model.add(MaxPooling2D(pool_size=(2, 2)))
            model.add(Dropout(0.40))
            model.add(Conv2D(512,(3, 3), activation='relu',padding='same'))
            #model.add(MaxPooling2D(pool_size=(2, 2)))
            model.add(Dropout(0.50))
            # Finish the convolutional model and flatten the layer which does not affect the batch size.
            model.add(Flatten())
            # Use a dense layer (MLP) consisting of 256 neurons with relu activation functions
            model.add(Dense(256, activation='relu'))
            model.add(Dropout(0.35))
            model.add(Dense(128, activation='relu'))
            model.add(Dropout(0.25))
            model.add(Dense(10, activation='softmax'))
            model.summary()
        except:
            print("Error while creating the model: ", sys.exc_info()[0])