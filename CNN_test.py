import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD
import matplotlib.pyplot as plt

model = Sequential()
model.add(Dense(units=128,activation="relu",input_shape=(784,)))
model.add(Dense(units=128,activation="relu"))
model.add(Dense(units=128,activation="relu"))
model.add(Dense(units=10,activation="softmax"))

model.compile(optimizer=SGD(0.001),loss="categorical_crossentropy",metrics=["accuracy"])

epoch = 20
model.load_weights("AppleSorting"+epoch+".h5")

def quality(filename):
	# Load this image, is cv2 compatible?
	img = 
	test_img = img.reshape((1,784))
	img_class = model.predict_classes(test_img)
	classname = img_class[0]
	if(classname==0):
		return "GOOD"
	else:
		return "BAD"
