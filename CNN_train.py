import keras
from keras.layers import Dense, Conv2D
from keras.models import Sequential
from keras.optimizers import SGD
import matplotlib.pyplot as plt

"""
			TO DO
			-----

x is the images, y is the label

for y
0: Bad
1: Good

These are numpy.ndarray

train_x=[]
train_y=[]

val_x=[]
val_y=[]

For testing, we will send images one by one.

"""

# Total images = 400, 200 good and 200 bad
# TODO image generation. see this from keras.preprocessing.image import ImageDataGenerator 
# They have used it here--> https://github.com/gsurma/image_classifier/blob/master/image_classifier.ipynb

num_of_training =  280 # 70% training

num_of_validation = 120 # 30% validation

train_x = train_x.reshape(num_of_training,784)
val_x = val_x.reshape(num_of_validation,784)

train_y = keras.utils.to_categorical(train_y,2)
val_y = keras.utils.to_categorical(val_y,2)

# Model
# Add Conv2D layer
model = Sequential()
model.add(Dense(units=128,activation="relu",input_shape=(784,)))
model.add(Dense(units=128,activation="relu"))
model.add(Dense(units=128,activation="relu"))
model.add(Dense(units=10,activation="softmax"))

model.compile(optimizer=SGD(0.001),loss="categorical_crossentropy",metrics=["accuracy"])

epoch=20

model.fit(train_x,train_y,batch_size=32, epochs=epoch,verbose=1, validation_data=(val_x,val_y))

model.save("AppleSorting"+epoch+".h5")
