import keras
from keras.layers import Dense
from keras import layers, models, optimizers
from keras.optimizers import SGD
import matplotlib.pyplot as plt
import cv2
import numpy as np
# model = Sequential()
# model = model.load('model_keras.h5')

model = models.Sequential()
model.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(150,150,3)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64, (3,3),activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(128, (3,3),activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(128, (3,3),activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Flatten())
model.add(layers.Dropout(0.5))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1,activation='sigmoid'))

model.load_weights('model_weights.h5')

nrows = 150
ncols = 150
channels = 3 # RGB

def quality(filename):
	x=[]
	x.append(filename)
	X = []
	for i in x:
		X.append(cv2.resize(cv2.imread(i,cv2.IMREAD_COLOR), (nrows,ncols), interpolation=cv2.INTER_CUBIC))
	# Convert to numpy array
	X = np.array(X)
	test_img=X[0]
	img_class = model.predict_classes(test_img)
	if(img_class>=0.5):
		return "GOOD"
	else:
		return "BAD"