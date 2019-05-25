from PIL import Image
import cv2
import numpy as np

# load the images
def getsize(filename):
	empty = cv2.imread("background.jpg")
	empty=cv2.resize(empty,(224,224))
	full = cv2.imread(filename)
	full=cv2.resize(full,(224,224))
	# save color copy for visualization
	full_c = full.copy()
	# convert to grayscale
	empty_g = cv2.cvtColor(empty, cv2.COLOR_BGR2GRAY)
	full_g = cv2.cvtColor(full, cv2.COLOR_BGR2GRAY)
	
	cv2.imwrite("emptyg_before_blurr.jpg",empty_g)
	cv2.imwrite("fullg_before_blurr.jpg",full_g)

	# blur to account for small camera movement
	# you could try if maybe different values will maybe
	# more reliable for broader cases
	
	empty_g = cv2.GaussianBlur(empty_g, (41, 41), 0)
	full_g = cv2.GaussianBlur(full_g, (41, 41), 0)
	cv2.imwrite("emptyg_after_blurr.jpg",empty_g)
	cv2.imwrite("fullg_after_blurr.jpg",full_g)

	# get the difference between full and empty box
	diff = full_g - empty_g
	diff_name= "diff_of.jpg"
	cv2.imwrite(diff_name, diff)

	# Now check in the diff image
	im=Image.open(diff_name)
	pix=im.load()
	imtuple=im.size
	l=imtuple[0]
	b=imtuple[1]
	blackpix=0
	originalsize=0
	# Introduced error margin to reduce the error.
	errormargin=5
	for i in range(l):
		for j in range(b):
			temptuple=pix[i,j]
			if(temptuple[0]==0 and temptuple[1]==0 and temptuple[2]==0):
				blackpix+=1
			else:
				originalsize+=1

	if(originalsize>50):
		return "BIG"
	else:
		return "SMALL"

print(getsize("./try.jpg"))