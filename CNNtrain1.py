# SOURCE: https://towardsdatascience.com/image-detection-from-scratch-in-keras-f314872006c9

import numpy as np
from keras import layers, models, optimizers
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from sklearn.model_selection import train_test_split
import os, cv2

############################ DATA PROCESSING #####################################

# Contains list of names of all images along with their pwd.
# x_good = ["/home/user/AppleSorting/234.jpg", "er"]

datadir="/home/tanmay/Desktop/GIT/AppleSorting/data"

x_good = []
for file in os.listdir("/home/tanmay/Desktop/GIT/AppleSorting/data/good"):
	x_good.append(datadir+"/good/"+file)

x_bad = []
for file in os.listdir("/home/tanmay/Desktop/GIT/AppleSorting/data/bad"):
	x_bad.append(datadir+"/bad/"+file)

# IMAGES
x = x_good+x_bad 

# print("x====",x)

# LABELS
y = [] # 0:bad and 1:good
for i in x:
	if "good" in i:
		y.append(1)
	else:
		y.append(0)


nrows = 150
ncols = 150
channels = 3 # RGB

# List of images
X = []
for i in x:
	X.append(cv2.resize(cv2.imread(i,cv2.IMREAD_COLOR), (nrows,ncols), interpolation=cv2.INTER_CUBIC))

# Convert to numpy array
X = np.array(X)
y = np.array(y)

percent_to_val = 0.20 # 20% data is assigned to validation, 80% to training
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = percent_to_val, random_state=2)

################################ MODEL ##########################################
batch_size = 32

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
model.add(layers.Dense(1,activation='softmax')) 

# model.summary()

model.compile(loss="binary_crossentropy", optimizer=optimizers.RMSprop(lr=1e-4) ,metrics=['acc'])

################################### IMAGE DATA GENERATOR ###################################

train_datagen = ImageDataGenerator(
	rescale = 1./255,
	rotation_range = 40,
	width_shift_range=0.2,
	height_shift_range=0.2,
	shear_range=0.2,
	zoom_range=0.2,
	horizontal_flip=True,
	)

val_datagen=ImageDataGenerator(rescale=1./255)
################################## TRAINING ################
train_generator = train_datagen.flow(X_train, y_train, batch_size=batch_size)
val_generator = val_datagen.flow(X_val, y_val, batch_size=batch_size)
ntrain = len(X_train)
nval = len(X_val)


history = model.fit_generator(
	train_generator,
	steps_per_epoch=ntrain,
	epochs=10,
	validation_data=val_generator,
	validation_steps=nval 
	)

############### SAVE WEIGHTS ########################

model.save_weights('model_weights.h5')
model.save('model_keras.h5')

#######################################################
# TODO: PLOT graph, to put into the poster
#######################################################