import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD
import matplotlib.pyplot as plt

model = Sequential()
model = model.load('model_keras.h5')
model.load_weights('model_weights.h5')

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