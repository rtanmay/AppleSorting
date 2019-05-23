import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD
import matplotlib.pyplot as plt

model = Sequential()
model = model.load('model_keras.h5')
model.load_weights('model_weights.h5')

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